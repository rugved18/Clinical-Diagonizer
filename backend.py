# backend.py
import sqlite3
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class Backend:
    
    def Login(self):
        entered_username = self.username_le.text()
        entered_password = self.password_le.text()
        print("Entered username:", entered_username)
        print("Entered password:", entered_password)

        conn = sqlite3.connect("CDDB.db", timeout=120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT username, access, password, hospital_id FROM Login_Details WHERE username=:username", {"username":  entered_username})
            data = c.fetchone()
            print("Data fetched:", data)
            try:
                username, access, password, hospital_id = data
            except TypeError:
                print("User not found or incorrect credentials.")
                QtWidgets.QMessageBox.information(self, 'Info', "Wrong credentials")
                return

            if entered_username != username or entered_password != password:
                print("Incorrect username or password.")
                QtWidgets.QMessageBox.information(self, 'Info', "Wrong credentials")
                return
            if access != "Y":
                print("Access denied.")
                QtWidgets.QMessageBox.information(self, 'Info', "Access Denied")
                return

        with conn:
            c.execute("SELECT name FROM Hospital WHERE hospital_id=:hospital_id", {'hospital_id': hospital_id})
            hosp = c.fetchone()
            self.hospital = {'name': hosp[0], 'id': hospital_id}
        conn.close()
        print("Login successful. Hospital:", self.hospital)
        QtWidgets.QMessageBox.information(self, 'Info', "Welcome \n" + self.hospital['name'])
        self.CreateMainPage()
        docs = self.fetchDocsfromHispitalId(hospital_id)
        self.DOCTOR_DISEASE_CB.addItems(docs)
        patients = self.fetchAllPatients()
        self.PATIENT_DISEASE_CB.addItems(patients)



        
    def fetchDocsfromHispitalId(self, hid):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT doctor_id, name FROM Doctor WHERE hospital_id=:hospital_id", {"hospital_id":hid})
            data = c.fetchall()
        conn.close()
        docs=[]
        for item in data:
            idname = str(item[0]) +"-"+ str(item[1])
            docs.append(idname)
        return docs
    
    def fetchAllPatients(self):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT patient_id, name FROM Patients")
            data = c.fetchall()
        conn.close()
        pats=[]
        for item in data:
            idname = str(item[0]) +"-"+ str(item[1])
            pats.append(idname)
        return pats
        
    def submitPatientDetails(self):
        name = self.NAME_PATIENT_LE.text()
        age= self.AGE_PATIENT_LE.text()
        gender= self.GENDER_PATIENT_CB.currentText()
        weight = self.WEIGHT_PATIENT_LE.text()
        keywords = self.HISTORY_PATIENT_LE.text()
        
        try: 
            conn = sqlite3.connect("CDDB.db", timeout = 120.0)
            c = conn.cursor()
            with conn:
                c.execute("SELECT MAX(patient_id) FROM Patients")
                patient_id = c.fetchone()
                patient_id = patient_id[0]
                if patient_id == None:
                    patient_id = 1
                else:
                    patient_id = patient_id+ 1
            
            with conn:
                c.execute("INSERT INTO Patients VALUES(:patient_id,:name, :age, :gender, :weight, :keywords, :date)",
                          {"patient_id":patient_id,
                           "name": name,
                           "age":age,
                           "gender":gender,
                           "weight":weight,
                           "keywords":keywords,
                           "date":str(datetime.datetime.now())
                           })
            conn.close()
            QtWidgets.QMessageBox.information(self, 'Info', "done")
        except Exception as e:
            QtWidgets.QMessageBox.information(self, 'Error', str(e))
    
    
    def addRecord(self):
        try:
            patient = self.PATIENT_DISEASE_CB.currentText()
            patient = patient.split("-")
            patient_id = int(patient[0])
            name = patient[1]
            
            doctor = self.DOCTOR_DISEASE_CB.currentText()
            doctor = doctor.split("-")
            doctor_id = doctor[0]
            
            symptoms = self.SYMPTOMS_DISEASE_TE.text()
            symptoms = symptoms.lower()
            treatment = self.TREATMENT_DISEASE_TE.text()
            drugs_used = self.DRUGSUSED_DISEASE_TE.text()
            side_effects = self.SIDEEFFECTS_DISEASE_TE.text()
            
            
            conn = sqlite3.connect("CDDB.db", timeout = 120.0)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO Record VALUES(:name, :symptoms, :patient_id, :doctor_id, :treatment,	:side_effects,	:drugs_used	, :date)", 
                          {"name": name,
                            "symptoms":symptoms,
                            "patient_id":patient_id,
                            "doctor_id":doctor_id,
                            "treatment":treatment,
                            "side_effects":side_effects,
                            "drugs_used": drugs_used,
                            "date": str(datetime.datetime.now())                       
                            })
            conn.close()
            QtWidgets.QMessageBox.information(self, 'Info', "done")
        except Exception as e:
            QtWidgets.QMessageBox.information(self, 'Error', str(e))
        
    def submitDrugDetails(self):
        try:
            name = self.NAME_DRUG_LE.text()
            composition = self.COMPOSITION_DRUG_LE.text()
            company = self.COMPANY_DRUG_LE.text()
            alternatives = self.ALTERNATIVES_DRUG_LE.text()
                    
            conn = sqlite3.connect("CDDB.db", timeout=120.0)
            c = conn.cursor()
            with conn:
              c.execute("INSERT INTO Drugs (drug_name, composition, company, alternatives, date) VALUES (:name, :contents, :manufacturer, :alternatives, :date)",
                      {"name": name,
                       "contents": composition,
                       "manufacturer": company,
                       "alternatives": alternatives,
                       "date": str(datetime.datetime.now())
                    })
            conn.close()
            QtWidgets.QMessageBox.information(self, 'Info', "done")
        except Exception as e:
            QtWidgets.QMessageBox.information(self, 'Error', str(e))


        
    def searchByKeywords(self):
     keywords = self.SEARCH_LE.text()
     keywords = keywords.split(",")

     print("Keywords:", keywords)  # Add a print statement to check the keywords
    
    # Check if any keywords are entered
     if not keywords:
        QtWidgets.QMessageBox.information(self, 'Info', "Please enter keywords for search.")
        return

    # Initialize the WHERE clause of the SQL query
     where_clause = []

    # Construct the WHERE clause for each keyword
     for keyword in keywords:
        # Add conditions for each keyword
        where_clause.append(f"Record.symptoms LIKE '%{keyword}%'")

    # Join all WHERE clause conditions using AND
     where_clause_str = " AND ".join(where_clause)

     print("WHERE clause:", where_clause_str)  # Add a print statement to check the WHERE clause
    
    # Construct the complete SQL query
     query = f"""
        SELECT Patients.name, Patients.age, Patients.gender, Patients.weight, Patients.keywords,
               Doctor.name, Hospital.name, Record.symptoms, Record.treatment, Record.side_effects, Record.drugs_used
        FROM Record
        JOIN Patients ON Patients.patient_id = Record.patient_id
        JOIN Doctor ON Record.doctor_id = Doctor.doctor_id
        JOIN Hospital ON Doctor.hospital_id = Hospital.hospital_id
        WHERE {where_clause_str}
    """

     print("Query:", query)  # Add a print statement to check the constructed SQL query
    
    # Execute the query and update the table with the results
     conn = sqlite3.connect("CDDB.db", timeout=120.0)
     c = conn.cursor()
     with conn:
        c.execute(query)
        data = c.fetchall()

     print("Search Results:", data)  # Add a print statement to check the retrieved data
    
     conn.close()

    # Update the table with the fetched data
     self.updateSearchResults(data)

    def updateSearchResults(self, data):
        self.SEARCH_TABLE.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.SEARCH_TABLE.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col_data)))
