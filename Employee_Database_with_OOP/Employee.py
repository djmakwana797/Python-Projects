import sqlite3
from Verification import Verification as V
from DbConnection import Record 

class Employee:
    _employeeFirstName=""
    _employeeLastName=""
    _employeeMobileNo=""
    _employeeDepart=""
    _employeeJoinYear=""
    _employeeEmail=""
 
    def __init__(self):
        verify = V()
        self._employeeFirstName = input("Enter your first name: ")
        self._employeeLastName = input("Enter your last name: ")
        self._employeeDepart = input("Enter your department: ")
        self._employeeJoinYear = V.verifyJY(verify) 
        self._employeeMobileNo = V.verifyMobile(verify)
        self._employeeEmail = V.verifyEmail(verify)

    def addEmp(self):
        R = Record()
        R.add_data(self._employeeFirstName,self._employeeLastName,self._employeeDepart,self._employeeJoinYear,self._employeeMobileNo,self._employeeEmail)

    def updateEmp(self,ofname):
        R = Record()
        R.update_data_by_fname(self._employeeFirstName,self._employeeLastName,self._employeeDepart,self._employeeJoinYear,self._employeeMobileNo,self._employeeEmail,ofname)

i = 1
while(i):
    print("\n0.Exit\n1.Add Employee.\n2.Display details of all the Employees.\n3.Display Employee by first name.\n4.Update Employee by first name.\n5.Delete Employee by first name.")
    try:
        i = int(input("Enter your choice : "))
    except:
        print("Please enter correct choice") #when user enters non integer value
        continue

    if(i==1):
        E = Employee()
        E.addEmp()
        
    elif(i==2):
        R = Record();
        R.display_all();

    elif(i==3):
        f = input("Enter first name: ")
        R = Record();
        R.display_by_fname(f)

    elif(i==4):
        Old_Name = input("Enter old first name :")
        E = Employee()
        E.updateEmp(Old_Name)

    elif(i==5):
        f = input("Enter first name: ")
        R = Record()
        R.delete_data_by_fname(f)

    elif(i==0):
        exit
        
    else:
        print("Please enter correct choice")
