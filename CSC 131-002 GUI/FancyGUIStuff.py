from tkinter import *

class GUITest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        l1 = Label(self.master, text="A label")
        l1.grid(row=0, column=0, sticky=W)

        l2 = Label(self.master, text="Another label")
        l2.grid(row=1, column=0, sticky=W)

        l3 = Label(self.master, text="A third label, centered")
        l3.grid(row=2, column=0, columnspan=2, sticky=NE+W) # Centering via sticky

        img = PhotoImage(file="C:/Users/Jacob Pace/Documents/PythonCode/smile.gif")
        l4 = Label(self.master, image=img)
        l4.image = img
        l4.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=N+S+E+W)

        e1 = Entry(self.master)
        e1.grid(row=0, column=1)

        e2 = Entry(self.master)
        e2.insert(END, "user input")
        e2.grid(row=1, column=1)

        c1 = Checkbutton(self.master, text="Some CheckButton option")
        c1.grid(row=3, column=0, columnspan=2, sticky=W)

        b1 = Button(self.master, text="A button")
        b1.grid(column=2, row=3)

        b2 = Button(self.master, text="Another button")
        b2.grid(column=3, row=3)
window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()
