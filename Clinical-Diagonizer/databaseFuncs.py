# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:33:24 2023

@author: amogha
"""

import sqlite3
#import db2XL

class ClinicalDiagonizerDB:
    
    
    def create_login_details(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Login_Details (username text primary key not null, 
                    access varchar(10), 
                    password text, 
                    hospital_id integer UNIQUE,
                    date text,
                    FOREIGN KEY(hospital_id) REFERENCES Hospital(hospital_id))""")
        conn.close()
        
    def create_hospital_table(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Hospital (hospital_id integer PRIMARY KEY NOT NULL UNIQUE,
                    name text,
                    address text,
                    phone integer,
                    type text,
                    extra_details text,
                    date text)""")
        conn.close()
    
    def create_doctor_table(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Doctor (doctor_id integer PRIMARY KEY NOT NULL UNIQUE,
                    hospital_id integer,
                    name text, 
                    qualification text, 
                    date text,
                    FOREIGN KEY(hospital_id) REFERENCES Hospital(hospital_id))""")
        conn.close()
    
    def create_patient_table(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Patients (patient_id integer PRIMARY KEY NOT NULL UNIQUE,
                    name text,
                    age integer,
                    gender varchar(10),
                    weight float,
                    keywords text,
                    date text)""")
        conn.close()
    
    
    def create_record_table(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Record (name text,
                     symptoms text,
                     patient_id integer,
                     doctor_id integer,
                     treatment text,
                     side_effects text,
                     drugs_used text,
                     date text,
                     FOREIGN KEY(doctor_id) REFERENCES Doctor(doctor_id),
                     FOREIGN KEY(patient_id) REFERENCES Patients(patient_id))""")
        conn.close()
    
    def create_drugs_table(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()    
        c.execute("""CREATE TABLE Drugs (drugs_id integer PRIMARY KEY NOT NULL UNIQUE,
                     name text,
                     contents text,
                     manufacturer text,
                     alternatives text,
                    date text)""")
        conn.close()
        
    def __init__(self):
        #run to create tables
        self.create_login_details()
        self.create_hospital_table()
        self.create_doctor_table()
        self.create_patient_table()
        self.create_drugs_table()
        self.create_record_table()
        
        
        #Uncomment for xlsx of db
        #db2XL.db2xl(dbfile = r'CDDB.db')
        


if __name__ == "__main__": 
    ClinicalDiagonizerDB()