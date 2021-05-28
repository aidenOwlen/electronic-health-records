import csv 
import sqlite3
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from PyQt4.QtCore import QThread 
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel

from desi import * 
import cat 
import mysql.connector
import os
from selected import *
from shutil import copyfile
import os.path
import datetime 



DELETE = False
#FirstTime = True
if not os.path.isfile("database.db"):
    cat.CreateBase()

class threadModel(QThread):
    def __init__(self,model):
        QThread.__init__(self)
        self.model = model
    def run(self):
        co = sqlite3.connect("database.db")
        cu = co.cursor()
        qu = """SELECT DISTINCT NAME FROM PATIENTS"""
        try:
            cu.execute(qu)
            
            co.commit()
            roo2 = cu.fetchall()

        except:
            
            co.rollback()
        finally:
            co.close()
        
        listopo = []
        for i in roo2:
            listopo.append(i[0])
            self.model.setStringList(listopo)
            
    
class selectedPatient(Ui_Form):
    def retranslateUi(self,Form):
        super(__class__,self).retranslateUi(Form)
        header = self.FTable.horizontalHeader()
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.Stretch)
        header.setResizeMode(4, QtGui.QHeaderView.Stretch)
        header.setResizeMode(5, QtGui.QHeaderView.Stretch)
       
       
        self.FSave.clicked.connect(self.ha)
        self.FClose.clicked.connect(self.close)
        self.FDelete.clicked.connect(self.delete)



        self.FNumber.setText(FNum)
        self.FDate.setText(FDate)
        self.FName.setText(FName)
        self.FSeance.setText(FSeance)
        self.FSeance.setValidator(QIntValidator())
        self.FNumber.setReadOnly(True)
        self.FDate.setReadOnly(True)
        
        indexx = self.FEncaissement.findText(FEncaissement)
        self.FEncaissement.setCurrentIndex(indexx)
        self.FSomme.setText(FSomme)
        self.FSomme.setValidator(QDoubleValidator())
        self.FComment.setText(FComment)
        if FMutualiste == "Oui":
            self.FMutualisteO.setChecked(True)
        elif FMutualiste == "Non":
            self.FMutualisteN.setChecked(True)
        try:
            if FEncaissement == "Kenza":
                La_Somme_Kenza = float(FSomme) 
                La_Somme_Ibtissam = "0"
            elif FEncaissement == "Cabinet":
                La_Somme_Kenza = float(FSomme) * 60 / 100
                La_Somme_Ibtissam = float(FSomme) * 40 / 100
            elif FEncaissement == "50/50":
                La_Somme_Kenza = float(FSomme) * 50 / 100
                La_Somme_Ibtissam = float(FSomme) * 50 / 100
            else:
                La_Somme_Kenza = "Error"
                La_Somme_Ibtissam = "Error"
        except:
                La_Somme_Kenza = "Error, somme indefinie"
                La_Somme_Ibtissam = "Error, somme indefinie"

        BtissamTotal = cat.SELECTSELECTIBTISSAM(self.FName.text())
        BtissamTotal = BtissamTotal[0][0]
        if str(BtissamTotal) == "None":
            BtissamTotal = 0
        BtissamTotal2 = ( BtissamTotal * 40 ) /100
        self.FTotal4.setText("Total ibtissam : {}".format(str(BtissamTotal2)))

        KenzaTotal = (BtissamTotal * 60) / 100


        Ken = cat.SELECTSELECTSELECT(self.FName.text())
        Ken = Ken[0][0]
        if str(Ken) == "None":
            Ken = 0
        KenzaTotal += Ken 
        self.FTotal3.setText("Total Kenza : {}".format(str(KenzaTotal)))



        fetchT = cat.SelectTotalPatient(FName)
        fetchT2 = cat.SelectTotalPatient2(FName)
        fetchT3 = cat.SelectTotalPatient3(FName)
        self.FTotal2.setText("Total seances : " + str(fetchT2[0][0]))
        self.FTotal1.setText("Total Paye : " + str(fetchT[0][0]))
        self.Average.setText("Average paye : " + str(fetchT3[0][0]))
        self.FPatientName1.setText(FName + " : ")
        self.FN.setText(FName + " : ")

        self.FKenza.setText(str(La_Somme_Kenza))
        self.FIbtissam.setText(str(La_Somme_Ibtissam))
        self.FKenza.setReadOnly(True)
        self.FIbtissam.setReadOnly(True)

        fetchT4 = cat.selectPatientHistory(FName)
        print(fetchT4)
        if len(fetchT4) >= 1:
            self.FTable.setRowCount(0)
        for row_number,row_data in enumerate(fetchT4):
            self.FTable.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.FTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        
    def delete(self):
        global DELETE
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure ?")
        msg.setInformativeText("Etes vous sur de vouloir SUPPRIMER le truc ?")
        msg.setWindowTitle("Suppression des donnees")
        
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        retval2 = msg.exec_()
        if retval2 == 16384:
            cat.DeleteFromDatabase(self.FNumber.text())
            DELETE = True 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Updated")
            msg.setInformativeText("It has been deleted\nIt will still appear in the main table until you restart the program.")
            msg.setWindowTitle("Updated")
            The_Patient_History.close()
        else:
            DELETE = False



    def ha(self):
        global UpdateListo
        UpdateListo = []

        newName = str(self.FName.text())
        newSeance = str(self.FSeance.text())
        newEncaissement = str(self.FEncaissement.currentText())
        newSomme = str(self.FSomme.text())
        newComment = str(self.FComment.toPlainText())
        if self.FMutualisteO.isChecked:
            newMutualiste = "Oui"
        elif self.FMutualisteN.isChecked:
            newMutualiste = "Non"
        else:
            newMutualiste = ""
        

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure ?")
        msg.setInformativeText("Etes vous sur de vouloir modifier le truc ?")
        msg.setWindowTitle("Modification des donnees")
        msg.setDetailedText("""Nom : {}\nSeance : {}\nEncaissement : {}\nSomme : {}\nCommentaire : {}""".format(newName,newSeance,newEncaissement,newSomme,newComment))
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == 16384:
            cat.UpdateDatabase(newName,newMutualiste,newEncaissement,newSeance,newSomme,newComment,self.FNumber.text())
           
            UpdateListo = [newName,newMutualiste,newEncaissement,newSeance,newSomme,newComment]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Updated")
            msg.setInformativeText("Database has been updated.\nFor the update to appear in the main table khas tayt7el wytsed lprogramme")
            msg.setWindowTitle("Updated")
           
       
            msg.exec_()
            The_Patient_History.close()


        else:
            
            UpdateListo = []




    def close(self):
        The_Patient_History.close()
       
        
       


