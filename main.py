import tkinter as tk
import mysql.connector
from dbfile.db import *

root=tk.Tk()
root.title("Mark Entry")
root.geometry("700x670+200+20")

db=mysqldb()


def  displayrecord():
    record=db.selectrecord()
    for records in record:
        print(records)

def passvalue():
    value1=lblety1.get()
    value2=lblety2.get()
    value3=lblety3.get()
    value4=lblety4.get()
    value5=lblety5.get()
    value6=lblety6.get()
    value7=lblety7.get()
    value8=lblety8.get()

    db.insertrecord(value1,value2,value3,value4,value5,value6,value7,value8)
    displayrecord()
def passdeleterecord():
    value1=lblety1.get()
    db.deleterecord(value1)
    displayrecord()

lbl0=tk.Label(root,text="Student Mark",font=("Helvetica",16))
lbl0.grid(row=0,columnspan=2,padx=10,pady=10)

lbl1=tk.Label(root,text="Name:")
lbl1.grid(row=1,column=0,padx=10,pady=30)

lblety1=tk.Entry(root)
lblety1.grid(row=1,column=1,padx=10,pady=30)

lbl2=tk.Label(root,text="Department:")
lbl2.grid(row=1,column=2,padx=10,pady=30)

lblety2=tk.Entry(root)
lblety2.grid(row=1,column=3,padx=10,pady=30)

lbl3=tk.Label(root,text="Shift:")
lbl3.grid(row=1,column=4,padx=10,pady=30)

lblety3=tk.Entry(root)
lblety3.grid(row=1,column=5,padx=10,pady=30)

lbl4=tk.Label(root,text="mark1:")
lbl4.grid(row=2,column=1,padx=10,pady=30)

lblety4=tk.Entry(root)
lblety4.grid(row=2,column=2,padx=10,pady=30)

lbl5=tk.Label(root,text="mark2:")
lbl5.grid(row=3,column=1,padx=10,pady=30)

lblety5=tk.Entry(root)
lblety5.grid(row=3,column=2,padx=10,pady=30)

lbl6=tk.Label(root,text="mark3:")
lbl6.grid(row=4,column=1,padx=10,pady=30)

lblety6=tk.Entry(root)
lblety6.grid(row=4,column=2,padx=10,pady=30)

lbl7=tk.Label(root,text="mark4:")
lbl7.grid(row=5,column=1,padx=10,pady=30)

lblety7=tk.Entry(root)
lblety7.grid(row=5,column=2,padx=10,pady=30)

lbl8=tk.Label(root,text="mark4:")
lbl8.grid(row=6,column=1,padx=10,pady=30)

lblety8=tk.Entry(root)
lblety8.grid(row=6,column=2,padx=10,pady=30)

btn1=tk.Button(root,text="Submit", command=passvalue)
btn1.grid(row=7,column=4,padx=10,pady=30)

btn2=tk.Button(root,text="Delete",command=passdeleterecord)
btn2.grid(row=7,column=3,padx=10,pady=30)

root.mainloop()