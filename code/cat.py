import sqlite3



def CreateBase():
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """CREATE TABLE IF NOT EXISTS PATIENTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME VARCHAR, MUTUALISTE VARCHAR,ENCAISSEMENT VARCHAR,SEANCE VARCHAR,SOMME VARCHAR,COMMENT VARCHAR,DATE VARCHAR)"""
    try:
        cu.execute(qu)              
        co.commit()
    except Exception as K:
        raise K
        co.rollback()
    finally:
        co.close()

def InsertDatabase(nom,mutualiste,encaissement,seance,somme,comment,date):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """ INSERT INTO PATIENTS VALUES(NULL,"{}","{}","{}","{}","{}","{}","{}")""".format(nom,mutualiste,encaissement,seance,somme,comment,date)
    try:
        cu.execute(qu)
        co.commit()
    except:
        co.rollback()
    finally:
        co.close()

def FetchDatabase():
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT * FROM PATIENTS"""
    try:
        cu.execute(qu)
        
        co.commit()
        ko = cu.fetchall()
    except Exception as k:
        raise k
        co.rollback()
    finally:
        co.close()
    return ko


def SelectById(Id):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT ID,Date,Name,Seance,Mutualiste,Encaissement,Somme,Comment FROM PATIENTS WHERE ID = '{}' """.format(Id)
    try:
        cu.execute(qu)
        
        co.commit()
        roo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return roo

def selectPatientHistory(patient_name):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT ID,Date,Somme,Encaissement,Seance,Comment FROM PATIENTS WHERE NAME = '{}' """.format(patient_name)
    try:
        cu.execute(qu)
        
        co.commit()
        roo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return roo


def SelectTotalDatabaseKenza(DATE111,DATE222):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE ENCAISSEMENT = 'Kenza' AND DATE BETWEEN '{}' AND '{}-1 day'""".format(DATE111,DATE222)
    try:
        cu.execute(qu)
        
        co.commit() 
        jiii = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return jiii

def SelectEqualDatabaseIbtissam(DATE11,DATE22):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE ENCAISSEMENT = '50/50' AND DATE BETWEEN '{}' AND '{}-1 day'""".format(DATE11,DATE22)
    try:
        cu.execute(qu)
        
        co.commit() 
        jii = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return jii

def SelectTotalDatabaseIbtissam(DATE11,DATE22):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE ENCAISSEMENT = 'Cabinet' AND DATE BETWEEN '{}' AND '{}-1 day'""".format(DATE11,DATE22)
    try:
        cu.execute(qu)
        
        co.commit() 
        jii = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return jii

def SELECTSELECTSELECT(pat_n):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE ENCAISSEMENT = 'Kenza' AND NAME = '{}'""".format(pat_n)
    try:
        cu.execute(qu)
        
        co.commit() 
        jiiii = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return jiiii

def SELECTSELECTIBTISSAM(patiet_namee):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE ENCAISSEMENT = 'Cabinet' AND NAME = '{}'""".format(patiet_namee)
    try:
        cu.execute(qu)
        
        co.commit() 
        jiii = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return jiii
def SelectTotalDatabase(DATE1,DATE2):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE DATE BETWEEN '{}' AND '{}-1 day'""".format(DATE1,DATE2)
    try:
        cu.execute(qu)
        
        co.commit() 
        ji = cu.fetchall()
        
    except:
        
        co.rollback()
    finally:
        co.close()
    return ji

def DeleteFromDatabase(chay):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """DELETE FROM PATIENTS WHERE ID = '{}' """.format(chay)
    try:
        cu.execute(qu)
        
        co.commit()
        
    except:
        
        co.rollback()
    finally:
        co.close()
   

def UpdateDatabase(ssname,ssmutualiste,ssencaissement,ssseance,sssomme,sscomment,ssId):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """UPDATE PATIENTS SET NAME = '{}',MUTUALISTE = '{}',ENCAISSEMENT='{}',SEANCE = '{}',SOMME = '{}',COMMENT = '{}' WHERE ID = '{}'""".format(ssname,ssmutualiste,ssencaissement,ssseance,sssomme,sscomment,ssId)
    try:
        cu.execute(qu)
        
        co.commit()
        roo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return roo



def SelectTotalPatient(patient_name):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT SUM(SOMME) FROM PATIENTS WHERE NAME = '{}' """.format(patient_name)
    try:
        cu.execute(qu)
        
        co.commit()
        poo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return poo

def SelectTotalPatient2(patient_name):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT MAX(SEANCE) FROM PATIENTS WHERE NAME = '{}' """.format(patient_name)
    try:
        cu.execute(qu)
        
        co.commit()
        yoo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return yoo

def SelectTotalPatient3(patient_name):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT AVG(SOMME) FROM PATIENTS WHERE NAME = '{}' """.format(patient_name)
    try:
        cu.execute(qu)
        
        co.commit()
        loo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return loo


def SearchByDate(date1,date2):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT * FROM PATIENTS WHERE DATE BETWEEN '{}' AND  '{}-1 day' """.format(date1,date2)
    try:
        cu.execute(qu)
        
        co.commit()
        joo = cu.fetchall()

    except:
        
        co.rollback()
    finally:
        co.close()
    return joo

def SelectByDate(date3):
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT * FROM PATIENTS WHERE DATE BETWEEN '{}' AND '{}+1 day' """.format(date3,date3)
    try:
        cu.execute(qu)
        
        co.commit()
        moo = cu.fetchall()

    except Exception as k:
        raise k
        co.rollback()
    finally:
        co.close()
    return moo

def SearchDatabase(searchby,search):
    

    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT * FROM PATIENTS WHERE [{}] LIKE '%{}%'""".format(searchby,search)
    try:
        cu.execute(qu)
        
        co.commit()
        koo = cu.fetchall()

    except:
     
        co.rollback()
    finally:
        co.close()
    return koo

def SearchId():
    co = sqlite3.connect("database.db")
    cu = co.cursor()
    qu = """SELECT Count(ID) FROM PATIENTS"""
    try:
        cu.execute(qu)
        
        co.commit()
        koc = cu.fetchall()
    except Exception as k:
        raise k
        co.rollback()
    finally:
        co.close()
    return koc

