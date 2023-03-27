import pygame
pygame.init()

class Item:
    def __init__(self, name="player 1", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1
    
    # Accessors and mutators for all variables with the constraints for each
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(value) < 2:
            self._name = f"player 1"
        elif (len(value) >= 2):
            self._name = value

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
    
    
    ############## Change X or Y value ##################
    def goRight(self):
        self.x += 1

    def goLeft(self):
        self.x -= 1

    def goUp(self):
        self.y -= 1

    def goDown(self):
        self.y += 1


    ##################### Output the person's data ######################
    def __str__(self):
        return f"Person({self.name}):\tsize:{self.size},\tx = {self.x}\ty = {self.y}"