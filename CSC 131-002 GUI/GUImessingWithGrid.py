from tkinter import *

window = Tk()

l1 = Label(window, text="A", bg="red", fg="white")
l1.grid(column=0, row=0, columnspan=3)

l2 = Label(window, text="B", bg="green", fg="white")
l2.grid(column=1, row=1)

l3 = Label(window, text="C", bg="blue", fg="white")
l3.grid(column=2, row=2)

# textbox
e1 = Entry(window)
e1.grid(column=3,row=3)

def printText():
    print(e1.get())
    l1.config(text=e1.get())
b1 = Button(window, text="Submit", command=printText)
b1.grid(column=4,row=3)

window.mainloop()