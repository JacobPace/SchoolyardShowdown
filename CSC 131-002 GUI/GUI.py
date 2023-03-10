from tkinter import *

class App(Frame):
    def __init__(self, main):
        Frame.__init__(self, main)

        # button1
        self.button1 = Button(main, text="BYE!", fg="red", command=self.quit)
        self.button1.pack(side=LEFT)

        # button2
        self.button2 = Button(main, text="CLICK ME!", command=self.say)
        self.button2.pack(side=LEFT)

    # .say command for button2
    def say(self):
        print("HI")

# MAIN
window = Tk() # instance
app = App(window)
window.mainloop()