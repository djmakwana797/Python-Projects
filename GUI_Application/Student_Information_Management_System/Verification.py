import re

class Verify:

    def verifyEmail(self,email):
        pattern = re.compile(r'\w+[^_][.]{0,1}\w+@[^0-9]\w+\.{0,1}\w+\.{0,1}\w+') 
        if pattern.match(email):           
            return False
        # print("<< Invalid email >>")
        else:
            return True

    def verifyMobile(self):
        pattern = re.compile(r'([+]\d{2}[ ])?\d{10}') 
        mobile = input("Enter your mobile number: ")
        if pattern.match(mobile):           
            return False        
        # print("<< Invalid Mobile number >>")
        else:
            return True

   