# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\desi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1073, 998)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 941))
        self.tabWidget.setStyleSheet(_fromUtf8("\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Insert = QtGui.QWidget()
        self.Insert.setObjectName(_fromUtf8("Insert"))
        self.table1 = QtGui.QTableWidget(self.Insert)
        self.table1.setGeometry(QtCore.QRect(130, 330, 821, 451))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.table1.setPalette(palette)
        self.table1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.table1.setStyleSheet(_fromUtf8("\n"
"background:rgba(32, 221, 225, 179);\n"
"alternate-background-color:rgba(0, 0, 0, 147);\n"
"font:bold;\n"
""))
        self.table1.setFrameShadow(QtGui.QFrame.Sunken)
        self.table1.setLineWidth(1)
        self.table1.setMidLineWidth(0)
        self.table1.setAlternatingRowColors(True)
        self.table1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table1.setRowCount(0)
        self.table1.setObjectName(_fromUtf8("table1"))
        self.table1.setColumnCount(8)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(7, item)
        self.table1.horizontalHeader().setCascadingSectionResizes(False)
        self.table1.horizontalHeader().setSortIndicatorShown(False)
        self.table1.horizontalHeader().setStretchLastSection(False)
        self.table1.verticalHeader().setVisible(False)
        self.groupBox_3 = QtGui.QGroupBox(self.Insert)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 40, 301, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox_3.setPalette(palette)
        self.groupBox_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"color:white;"))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(11, 41, 41, 16))
        self.label_9.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(11, 70, 51, 16))
        self.label_10.setStyleSheet(_fromUtf8("color: white;\n"
"font: 90 bold 8pt \"MS Shell Dlg 2\";\n"
"background:transparent;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(11, 101, 51, 16))
        self.label_11.setStyleSheet(_fromUtf8("color: white;\n"
"font: 90 bold 8pt \"MS Shell Dlg 2\";\n"
"background:transparent;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.nom = QtGui.QLineEdit(self.groupBox_3)
        self.nom.setGeometry(QtCore.QRect(70, 40, 188, 22))
        self.nom.setStyleSheet(_fromUtf8("background-color:white;\n"
"color:black;\n"
"font:bold;"))
        self.nom.setObjectName(_fromUtf8("nom"))
        self.plus = QtGui.QPushButton(self.groupBox_3)
        self.plus.setText("+")
        self.plus.setStyleSheet(_fromUtf8("background-color:green;\n"
"color:black;\n"
"font:bold;"))
        self.plus.setGeometry(QtCore.QRect(260, 40, 20, 22))
        self.mutualiste = QtGui.QComboBox(self.groupBox_3)
        self.mutualiste.setGeometry(QtCore.QRect(70, 70, 211, 22))
        self.mutualiste.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;\n"
"font:bold;"))
        self.mutualiste.setObjectName(_fromUtf8("mutualiste"))
        self.mutualiste.addItem(_fromUtf8(""))
        self.mutualiste.addItem(_fromUtf8(""))
        self.seance = QtGui.QLineEdit(self.groupBox_3)
        self.seance.setGeometry(QtCore.QRect(70, 100, 211, 22))
        self.seance.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;"))
        self.seance.setObjectName(_fromUtf8("seance"))
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(11, 131, 51, 16))
        self.label_22.setStyleSheet(_fromUtf8("color: white;\n"
"font: 90 bold 8pt \"MS Shell Dlg 2\";\n"
"background:transparent;"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_7897 = QtGui.QLabel(self.groupBox_3)
        self.label_7897.setGeometry(QtCore.QRect(11, 190, 51, 16))
        self.label_7897.setStyleSheet(_fromUtf8("color: white;\n"
"font: 90 bold 8pt \"MS Shell Dlg 2\";\n"
"background:transparent;"))
        self.label_7897.setText("Date")
        self.somme = QtGui.QLineEdit(self.groupBox_3)
        self.somme.setGeometry(QtCore.QRect(70, 130, 211, 22))
        self.somme.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;"))
        self.somme.setObjectName(_fromUtf8("somme"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(11, 160, 91, 16))
        self.label_23.setStyleSheet(_fromUtf8("color: white;\n"
"font: 90 bold 8pt \"MS Shell Dlg 2\";\n"
"background:transparent;"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.encaissement = QtGui.QComboBox(self.groupBox_3)
        self.encaissement.setGeometry(QtCore.QRect(110, 160, 171, 22))

        self.encaissement.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;\n"
"font:bold;"))
        self.encaissement.setObjectName(_fromUtf8("encaissement"))
        self.encaissement.addItem(_fromUtf8(""))
        self.encaissement.addItem(_fromUtf8(""))
        self.calendarr2 = QtGui.QDateEdit(self.groupBox_3)
        self.calendarr2.setGeometry(QtCore.QRect(55,190,228,22))
        self.calendarr2.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;\n"
"font:bold;"))

        self.groupBox_4 = QtGui.QGroupBox(self.Insert)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 40, 341, 211))
        self.groupBox_4.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"color:white;font:bold;"))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 311, 71))
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(104, 104, 104);\n"
"font: 75 italic 9pt \\\"8514oem\\\";\n"
"background:transparent;\n"
"color:white;\n"
"font: 75 italic 11pt  \"Unispace\";"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.BACKUP = QtGui.QPushButton(self.groupBox_4)
        self.BACKUP.setGeometry(QtCore.QRect(40, 230, 321, 28))
        self.BACKUP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BACKUP.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BACKUP.setObjectName(_fromUtf8("BACKUP"))
        self.add = QtGui.QPushButton(self.groupBox_4)
        self.add.setGeometry(QtCore.QRect(10, 160, 321, 28))
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.add.setObjectName(_fromUtf8("add"))
        self.groupBox_5 = QtGui.QGroupBox(self.Insert)
        self.groupBox_5.setGeometry(QtCore.QRect(710, 40, 341, 211))
        self.groupBox_5.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"color:white;font:bold;"))
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.BACKUP_2 = QtGui.QPushButton(self.groupBox_5)
        self.BACKUP_2.setGeometry(QtCore.QRect(40, 230, 321, 28))
        self.BACKUP_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BACKUP_2.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BACKUP_2.setObjectName(_fromUtf8("BACKUP_2"))
        self.comment = QtGui.QTextEdit(self.groupBox_5)
        self.comment.setGeometry(QtCore.QRect(20, 20, 311, 171))
        self.comment.setStyleSheet(_fromUtf8("background:white;\n"
"color:red;"))
        self.comment.setObjectName(_fromUtf8("comment"))
        self.MyDate = QtGui.QLabel(self.Insert)
        self.MyDate.setGeometry(QtCore.QRect(880, 10, 171, 16))
        self.MyDate.setStyleSheet(_fromUtf8("color:rgb(163, 8, 29);\n"
"background:transparent;\n"
"font:bold;\n"
"color:white;"))
        self.MyDate.setObjectName(_fromUtf8("MyDate"))
        self.rxN = QtGui.QLineEdit(self.Insert)
        self.rxN.setGeometry(QtCore.QRect(480, 295, 134, 22))
        self.rxN.setStyleSheet(_fromUtf8("background:rgba(32, 221, 225, 179);\n"
"color:black;\n"
"font:bold;\n"
"\n"
""))
        self.rxN.setText(_fromUtf8(""))
        self.rxN.setObjectName(_fromUtf8("rxN"))
        self.label_15 = QtGui.QLabel(self.Insert)
        self.label_15.setGeometry(QtCore.QRect(440, 300, 36, 16))
        self.label_15.setStyleSheet(_fromUtf8("font:bold;\n"
"background:transparent;\n"
"color:black;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.BPatient_2 = QtGui.QPushButton(self.Insert)
        self.BPatient_2.setGeometry(QtCore.QRect(130, 820, 411, 28))
        self.BPatient_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BPatient_2.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BPatient_2.setObjectName(_fromUtf8("BPatient_2"))
        self.BCalculator_3 = QtGui.QPushButton(self.Insert)
        self.BCalculator_3.setGeometry(QtCore.QRect(130, 790, 411, 28))
        self.BCalculator_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BCalculator_3.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BCalculator_3.setObjectName(_fromUtf8("BCalculator_3"))
        self.BClose = QtGui.QPushButton(self.Insert)
        self.BClose.setGeometry(QtCore.QRect(560, 790, 391, 28))
        self.BClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BClose.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BClose.setObjectName(_fromUtf8("BClose"))
        self.BClose_2 = QtGui.QPushButton(self.Insert)
        self.BClose_2.setGeometry(QtCore.QRect(560, 820, 391, 28))
        self.BClose_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BClose_2.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BClose_2.setObjectName(_fromUtf8("BClose_2"))
        self.BACKUP_3 = QtGui.QPushButton(self.Insert)
        self.BACKUP_3.setGeometry(QtCore.QRect(130, 850, 821, 28))
        self.BACKUP_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BACKUP_3.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.BACKUP_3.setObjectName(_fromUtf8("BACKUP_3"))
        self.tabWidget.addTab(self.Insert, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.table2 = QtGui.QTableWidget(self.tab_2)
        self.table2.setGeometry(QtCore.QRect(130, 390, 801, 461))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 221, 225, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.table2.setPalette(palette)
        self.table2.setStyleSheet(_fromUtf8("background:rgba(32, 221, 225, 179);\n"
"alternate-background-color:rgba(0, 0, 0, 147);\n"
"font:bold;"))
        #self.table2.setAlternatingRowColors(True)
        self.table2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table2.setShowGrid(True)
        self.table2.setGridStyle(QtCore.Qt.SolidLine)
        self.table2.setWordWrap(True)
        self.table2.setCornerButtonEnabled(True)
        self.table2.setRowCount(0)
        self.table2.setObjectName(_fromUtf8("table2"))
        self.table2.setColumnCount(8)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(7, item)
        self.table2.horizontalHeader().setCascadingSectionResizes(False)
        self.table2.verticalHeader().setVisible(False)
        self.table2.verticalHeader().setCascadingSectionResizes(False)
        self.table2.verticalHeader().setDefaultSectionSize(30)
        self.table2.verticalHeader().setHighlightSections(True)
        self.groupBox_12 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 20, 1031, 71))
        self.groupBox_12.setTitle(_fromUtf8(""))
        self.groupBox_12.setFlat(False)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.label_29 = QtGui.QLabel(self.groupBox_12)
        self.label_29.setGeometry(QtCore.QRect(16, 27, 53, 16))
        self.label_29.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.search = QtGui.QLineEdit(self.groupBox_12)
        self.search.setGeometry(QtCore.QRect(70, 23, 191, 22))
        self.search.setStyleSheet(_fromUtf8("background-color:white;\n"
"font:bold;\n"
"color:black;\n"
""))
        self.search.setObjectName(_fromUtf8("search"))
        self.EditDrugs_2 = QtGui.QPushButton(self.groupBox_12)
        self.EditDrugs_2.setGeometry(QtCore.QRect(420, 20, 93, 28))
        self.EditDrugs_2.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.EditDrugs_2.setObjectName(_fromUtf8("EditDrugs_2"))
        self.RefreshDrugs_2 = QtGui.QPushButton(self.groupBox_12)
        self.RefreshDrugs_2.setGeometry(QtCore.QRect(620, 20, 93, 28))
        self.RefreshDrugs_2.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.RefreshDrugs_2.setObjectName(_fromUtf8("RefreshDrugs_2"))
        self.DeleteDrugs_2 = QtGui.QPushButton(self.groupBox_12)
        self.DeleteDrugs_2.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.DeleteDrugs_2.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.DeleteDrugs_2.setObjectName(_fromUtf8("DeleteDrugs_2"))
        self.searchby = QtGui.QComboBox(self.groupBox_12)
        self.searchby.setGeometry(QtCore.QRect(270, 20, 142, 28))
        self.searchby.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(0, 240, 240);\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.searchby.setObjectName(_fromUtf8("searchby"))
       
        self.excel = QtGui.QPushButton(self.groupBox_12)
        self.excel.setGeometry(QtCore.QRect(862, 20, 151, 28))
        self.excel.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"font: 75 bold 8pt  \"Unispace\";"))
        self.excel.setObjectName(_fromUtf8("excel"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 110, 511, 271))
        self.groupBox_10.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:white;\n"
