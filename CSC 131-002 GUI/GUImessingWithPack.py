from tkinter import *

window = Tk()

l1 = Label(window, text="A", bg="red", fg="white")
l1.pack(side=LEFT, expand=1, fill=X)

l2 = Label(window, text="B", bg="green", fg="white")
l2.pack(side=LEFT, expand=1, fill=X)

l3 = Label(window, text="C", bg="blue", fg="white")
l3.pack(side=LEFT, expand=1, fill=X)

window.mainloop()