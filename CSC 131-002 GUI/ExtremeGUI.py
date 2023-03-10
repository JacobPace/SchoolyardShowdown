from tkinter import *
from random import randint
WIDTH = 200
HEIGHT = 75
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"



# MAIN #
window = Tk()
def generatePassword():
    e1.delete(0, 100)
    password = ""
    for i in range(8):
        password += CHARACTERS[randint(0, len(CHARACTERS)-1)]
    return password

l1 = Label(window, text="Generate random password")
l1.grid(row=0, column=0, columnspan=3, sticky=W+E)

e1 = Entry(window)
e1.grid(row=1, column=0, columnspan=3, sticky=W+E)

b1 = Button(window, text="Generate", command=lambda: e1.insert(END, generatePassword()))
b1.grid(row=2, column=1)


window.title("Password Generator")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.mainloop()


