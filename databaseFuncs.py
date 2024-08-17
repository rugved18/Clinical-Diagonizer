# databaseFuncs.py
import sqlite3

class ClinicalDiagonizerDB:
    
    def create_login_details(self):
        conn = sqlite3.connect("CDDB.db", timeout=120.0)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Login_Details';")
        if c.fetchone() is None:
            c.execute("""CREATE TABLE Login_Details (
                        username TEXT PRIMARY KEY NOT NULL, 
                        access TEXT NOT NULL, 
                        password TEXT NOT NULL, 
                        hospital_id INTEGER NOT NULL, 
                        date TEXT NOT NULL,
                        FOREIGN KEY(hospital_id) REFERENCES Hospital(hospital_id)
                    );""")
            conn.commit()
        else:
            print("Login_Details table already exists.")
        conn.close()

    def check_connection(self):
        try:
            conn = sqlite3.connect("CDDB.db", timeout=120.0)
            c = conn.cursor()
            c.execute("SELECT * FROM Login_Details LIMIT 1")
            conn.close()
            print("Database connection successful.")
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def __init__(self):
        self.create_login_details()
        # Call other table creation functions here
        self.check_connection()

if __name__ == "__main__": 
    ClinicalDiagonizerDB()
