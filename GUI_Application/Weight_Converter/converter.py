

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Weight Converter")

def unit_converter():
    try :
        to_grams=float(store_entry.get())*1000
        to_pounds = float(store_entry.get()) * 2.20462
        to_milligrams = float(store_entry.get())* 1000000
        text_1.delete(0.1,END)
        text_1.insert(END,to_grams)
        text_2.delete(0.1,END)
        text_2.insert(END,  to_pounds)
        text_3.delete(0.1,END)
        text_3.insert(END, to_milligrams)
    except :
        messagebox.showerror("Invalid Input","Please Enter valid weight")

button = Button(text="Convert",activebackground="green",activeforeground="white",command=unit_converter)
button.grid(row=0, column=2)

label_0 = Label(text="Kilograms :")
label_0.grid(row=0,column=0)

store_entry=StringVar()
entry = Entry(window,textvariable=store_entry,width=17,selectbackground="black")
entry.grid(row=0,column=1)

label_1 = Label(window,text="Grams :")
label_1.grid(row=1,column=0)

text_1 = Text(window,height=1, width=13)
text_1.grid(row=1,column=1)

label_2 = Label(window,text="Pounds :")
label_2.grid(row=2,column=0)

text_2 = Text(window,height=1, width=13)
text_2.grid(row=2,column=1)

label_3 = Label(window,text="Milligrams :")
label_3.grid(row=3,column=0)

text_3 = Text(window,height=1, width=13)
text_3.grid(row=3,column=1)

window.mainloop()
