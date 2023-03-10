################################################
# Name: Jacob Pace
# Date: 2/8/2023
# Description: The Reckoner
################################################

from tkinter import *

####### MAY HAVE TO CHANGE THIS FOR IT TO WORK FOR GRADING
####### THIS IS HOW WINDOWS IS
folder = "images\\"
ButtonDisplays = [
    ["lpr", "rpr", "clr", "bak"],
    ["7", "8", "9", "div"],
    ["4", "5", "6", "mul"],
    ["1", "2", "3", "sub"],
    ["0", "dot", "", "add"],
    ["eql-wide", "pow", "mod"]
]

buttonDef = {
    "lpr" : "(",
    "rpr" : ")",
    "clr" : "clr",
    "pow" : "**",
    "mul" : "*",
    "div" : "/",
    "sub" : "-",
    "dot" : ".",
    "eql-wide" : "=",
    "add" : "+",
    "mod" : "%",
}

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()

    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", height=2, font=("TextGyreAdventor", 45))
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        # creating buttons
        for row in range(len(ButtonDisplays)):
            for column in range(len(ButtonDisplays[row])):
                if (ButtonDisplays[row][column] != "" and ButtonDisplays[row][column] != "eql-wide" and ButtonDisplays[row][column] != "pow" and ButtonDisplays[row][column] !="mod"):
                    img = PhotoImage(file=folder+ButtonDisplays[row][column]+".gif")
                    button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda button=ButtonDisplays[row][column]: self.process(button))
                    button.image = img
                    button.grid(row=row+1, column=column, stick=N+S+E+W)
                elif (ButtonDisplays[row][column] == "eql-wide"):
                    img = PhotoImage(file=folder+ButtonDisplays[row][column]+".gif")
                    button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda button=ButtonDisplays[row][column]: self.process(button))
                    button.image = img
                    button.grid(row=row+1, column=0, columnspan=2, stick=N+S+E+W)
                elif (ButtonDisplays[row][column] == "pow"):
                    img = PhotoImage(file=folder+ButtonDisplays[row][column]+".gif")
                    button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda button=ButtonDisplays[row][column]: self.process(button))
                    button.image = img
                    button.grid(row=row+1, column=2, stick=N+S+E+W)
                elif (ButtonDisplays[row][column] == "mod"):
                    img = PhotoImage(file=folder+ButtonDisplays[row][column]+".gif")
                    button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda button=ButtonDisplays[row][column]: self.process(button))
                    button.image = img
                    button.grid(row=row+1, column=3, stick=N+S+E+W)

        self.pack(fill=BOTH, expand=1)

    def process(self, button):
        if (button in buttonDef):
            button = buttonDef[button]
        if (button == "clr"):
            self.display["text"] = ""
        elif (button == "bak"):
            self.display["text"] = self.display["text"][:-1]
        elif (button == "="):
            try:
                result = eval(self.display["text"])
                if (len(str(result)) > 14):
                    result = str(result)
                    result = str(result[0:11]+"...")
                    self.display["text"] = result
                elif (len(str(result)) < 14):
                    self.display["text"] = result
            except:
                self.display["text"] = "ERROR"
        elif (len(self.display["text"]) < 14):
                self.display["text"] += button

### MAIN ###

# create window
window = Tk()

# set window title
window.title("The Reckoner")

# generate the GUI
calc = MainGUI(window)

# display interface
window.mainloop()