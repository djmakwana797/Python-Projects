import re
 
e = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
m = re.compile(r'\d{10}')
 
i = 1
salary = "60000"
while(i):
    print("1. Add Emp\n2. Display Emp")
    i = int(input("Enter your Choice:"))
    if(i==1):
        name = input("Enter name: ")
        email = input("Enter email: ")
        if(e.findall(email)):
            pass
        else:
            print("Invalid Email.")
            break
        mobile = input("Enter mobile no: ")
        if(m.findall(mobile)):
            pass
        else:
            print("Invalid Mobile number.")
            break
        type = input("Enter Employee type: ")
        exp = input("Enter experience: ")
 
        f = open("Employee.txt", "a")
        f.write("Name: "+name + "\nEmail: " + email + "\nEmp Type: " + type + "\nMobile no.: " + mobile + "\nExperience: " + exp + "\nSalary: " + salary +"\n\n")
        f.close()
    elif(i==2):
        name = input("Enter emp name: ")
        f = open("Employee.txt",'r')
        data = f.read()
        position = data.find(name)
        start = position - 6
        end = data.find("6000",start)
 
        print("==================================")
        print(data[start:end+5])
        print("==================================")
