from tkinter import *
from tkinter import messagebox
from DbConnection import Record
from Verification import Verify 

root = Tk()
root.title("Student's Information System")
root.geometry("600x600")

def submit():
    V = Verify()
    R = Record()
    if f_name.get()== "":
        messagebox.showinfo("Required field","Please enter First Name.")
    if l_name.get() == "":
        messagebox.showinfo("Required field","Please enter Last Name.")
    if sem.get() == "":
        messagebox.showinfo("Required field","Please enter Semester")
    if branch.get() == "":
        messagebox.showinfo("Required field","Please enter Branch.")
    if division.get() == "":
        messagebox.showinfo("Required field","Please enter Division.")
    if email.get() == "":
        messagebox.showinfo("Required field","Please enter Email.")
    if V.verifyEmail(email.get()) == 1:
        messagebox.showwarning("Warning","Please enter valid Email.")
    else:
        R.add_data(f_name.get(),l_name.get(),sem.get(),branch.get(),division.get(),email.get())
        f_name.delete(0,END)
        l_name.delete(0,END)
        sem.delete(0,END)
        branch.delete(0,END)
        division.delete(0,END)
        email.delete(0,END)

def record():
    R = Record()
    data = R.display_all()
    if data == []:
        messagebox.showinfo("","No records found")
    else:
        print_record = ""
        for record in data:
            print_record += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + str(record[4]) + str(record[5]) + " " + str(record[6]) + "\n"
            l = Label(root, text=print_record)
            l.grid(row=8,column=0, columnspan=3)
    
#Create input fields
f_name = Entry(root, width=50)
f_name.grid(row=0, column=1, pady=5, ipadx=80)
l_name = Entry(root, width=50)
l_name.grid(row=1, column=1, pady=5, ipadx=80)
sem = Entry(root, width=50)
sem.grid(row=2, column=1, pady=5, ipadx=80)
branch = Entry(root, width=50)
branch.grid(row=3, column=1, pady=5, ipadx=80)
division = Entry(root, width=50)
division.grid(row=4, column=1, pady=5, ipadx=80)
email = Entry(root, width=50)
email.grid(row=5, column=1, pady=5, ipadx=80)

#Create labels
fn = Label(root, text="First Name")
fn.grid(row=0,column=0,padx=10)
ln = Label(root, text="Last Name")
ln.grid(row=1,column=0,padx=10)
sm = Label(root, text="Semester")
sm.grid(row=2,column=0,padx=10)
br = Label(root, text="Branch")
br.grid(row=3,column=0,padx=10)
dv = Label(root, text="Division")
dv.grid(row=4,column=0,padx=10)
em = Label(root, text="Email Address")
em.grid(row=5,column=0,padx=10)


#Submit Button
btn = Button(root, text="Add data to the database",padx=80,command=submit)
btn.grid(row=6, column=0, columnspan=2, padx=50)

q_btn = Button(root, text="Display data",padx=80,command=record)
q_btn.grid(row=7, column=0, columnspan=2, padx=140, pady=20)

root.mainloop()