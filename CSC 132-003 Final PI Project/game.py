import pygame
pygame.init()
from random import randint

# This is where we will put all of the reuseable code so that there is no
# need to keep copy pasting -e.g. making buttons for the screen

# Button class should need no further editing
class Button:
    def __init__(self, name, x, y, image, imgHover, scale, selected):
        self.name = name
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
    
    def __str__(self):
        return f"{self.name}\t Selected: {self.selected}"

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
    def __init__(self, x, y, image):
        self.health = 10
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False



    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))   

class NPC:
    def ___init__(self, name=""):
        self.name = name

class Enemy(NPC):
    def __init__(self, battleSprite):
        NPC.__init__(self)
        self.battleSprite = pygame.transform.scale(battleSprite, (32, 32))
        self.health = 10
        self.inventory = []
        self.attacks = ["Rock", "Paper", "Scissors"]
        self.actions = [self.attacks, "Block", "Bag"]
        


    def draw(self, surface):
        surface.blit(self.battleSprite, (750, 200))

    def action(self):
        choice = randint(1, 10)
        if choice > 1:
            actionChoice = randint(1,9)
            if actionChoice in range(1, 3):
                print("Testing\tRock")
                return "Rock"
            if actionChoice in range(4, 6):
                print("Testing\tPaper")
                return "Paper"
            if actionChoice in range(7, 9):
                print("Testing\tScissors")
                return "Scissors"
        if choice == 1:
            print("Testing\tBlock")
            return "Block"

class RockGrunt(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = "Rock"

class PaperGrunt(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = "Paper"

class ScissorsGrunt(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = "Scissors"

class Boss(Enemy):
    def __init__(self):
        Enemy.__init__(self, name="Joel")
        self.health = 15
