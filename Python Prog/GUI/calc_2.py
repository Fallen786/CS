from tkinter import *

root = Tk()
e = Entry(root,width=40,borderwidth=10)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def click(n):
    x = e.get()
    e.delete(0,END)
    e.insert(0,str(x) + str(n))

def add():
    first_num = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_num)
    e.delete(0,END)

def sub():
    first_num = e.get()
    global f_num
    global operation
    operation = "substraction"
    f_num = float(first_num)
    e.delete(0,END)

def mul():
    first_num = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_num)
    e.delete(0,END)

def div():
    first_num = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_num)
    e.delete(0,END)

def rem():
    first_num = e.get()
    global f_num
    global operation
    operation = "reminder"
    f_num = float(first_num)
    e.delete(0,END)

def clear():
    e.delete(0,END)


def equal():
    second_num = e.get()
    s_num = float(second_num)
    e.delete(0,END)
    if operation == "addition":
        e.insert(0,f_num + s_num)
    elif operation == "substraction":
        e.insert(0,f_num - s_num)
    elif operation == "multiplication":
        e.insert(0,f_num * s_num)
    elif operation == "division":
        e.insert(0,f_num / s_num)
    elif  operation == "reminder":
        e.insert(0,f_num % s_num)

button_7 = Button(root,text="7",padx=25,pady=10,command=lambda: click(7))
button_8 = Button(root,text="8",padx=25,pady=10,command=lambda: click(8))
button_9 = Button(root,text="9",padx=25,pady=10,command=lambda: click(9))
button_4 = Button(root,text="4",padx=25,pady=10,command=lambda: click(4))
button_5 = Button(root,text="5",padx=25,pady=10,command=lambda: click(5))
button_6 = Button(root,text="6",padx=25,pady=10,command=lambda: click(6))
button_1 = Button(root,text="1",padx=25,pady=10,command=lambda: click(1))
button_2 = Button(root,text="2",padx=25,pady=10,command=lambda: click(2))
button_3 = Button(root,text="3",padx=25,pady=10,command=lambda: click(3))
button_0 = Button(root,text="0",padx=25,pady=10,command=lambda: click(0))
button_add = Button(root,text="+",padx=25,pady=10,command=add)
button_sub = Button(root,text="-",padx=25,pady=10,command=sub)
button_mul = Button(root,text="*",padx=25,pady=10,command=mul)
button_div = Button(root,text="/",padx=25,pady=10,command=div)
button_rem = Button(root,text="%",padx=25,pady=10,command=rem)
button_clear = Button(root,text="C",padx=25,pady=10,command=clear)
button_equal= Button(root,text="=",padx=72,pady=10,command=equal)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=1)
button_add.grid(row=4,column=0)
button_sub.grid(row=4,column=2)
button_mul.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_rem.grid(row=5,column=2)
button_clear.grid(row=6,column=2)
button_equal.grid(row=6,column=0,columnspan=2)

root.mainloop()