from tkinter import *
from random import randint

# CONSTANTS
WIDTH = 400
HEIGHT = 400
POINT_COLORS = ["black", "red", "green", "blue"]
POINT_RADIUS = 0
NUM_POINT = 2000

class Points(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plot(self, x, y):
        color = POINT_COLORS[randint(0, len(POINT_COLORS)-1)] # Outline color
        color2 = POINT_COLORS[randint(0, len(POINT_COLORS)-1)] # Fill color
        self.create_oval(x, y, x+POINT_RADIUS*2, y+POINT_RADIUS*2, outline=color, fill=color2)

    def plotPoints(self, n):
        # The x
        for i in range(WIDTH):
            self.plot(i, i)
            self.plot(WIDTH-i-1, i)
        # The random points
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)


############### MAIN ####################
window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Check out these points!")
p = Points(window)
p.plotPoints(NUM_POINT)
window.mainloop()