from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=30,borderwidth=10)
e.grid(row=0,column=0,padx=20,pady=20,columnspan=3)

def click(n):
    x = e.get()
    e.delete(0, END)
    e.insert(0,str(x) + str(n))

def clear():
    e.delete(0, END)

def add():
    first_num = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_num)
    e.delete(0,END)

def sub():
    first_num = e.get()
    global f_num
    global operation
    operation = "substraction"
    f_num = int(first_num)
    e.delete(0,END)

def equal():
    second_num = e.get()
    s_num = int(second_num)
    e.delete(0,END)
    if operation == "addition":
        e.insert(0,f_num + s_num)
    elif operation == "substraction":
        e.insert(0,f_num - s_num)

button_7 = Button(root,text="7",padx=20,pady=10,command=lambda: click(7))
button_8 = Button(root,text="8",padx=20,pady=10,command=lambda: click(8))
button_9 = Button(root,text="9",padx=20,pady=10,command=lambda: click(9))
button_4 = Button(root,text="4",padx=20,pady=10,command=lambda: click(4))
button_5 = Button(root,text="5",padx=20,pady=10,command=lambda: click(5))
button_6 = Button(root,text="6",padx=20,pady=10,command=lambda: click(6))
button_1 = Button(root,text="1",padx=20,pady=10,command=lambda: click(1))
button_2 = Button(root,text="2",padx=20,pady=10,command=lambda: click(2))
button_3 = Button(root,text="3",padx=20,pady=10,command=lambda: click(3))
button_clear = Button(root,text="Clear",padx=50,pady=10,command=clear)
button_add = Button(root,text="+",padx=20,pady=10,command=add)
button_equal = Button(root,text="=",padx=60,pady=10,command=equal)
button_sub = Button(root,text="-",padx=20,pady=10,command=sub)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_clear.grid(row=4,column=0,columnspan=2)
button_add.grid(row=4,column=2)
button_equal.grid(row=5,column=0,columnspan=2)
button_sub.grid(row=5,column=2)


root.mainloop()