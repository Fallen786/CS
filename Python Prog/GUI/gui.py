from tkinter import *
root = Tk()

e = Entry(root)
e.pack()

def click():
    label1 = Label(root, text = e.get())
    label1.pack()

button = Button(root,text="Enter name",command=click)
button.pack()
root.mainloop()