"font:bold;"))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.SHDate1 = QtGui.QDateEdit(self.groupBox_10)
        self.SHDate1.setGeometry(QtCore.QRect(10, 24, 110, 22))
        self.SHDate1.setStyleSheet(_fromUtf8("background-color:white;\n"

"color:black"))
        self.SHDate1.setObjectName(_fromUtf8("SHDate1"))

        self.SHDate2 = QtGui.QDateEdit(self.groupBox_10)
        self.SHDate2.setGeometry(QtCore.QRect(160, 24, 110, 22))
        self.SHDate2.setStyleSheet(_fromUtf8("background-color:white;\n"
"color:black;"))
        self.SHDate2.setObjectName(_fromUtf8("SHDate2"))
        self.label_26 = QtGui.QLabel(self.groupBox_10)
        self.label_26.setGeometry(QtCore.QRect(130, 26, 21, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))

        self.SHLABEL = QtGui.QLabel(self.groupBox_10)
        self.SHLABEL.setGeometry(QtCore.QRect(10, 90, 300, 18))
        self.SHLABEL.setText("Total : ")

        self.SHLABEL2 = QtGui.QLabel(self.groupBox_10)
        self.SHLABEL2.setGeometry(QtCore.QRect(10, 130, 300, 18))
        self.SHLABEL2.setText("Kenza : ")

        self.SHLABEL3 = QtGui.QLabel(self.groupBox_10)
        self.SHLABEL3.setGeometry(QtCore.QRect(10, 170, 300, 18))
        self.SHLABEL3.setText("Ibtissam : ")
       

        self.SHRefresh = QtGui.QPushButton(self.groupBox_10)
        self.SHRefresh.setGeometry(QtCore.QRect(280, 20, 93, 28))
        self.SHRefresh.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;\n"
