class Doctor:
    def __init__(self, id, name, specilization, availability):
        self.ID = id
        self.name = name
        self.specilization = specilization
        self.availability = availability

    def __str__(self):
        return f"Doctor's ID: {self.ID}, Name: {self.name}, Specilization: {self.specilization}, Available at: {self.availability}"
    
    @classmethod
    def searchDoctor(cls, docName):
        found = False
        with open("DoctorData.txt") as sfile:
            for line in sfile:
                data = line.strip().split(",")
            
                docID = int(data[0].strip())
                doctorName = data[1].strip()
                docSpec = data[2].strip()
                docAvail = data[3].strip()
            
                if doctorName == docName:
                    doctor = cls(docID, doctorName, docSpec, docAvail)
                    print(doctor)
                    found = True
                    break
        if not found:
            print("Doctor name not found!")
    
class Patient:
    def __init__(self, id, name, mobile, age):
        self.ID = id
        self.name = name
        self.mobile = mobile
        self. age = age
    
    def __str__(self):
        return f"Patient's ID: {self.ID}, Name: {self.name}, Mobile number: {self.mobile}, Age: {self.age}"
    
    @classmethod
    def patientSearch(cls, patientName):
        found = False
        with open("PatientData.txt") as rpfile:
            for line in rpfile:
                pdata = line.strip().split(",")

                pid = int(pdata[0].strip())
                pname = pdata[1].strip()
                pnumber = pdata[2].strip()
                page = int(pdata[3].strip())

                if pname == patientName:
                    patient = cls(pid, pname, pnumber, page)
                    print(patient)
                    found = True
                    break
        if not found:
            print("Patient record not found!")
    
option = int(input("Enter the below details:\n1. Doctor\n2. Patient\n"))
match(option):
    case 1:
        choice = int(input("1. Enter new doctor details\n2. Search for a doctor\n"))
        if choice == 1:
            docNum = int(input("How many doctor's data would like to store: "))
            for i in range(docNum):
                docName = input(f"{i+1} doctor's name: ")
                docID = int(input(f"{i+1} doctor's ID: "))
                docSpec = input(f"{i+1} specilization of the doctor: ")
                docAvail = input(f"{i+1} doctor's availability: ")

                doctor = Doctor(docID, docName, docSpec, docAvail)
                print(doctor)

                with open("DoctorData.txt","a") as wfile:
                    wfile.write(f"{docID}, {docName}, {docSpec}, {docAvail}\n")
        else:
            docSearchName = input("Enter the doctor's name you would like to search for: ")
            Doctor.searchDoctor(docSearchName)
    case 2:
        choice = int(input("1. Enter new patient details \n2. Search for a patient\n"))
        if choice == 1:
            patnum = int(input("Enter how many patient records would you like to store: "))
            for i in range(patnum):
                patID = int(input(f"{i+1} patient's ID: "))
                patName = input(f"{i+1} patient's name: ")
                patMobile = input(f"{i+1} patient's mobile number: ")
                patAge = int(input(f"{i+1} patient's age: "))

                patient = Patient(patID, patName, patMobile, patAge)
                print(patient)

                with open("PatientData.txt", "a") as wpfile:
                    wpfile.write(f"{patID}, {patName}, {patMobile}, {patAge}\n")
        else:
            pname = input("Enter the name you want to search for: ")
            Patient.patientSearch(pname)