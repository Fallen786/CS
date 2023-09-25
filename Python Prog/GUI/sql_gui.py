import mysql.connector as mc
from tkinter import *
mydb = mc.connect(host="localhost",user="root",password="bruh",database="eSports")
cur = mydb.cursor()
mydb.autocommit = True

root = Tk()
e = Entry(root)
e.pack()
def call():
    label = Label(root,text = e.get())
    label.pack()

button = Button(root,text="bruh",command=call)
button.pack()
root.mainloop()