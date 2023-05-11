import pygame
pygame.init()
from random import randint
#need a change to commit nahudjkawbksjBDkjsAJKDASJ
# This is where we will put all of the reuseable code so that there is no
# need to keep copy pasting -e.g. making buttons for the screen

# Button class should need no further editing
class Button:
    def __init__(self, x, y, image, imgHover, scale, selected):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.imgHover = pygame.transform.scale(imgHover, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.selected = selected
        self.cooldown = False

    def draw(self, surface):
        if self.selected:
            surface.blit(self.imgHover, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def changeButton(self, other):
        self.selected = True
        other.selected = False

    def action(self):
        return True

class Image:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))    

class Player:
    def __init__(self, x, y):
        self.health = 7
        self.x = x
        self.y = y
        #self.width = 32
        #self.height = 32
        self.bandAids = 5
        #self.image = pygame.transform.scale(image, (self.width, self.height))
        #self.rect = self.image.get_rect()
        #self.rect.center = [self.x, self.y]
        
        #self.move_right = False
        #self.move_left = False
        #self.move_up = False
        #self.move_down = False

    #def draw(self, surface):
        #surface.blit(self.image, (self.x, self.y))   

class Enemy():
    def __init__(self, name):
        self.name = name
        #self.battleSprite = pygame.transform.scale(battleSprite, (32, 32))
        self.health = 3
        self.type = "grunt"

    def draw(self, surface):
        surface.blit(self.battleSprite, (750, 200))

    def action(self):
        choice = randint(1, 10)
        if choice > 1:
            actionChoice = randint(1,9)
            if actionChoice == 1 or actionChoice == 2 or actionChoice == 3:
                return "Rock"
            if actionChoice == 4 or actionChoice ==5 or actionChoice ==6:
                return "Paper"
            if actionChoice == 7 or actionChoice == 8 or actionChoice ==9:
                return "Scissors"
            print(actionChoice)
        if choice == 1:
            return "Block"

class RockGrunt(Enemy):
    def __init__(self, name):
        Enemy.__init__(self, name)
        self.type = "Rock"


    def action(self):
        choice = randint(1, 10)
        if choice > 1:
            actionChoice = randint(1,12)
            if actionChoice > 6:
                return "Rock"
            if (actionChoice >= 4) and (actionChoice <= 6):
                return "Paper"
            if (actionChoice >= 1) and (actionChoice < 4):
                return "Scissors"
            print(actionChoice)
        if choice == 1:
            return "Block"

class PaperGrunt(Enemy):
    def __init__(self, name):
        Enemy.__init__(self, name)
        self.type = "Paper"

    def action(self):
        choice = randint(1, 10)
        if choice > 1:
            actionChoice = randint(1,12)
            if actionChoice > 6:
                return "Paper"
            if (actionChoice >= 4) and (actionChoice <= 6):
                return "Rock"
            if (actionChoice >= 1) and (actionChoice < 4):
                return "Scissors"
            print(actionChoice)
        if choice == 1:
            return "Block"

class ScissorsGrunt(Enemy):
    def __init__(self, name):
        Enemy.__init__(self, name)
        self.type = "Scissors"

    def action(self):
        choice = randint(1, 10)
        if choice > 1:
            actionChoice = randint(1,12)
            if actionChoice > 6:
                return "Scissors"
            if (actionChoice >= 4) and (actionChoice <= 6):
                return "Paper"
            if (actionChoice >= 1) and (actionChoice < 4):
                return "Rock"
            print(actionChoice)
        if choice == 1:
            return "Block"


class Boss(Enemy):
    def __init__(self, name):
        Enemy.__init__(self, name="Joel")
        self.health = 5
        self.type = "boss"