""))
        self.SHRefresh.setObjectName(_fromUtf8("SHRefresh"))
        self.SHClose = QtGui.QPushButton(self.groupBox_10)
        self.SHClose.setGeometry(QtCore.QRect(380, 20, 93, 28))
        self.SHClose.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;\n"
""))
        self.SHClose.setObjectName(_fromUtf8("SHClose"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_11.setGeometry(QtCore.QRect(540, 110, 511, 271))
        self.groupBox_11.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:white;\n"
"font:bold;"))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.calendarWidget = QtGui.QCalendarWidget(self.groupBox_11)
        self.calendarWidget.setGeometry(QtCore.QRect(60, 30, 371, 221))
        self.calendarWidget.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;"))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBackup_database = QtGui.QAction(MainWindow)
        self.actionBackup_database.setObjectName(_fromUtf8("actionBackup_database"))
        self.actionClear_database = QtGui.QAction(MainWindow)
        self.actionClear_database.setObjectName(_fromUtf8("actionClear_database"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFichier.addAction(self.actionBackup_database)
        self.menuFichier.addAction(self.actionClear_database)
        self.menuFichier.addAction(self.actionClose)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom", None))
        item = self.table1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mutualiste", None))
        item = self.table1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Encaissement", None))
        item = self.table1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Seance", None))
        item = self.table1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Somme", None))
        item = self.table1.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Commentaire", None))
        item = self.table1.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Patient", None))
        self.label_9.setText(_translate("MainWindow", "Name", None))
        self.label_10.setText(_translate("MainWindow", "Mutuel", None))
        self.label_11.setText(_translate("MainWindow", "Seance", None))
        self.mutualiste.setItemText(0, _translate("MainWindow", "Oui", None))
        self.mutualiste.setItemText(1, _translate("MainWindow", "Non", None))
        self.label_22.setText(_translate("MainWindow", "Somme", None))
        self.label_23.setText(_translate("MainWindow", "Encaissement", None))
        self.encaissement.setItemText(0, _translate("MainWindow", "Kenza", None))
        self.encaissement.setItemText(1, _translate("MainWindow", "Cabinet", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "The Automated software", None))
        self.label_14.setText(_translate("MainWindow", "The Automated Kinesetherapy", None))
        self.BACKUP.setText(_translate("MainWindow", "DATABASE BACKUP", None))
        self.add.setText(_translate("MainWindow", "Add Patient", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Ajouter un commentaire", None))
        self.BACKUP_2.setText(_translate("MainWindow", "DATABASE BACKUP", None))
        self.MyDate.setText(_translate("MainWindow", "Tue Jun  5 02:57:12 2018", None))
        self.label_15.setText(_translate("MainWindow", "Rx No", None))
        self.BPatient_2.setText(_translate("MainWindow", "F4-Patient", None))
        self.BCalculator_3.setText(_translate("MainWindow", "Calculator", None))
        self.BClose.setText(_translate("MainWindow", "Close", None))
        self.BClose_2.setText(_translate("MainWindow", "Export to excel =>", None))
        self.BACKUP_3.setText(_translate("MainWindow", "DATABASE BACKUP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Insert), _translate("MainWindow", "Insert", None))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom", None))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mutualiste", None))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Encaissement", None))
        item = self.table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Seance", None))
        item = self.table2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Somme", None))
        item = self.table2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Commentaire", None))
        item = self.table2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date", None))
        self.label_29.setText(_translate("MainWindow", "Search", None))
        self.EditDrugs_2.setText(_translate("MainWindow", "VIEW/EDIT", None))
        self.RefreshDrugs_2.setText(_translate("MainWindow", "REFRESH", None))
        self.DeleteDrugs_2.setText(_translate("MainWindow", "DELETE", None))
        
        self.excel.setText(_translate("MainWindow", "Export to excel", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Search between 2 dates ", None))
        self.label_26.setText(_translate("MainWindow", "To", None))
        self.SHRefresh.setText(_translate("MainWindow", "Refresh", None))
        self.SHClose.setText(_translate("MainWindow", "Close", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Search by single day", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionBackup_database.setText(_translate("MainWindow", "Backup database", None))
        self.actionClear_database.setText(_translate("MainWindow", "Clear database", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

