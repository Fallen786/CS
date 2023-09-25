import tkinter as tk

def move_rectangle():
    canvas.move(rect, 100, 0)  # Move the rectangle 5 pixels to the right
    canvas.after(50, move_rectangle)  # Schedule the function to run again in 50 milliseconds

root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

rect = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

move_rectangle()  # Start the animation loop

root.mainloop()
