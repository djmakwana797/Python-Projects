import re

class Verification:

    def verifyEmail(self):
        pattern = re.compile(r'\w+[^_][.]{0,1}\w+@[^0-9]\w+\.{0,1}\w+\.{0,1}\w+') 
        while 1:
            email = input("Enter your email: ")
            if pattern.match(email):           
                return email
            print("<< Invalid email >>")

    def verifyMobile(self):
        pattern = re.compile(r'([+]\d{2}[ ])?\d{10}') 
        while 1:
            mobile = input("Enter your mobile number: ")
            if pattern.match(mobile):           
                return int(mobile)
            print("<< Invalid Mobile number >>")

    def verifyJY(self):
        pattern = re.compile(r'[0-9]+')
        while 1:
            jy = input("Enter year of joining: ")
            if pattern.match(jy):
                return int(jy)
            print("<<Invalid Year>>")
