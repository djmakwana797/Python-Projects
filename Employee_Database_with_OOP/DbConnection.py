import sqlite3

class Record:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('edata.db')
        except:
            print("Something went wrong")
        self.cur = self.conn.cursor()

        try:
            self.cur.execute('''CREATE TABLE Employee(
                        id integer primary key autoincrement,
                        fname text,
                        lname text,
                        department text,
                        joiningYear integer,
                        mobile integer,
                        email text)
            ''')
        except:
            pass

    def add_data(self,fname,lname,dep,jy,mobile,email):
        with self.conn:
            result = self.cur.execute("INSERT INTO Employee(fname,lname,department,joiningYear,mobile,email) VALUES (?,?,?,?,?,?)",(fname,lname,dep,jy,mobile,email))
            print("\nEmployee added.")
    
    def update_data_by_fname(self,fname,lname,dep,jy,mobile,email,oldfname):
        with self.conn:
            result = self.cur.execute("UPDATE Employee SET fname = ?, lname = ?, department = ?, joiningYear = ?, mobile = ? ,email = ? WHERE fname = ?",(fname,lname,dep,jy,mobile,email,oldfname))            
            print("\nUpdated Employee successfully.")

    def delete_data_by_fname(self,f):
        with self.conn:
            self.cur.execute("DELETE from Employee WHERE fname = ?",(f,))
            print("\nRemoved Employee successfully.")
            

    def display_by_fname(self,f):
        with self.conn:
            self.cur.execute("SELECT * from Employee WHERE fname = ?",(f,))
            result = self.cur.fetchone()
            print("\nName: "+result[1]+" "+result[2]+"\nDepartment: "+result[3]+"\nJoining Year: "+str(result[4])+"\nMobile number: "+str(result[5])+"\nEmail: "+result[6])

    def display_all(self):
        with self.conn:
            results = self.cur.execute("SELECT *  from Employee")
            if(results.fetchall()==[]):
                print("\nNo Records found.")
            else:
                for result in results:
                    print("\nName: "+result[1]+" "+result[2]+"\nDepartment: "+result[3]+"\nJoining Year: "+str(result[4])+"\nMobile number: "+str(result[5])+"\nEmail: "+result[6])
