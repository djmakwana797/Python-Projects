import sqlite3

class Record:
    def __init__(self):
        
        try:
            self.conn = sqlite3.connect('sdata.db')
        except:
            print("Something went wrong")
        self.cur = self.conn.cursor()

        try:
            self.cur.execute('''CREATE TABLE Student(
                        id integer primary key autoincrement,
                        fname text,
                        lname text,
                        sem integer,
                        branch text,
                        division text,
                        email text)
            ''')
        except:
            pass

    def add_data(self,fname,lname,sem,branch,div,email):
        with self.conn:
            result = self.cur.execute("INSERT INTO Student(fname,lname,sem,branch,division,email) VALUES (?,?,?,?,?,?)",(fname,lname,sem,branch,div,email))

    def display_all(self):
        with self.conn:
            results = self.cur.execute("SELECT *  from Student")
            return results.fetchall()