class myInterface(Ui_MainWindow):
    def retranslateUi(self,MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
        self.add.clicked.connect(self.ADD)
        self.search.textChanged.connect(self.SEARCH)
        header = self.table1.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(6, QtGui.QHeaderView.Stretch)
        #header.setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(7, QtGui.QHeaderView.Stretch)
        self.DeleteDrugs_2.clicked.connect(self.DeleteIt)
        self.SHClose.clicked.connect(self.CLOSI)
        self.BClose_2.clicked.connect(self.EXCEL)

        self.actionClose.triggered.connect(self.CLOSI)
        self.actionBackup_database.triggered.connect(self.BACKK)
        self.actionClear_database.triggered.connect(self.clear)
        

        self.completer = QCompleter()
        self.nom.setCompleter(self.completer)
        self.model = QStringListModel()
        self.completer.setModel(self.model)
        self.modelStart = threadModel(self.model)
        self.modelStart.start()

        self.plus.clicked.connect(self.PLUS)
       
        self.SHDate2.setCalendarPopup(True)
        self.SHDate1.dateChanged.connect(self.date1)
        self.SHDate2.dateChanged.connect(self.date1)
        self.rxN.setReadOnly(True)
        self.somme.setValidator(QIntValidator())
        self.seance.setValidator(QIntValidator())
        self.excel.clicked.connect(self.EXCELL)
        self.searchby.addItem("NAME")
        self.searchby.addItem("MUTUALISTE")
        self.searchby.addItem("ENCAISSEMENT")

        self.BACKUP_3.clicked.connect(self.BACKK)
        
        self.SHDate2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.SHDate1.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 3), QtCore.QTime(23, 59, 59)))

        self.calendarr2.setCalendarPopup(True)
        self.calendarr2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.encaissement.addItem("50/50")

        self.searchby.addItem("SOMME")
        self.searchby.addItem("DATE")
        self.searchby.addItem("COMMENT")
        self.searchby.addItem("ID")
        self.SHRefresh.clicked.connect(self.date1)
        self.BClose.clicked.connect(self.close)
        self.BCalculator_3.clicked.connect(self.calc)
        self.EditDrugs_2.clicked.connect(self.edit)
        self.BPatient_2.clicked.connect(self.pat)
        thetime = str(datetime.datetime.now())
        thetime = thetime.split(".")
        thetime = str(thetime[0])
        

        self.MyDate.setText(thetime)

        self.calendarWidget.clicked[QtCore.QDate].connect(self.showDate)


        self.tim = QTimer()
        self.tim.setInterval(1000*60)
        self.tim.timeout.connect(self.dd)
        self.tim.start()

        XFETCH = cat.FetchDatabase()

        if len(XFETCH) >= 1:
            self.table1.setRowCount(0)
        for row_number,row_data in enumerate(XFETCH):
            self.table1.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table1.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        try:
            self.ss = cat.SearchId()
            self.rxN.setText(str(self.ss[0][0]))
        except:
            pass

    def PLUS(self):
        cos = sqlite3.connect("database.db")
        cus = cos.cursor()
        qus = """SELECT NAME,MUTUALISTE,ENCAISSEMENT,SEANCE,SOMME,COMMENT FROM PATIENTS WHERE NAME = "{}" ORDER BY ID DESC """.format(self.nom.text())
        try:
            cus.execute(qus)
            cos.commit()
            syko = cus.fetchall()
        except Exception as K:
            print(K)
            cos.rollback()
        finally:
            cos.close()
        print(syko)
        self.nom.setText(syko[0][0])
        if syko[0][1] == "Oui":
            self.mutualiste.setCurrentIndex(0)
        elif syko[0][1] == "Non":
            self.mutualiste.setCurrentIndex(1)
        self.seance.setText(syko[0][3])
        self.somme.setText(syko[0][4])
        self.comment.setText(syko[0][5])
        if syko[0][2] == "Kenza":
            self.encaissement.setCurrentIndex(0)
        elif syko[0][2] == "Cabinet":
            self.encaissement.setCurrentIndex(1)
        elif syko[0][2] == "50/50":
            self.encaissement.setCurrentIndex(2)
        
        
    
        
    def clear(self):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Are you sure ?")
            msg.setInformativeText("This action will erase everything !\nCette action supprimera toutes les données\nEtes vous surs de vouloir continuer ?")
            msg.setWindowTitle("Suppression des donnees")
            
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            retval3 = msg.exec_()
            if retval3 == 16384:
                os.remove("database.db")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Deleted")
                msg.setInformativeText("The whole database has been deleted\nIt will disappear after you close the program.")
                msg.setWindowTitle("Suppression des donnees")
                msg.exec_()
            else:
                pass



    def CLOSI(self):
        MainWindow.close()

    def DeleteIt(self):
        myroww = self.table2.currentRow()
        try:
            myIDD = self.table2.item(myroww,0).text()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Are you sure ?")
            msg.setInformativeText("Etes vous sur de vouloir la prescription numéro {}?".format(str(myIDD)))
            msg.setWindowTitle("Suppression des donnees")
            
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            retval3 = msg.exec_()
            if retval3 == 16384:
                cat.DeleteFromDatabase(str(myIDD))
             
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Updated")
                msg.setInformativeText("It has been deleted\nIt will still appear in the main table until you restart the program.")
                msg.setWindowTitle("Updated")
                self.table2.removeRow(myroww)
            else:
                pass
                
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nothing selected")
            msg.setInformativeText("Please select a row to delete")
            msg.setWindowTitle("Suppression des donnees")
            
            
            retval3 = msg.exec_()

        
    def pat(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("In progress ..")
        msg.setInformativeText("Nothing here yet.")
        msg.setWindowTitle("Not functional")
           
       
        msg.exec_()

    def edit(self):
        global FNum,FDate,FName,FSeance,FMutualiste,FEncaissement,FSomme,FComment,The_Patient_History,UpdateListo,DELETE
        FNum = ""
        FDate = ""
        FName = ""
        FSeance = "" 
        FMutualiste = ""
        FEncaissement = ""
        FSomme = ""
        FComment = ""
        try:
            cr = self.table2.currentRow()
            FNum = self.table2.item(cr,0).text()
            FNum = str(FNum)

           
            selected = cat.SelectById(FNum)
            FNum = str(selected[0][0])
           
            FDate = str(selected[0][1])
            FName = str(selected[0][2])
            FSeance = str(selected[0][3])
            FMutualiste = str(selected[0][4])
            FEncaissement = str(selected[0][5])
            FSomme = str(selected[0][6])
            FComment = str(selected[0][7])

            #print(selected)

            The_Patient_History = QtGui.QDialog(MainWindow)
            The_Patient_History_ui = selectedPatient()
            The_Patient_History_ui.setupUi(The_Patient_History)
            The_Patient_History.show()
            The_Patient_History.exec_()
            print("we here")

            try:
                self.table2.setItem(cr,1,QTableWidgetItem(UpdateListo[0]))
                self.table2.setItem(cr,2,QTableWidgetItem(UpdateListo[1]))
                self.table2.setItem(cr,3,QTableWidgetItem(UpdateListo[2]))
                self.table2.setItem(cr,4,QTableWidgetItem(UpdateListo[3]))
                self.table2.setItem(cr,5,QTableWidgetItem(UpdateListo[4]))
                self.table2.setItem(cr,6,QTableWidgetItem(UpdateListo[5]))
            except:
                pass
            if DELETE == True:
                self.table2.removeRow(cr)
                DELETE = False 
            DELETE = False
                
            UpdateListo = []
        except Exception as K:
            print(K)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nothing selected")
            msg.setInformativeText("Please select a row, you selected nothing")
            msg.setWindowTitle("Select a row")
           
       
            msg.exec_()

        

            

        


    def showDate(self):
        year3 = str(self.calendarWidget.selectedDate().year())
        month3 = str(self.calendarWidget.selectedDate().month())
        if len(month3) == 1:
            month3 = "0" + month3

        day3 = str(self.calendarWidget.selectedDate().day())
        if len(day3) == 1:
            day3 = "0" + day3
        self.Date3Value = year3 + "-" + month3 + "-" + day3
        silo = cat.SelectByDate(self.Date3Value)

       
        self.table2.setRowCount(0)
        for row_number,row_data in enumerate(silo):
            self.table2.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                 self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))
       

        #self.DELETE.clicked.connect(self.delete)

    def date1(self):
        global XFETCH2
        year = str(self.SHDate1.date().year())
        month = str(self.SHDate1.date().month())
        if len(month) == 1:
            month = "0" + month

        day = str(self.SHDate1.date().day())
        if len(day) == 1:
            day = "0" + day
        self.Date1Value = year + "-" + month + "-" + day
        year2 = str(self.SHDate2.date().year())
        month2 = str(self.SHDate2.date().month())
        if len(month2) == 1:
            month2 = "0" + month2

        day2 = str(self.SHDate2.date().day())
        if len(day2) == 1:
            day2 = "0" + day2
        self.Date2Value = year2 + "-" + month2 + "-" + day2
        print(self.Date2Value)

        
   

        XFETCH2 = cat.SearchByDate(self.Date1Value,self.Date2Value)
        XFF = cat.SelectTotalDatabase(self.Date1Value,self.Date2Value)
        XFF = XFF[0][0]
        if str(XFF) == "None":
            XFF = 0

        XFF2 = cat.SelectTotalDatabaseIbtissam(self.Date1Value,self.Date2Value)
        XFF2 = XFF2[0][0]
        if str(XFF2) == "None":
            XFF2 = 0

        IbtissamSomme = XFF2 * 40 / 100

        KenzaSomme = XFF2 * 60 / 100

        XFF3 = cat.SelectTotalDatabaseKenza(self.Date1Value,self.Date2Value)
        XFF3 = XFF3[0][0]
        if str(XFF3) == "None":
            XFF3 = 0
        KenzaSomme += XFF3

        XFF4 = cat.SelectEqualDatabaseIbtissam(self.Date1Value,self.Date2Value)
        XFF4 = XFF4[0][0]
        if str(XFF4) == "None":
        	XFF4 = 0
        KenzaSomme += XFF4/2
        IbtissamSomme += XFF4/2




        self.SHLABEL.setText("Total : {}".format(str(XFF)))
        self.SHLABEL3.setText("Ibtissam : {}".format(str(IbtissamSomme)))
        self.SHLABEL2.setText("Kenza : {}".format(str(KenzaSomme)))



        
       
        self.table2.setRowCount(0)
        for row_number,row_data in enumerate(XFETCH2):
            self.table2.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                 self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))
    def dd(self):
        thetime = str(datetime.datetime.now())
        thetime = thetime.split(".")
        thetime = str(thetime[0])
        self.MyDate.setText(thetime)

    def ADD(self):
        thetime2 = str(self.calendarr2.date().toPyDate())
 
        #thetime2 = str(datetime.datetime.now())
        #thetime2 = thetime2.split(".")
        #thetime2 = str(thetime2[0])
       
        cur = self.table1.rowCount()
        try:
            idd = self.table1.item(cur-1,0).text()
            idd = int(idd)
            idd += 1
            idd = str(idd)
        except:
           

            idd = "1"
        self.table1.insertRow(cur)
        self.table1.setItem(cur,0,QTableWidgetItem(idd))
        self.table1.setItem(cur,1,QTableWidgetItem(str(self.nom.text())))
        self.table1.setItem(cur,2,QTableWidgetItem(str(self.mutualiste.currentText())))
        self.table1.setItem(cur,3,QTableWidgetItem(str(self.encaissement.currentText())))
        self.table1.setItem(cur,4,QTableWidgetItem(str(self.seance.text())))
        self.table1.setItem(cur,5,QTableWidgetItem(str(self.somme.text())))
        self.table1.setItem(cur,7,QTableWidgetItem(thetime2))
        self.table1.setItem(cur,6,QTableWidgetItem(str(self.comment.toPlainText())))
        self.date = "fdsfd"
        self.ss = self.rxN.text()
        self.ss = int(self.ss)
        self.ss += 1
        self.rxN.setText(str(self.ss))
       

        cat.InsertDatabase(self.nom.text(),self.mutualiste.currentText(),self.encaissement.currentText(),self.seance.text(),self.somme.text(),self.comment.toPlainText(),thetime2)  
    def SEARCH(self):
        global XFETCH2
        if self.search.text() == "":
            self.table2.setRowCount(0)
        else:

            XFETCH2 = cat.SearchDatabase(self.searchby.currentText(),self.search.text())
            if len(XFETCH2) >= 1:
                self.table2.setRowCount(0)
            for row_number,row_data in enumerate(XFETCH2):
                self.table2.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def EXCEL(self):
        tittre = str(datetime.datetime.now())
        tittre = tittre.replace("-","")
        tittre = tittre.replace(":","")
        tittre = tittre.replace(" ","")
        tittre = tittre.replace(".","")
        file = str(QFileDialog.getExistingDirectory(MainWindow, "Select Directory"))
   
        FETCHALL = cat.FetchDatabase()  
        try:
            with open(file +'\CSV ' + tittre + ".csv","w") as f:
                writer = csv.writer(f)
                for row in FETCHALL:
                    writer.writerow(row)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Export")
            msg.setInformativeText("Excel file exported.\nName : "+tittre)
            msg.setWindowTitle("Excel Export")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Failed to Export")
            msg.setInformativeText("Failed to export excel file")
            msg.setWindowTitle("Excel Export")
            msg.exec_()

       
    def EXCELL(self):
        tittre = str(datetime.datetime.now())
        tittre = tittre.replace("-","")
        tittre = tittre.replace(":","")
        tittre = tittre.replace(" ","")
        tittre = tittre.replace(".","")
   

        try:
            file = str(QFileDialog.getExistingDirectory(MainWindow, "Select Directory"))
       
            
            with open(file +'\CSV ' + tittre + ".csv","w") as f:
                writer = csv.writer(f)
                for row in XFETCH2:
                    writer.writerow(row)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Export")
            msg.setInformativeText("Excel file exported.\nName : "+tittre)
            msg.setWindowTitle("Excel Export")
           
       
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Failed to Export")
            msg.setInformativeText("Failed to export excel file")
            msg.setWindowTitle("Excel Export")
            msg.exec_()

    def BACKK(self):
        file = str(QFileDialog.getExistingDirectory(MainWindow, "Select Directory"))
        tittre = str(datetime.datetime.now())
        tittre = tittre.replace("-","")
        tittre = tittre.replace(":","")
        tittre = tittre.replace(" ","")
        tittre = tittre.replace(".","")
   
        copyfile("database.db",file + "\database " + tittre + ".db")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Copied")
        msg.setInformativeText("Database copied.\nName : "+tittre)
        msg.setWindowTitle("Database backup")
           
       
        msg.exec_()


        
    def delete(self):
        cur = self.table2.currentRow()
        self.table2.removeRow(cur)
        iddd = self.table2.item(cur,0)
    def close(self):
        
        MainWindow.close()
    def calc(self):
        os.system("calc.exe")

        #cat.DeleteFromDatabase(iddd)










if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = myInterface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
