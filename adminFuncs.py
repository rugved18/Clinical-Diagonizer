# adminFuncs.py
import sqlite3
import datetime

class adminFuncs:
    
    def createHospital(name, address="", phone="", Type="", extra_details=""):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT MAX(hospital_id) FROM Hospital")
            hospital_id = c.fetchone()
            hospital_id = hospital_id[0]
            if hospital_id == None:
                hospital_id = 1
            else:
                hospital_id = hospital_id+ 1
        
        with conn:
            c.execute("INSERT INTO Hospital VALUES(:hospital_id,:name, :address, :phone, :type, :extra_details, :date)",
                      {"hospital_id":hospital_id,
                       "name": name,
                       "address":address,
                       "phone":phone,
                       "type":Type,
                       "extra_details":extra_details,
                       "date":str(datetime.datetime.now())
                       })
            
        conn.close()
        
    def createLogin(username, access, password, hospital_id):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO Login_Details VALUES(:username, :access,:password, :hospital_id, :date)",
                      {"username":username,
                       "access":access,
                       "password":password,
                       "hospital_id":hospital_id,
                       "date": str(datetime.datetime.now())
                       })
        conn.close()
    
    def createDoctor(hospital_id, name, qualification):
        conn = sqlite3.connect("CDDB.db", timeout = 120.0)
        c = conn.cursor()
        with conn:
            c.execute("SELECT MAX(doctor_id) FROM DOCTOR")
            doctor_id = c.fetchone()
            doctor_id = doctor_id[0]
            if doctor_id == None:
                doctor_id = 1
            else:
                doctor_id = doctor_id+ 1
                
        with conn:
            c.execute("INSERT INTO Doctor VALUES(:doctor_id, :hospital_id,:name, :qualification, :date)",
                      {"doctor_id":doctor_id,
                       "hospital_id":hospital_id,
                       "name":name,
                       "qualification":qualification,
                       "date":str(datetime.datetime.now())
                       })
        conn.close()

 # adminFuncs.createHospital(name="NIMHANS", address="Dharmaram College Post, Off Hosur Road, Bengaluru", phone=r"26995000 / 26568121 / 26995001",Type="govt", extra_details="Neurocenter")
# adminFuncs.createLogin(username="NIH", access="Y", password="nih", hospital_id=1)
# adminFuncs.createDoctor(hospital_id=1, name="Prajwal", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=1, name="Prapul", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=1, name="Karan", qualification="MBBS")

# adminFuncs.createHospital(name="Raja Rajeswari Medical College & Hospital", address="No.202, Kambipura, Mysore Road", phone=r"2843 7888/ 2929 2929")
# adminFuncs.createLogin(username="RRMC", access="Y", password="rrmc", hospital_id=2)
# adminFuncs.createDoctor(hospital_id=2, name="Anurag", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=2, name="Ajay", qualification="MBBS,")
# adminFuncs.createDoctor(hospital_id=2, name="Bhaskar", qualification="MBBS,MD")

# adminFuncs.createHospital(name="Bowring & Lady Curzon Hospital", address="Near Shivajinagar bus stand Cantonment area, Bangalore", phone=r"25591325 / 25591362",Type="govt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="BLCH", access="Y", password="blch", hospital_id=3)
# adminFuncs.createDoctor(hospital_id=3, name="Mohit", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=3, name="Aditya", qualification="MBBS,")
# adminFuncs.createDoctor(hospital_id=3, name="Bharath", qualification="MBBS,MD")

# adminFuncs.createHospital(name="E.S.I Hospital, Basavangudi", address="Med. Supdt. ESI Hospital North Anjaneya Temple Street, Basavanagudi BANGALORE-560004", phone=r"6673554",Type="pvt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="ESI", access="Y", password="esi", hospital_id=4)
# adminFuncs.createDoctor(hospital_id=4, name="Ashwini", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=4, name="Gopal", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=4, name="Bharadwaj", qualification="MBBS,MD")

# adminFuncs.createHospital(name="E.S.I Hospital, Indiranagar", address="Med. Supdt ESI Hospital HAL II Stage Indiranagar BANGALORE", phone=r"2526993 / 25266994",Type="pvt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="ESII", access="Y", password="esii", hospital_id=5)
# adminFuncs.createDoctor(hospital_id=5, name="Akash", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=5, name="Govind", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=5, name="Arjun", qualification="MBBS,MD")

# adminFuncs.createHospital(name="General Hospital, Jayanagar", address="4th T Block, Opposite Sagar Hotel", phone=r"26345711 / 26530633",Type="govt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="GHJ", access="Y", password="ghj", hospital_id=6)
# adminFuncs.createDoctor(hospital_id=6, name="Dhanush", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=6, name="Harshith", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=6, name="Bhuvan", qualification="MBBS,MD")

# adminFuncs.createHospital(name="Indira Gandhi Institute of Child Health Hospital", address="Complex, Near Nimhans Dharmaram College , Bengaluru – 560029", phone=r"26342421 / 26343143",Type="govt", extra_details="Children Hospital")
# adminFuncs.createLogin(username="IGI", access="Y", password="igi", hospital_id=7)
# adminFuncs.createDoctor(hospital_id=7, name="Jayanth", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=7, name="Lohith", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=7, name="Lavanya", qualification="MBBS,MD")

# adminFuncs.createHospital(name="Jayadeva Institute of Cardiology", address="Jayanagar, 9th Block Bannerghatta Road, Bengaluru -560069", phone=r"26534600",Type="pvt", extra_details="Cardiocenter")
# adminFuncs.createLogin(username="JIC", access="Y", password="jic", hospital_id=8)
# adminFuncs.createDoctor(hospital_id=8, name="Thanmay", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=8, name="Omkar", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=8, name="Uma", qualification="MBBS,MD")

# adminFuncs.createHospital(name="K C General Hospital", address="#89, 5th Cross, Near Malleswaram Police Station,Malleswaram, Bangalore", phone=r"23343791 / 23341771",Type="pvt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="KCG", access="Y", password="kcg", hospital_id=9)
# adminFuncs.createDoctor(hospital_id=9, name="Vishal", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=9, name="Dhanshree", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=9, name="Vidhur", qualification="MBBS,MD")

# adminFuncs.createHospital(name="Vanivilas Hospital", address="Krishna Rajendra Market, Near Victory Hospital, Kalasipalayam, Bengaluru", phone=r"26705206 / 26707174 / 26709145",Type="govt", extra_details="Genral Hospital")
# adminFuncs.createLogin(username="VVH", access="Y", password="vvh", hospital_id=10)
# adminFuncs.createDoctor(hospital_id=10, name="Neethu", qualification="MBBS,MD")
# adminFuncs.createDoctor(hospital_id=10, name="Kumar", qualification="MBBS")
# adminFuncs.createDoctor(hospital_id=10, name="Shanthi", qualification="MBBS,MD")       
