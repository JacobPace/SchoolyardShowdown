#####################################################################
# author:   Jacob Pace
# date:    3/26/2023
# description: Person Class Reloaded
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self,x=0,y=0)
        self.width = 10
        self.height = 10
        self.surf = pygame.Surface([self.width, self.height])
        self.rect = self.surf.get_rect()
        
        self.rect.topleft = [self.x, self.y]
        self.color = (255, 0, 0)
        self.surf.fill(self.color)

    def update(self, pressedKeys):
        if pressedKeys[K_UP] and self.y >0:
            self.goUp()
        if pressedKeys[K_DOWN] and self.y < HEIGHT-self.height:
            self.goDown()
        if pressedKeys[K_RIGHT] and self.x < WIDTH-self.width:
            self.goRight()
        if pressedKeys[K_LEFT] and self.x>0:
            self.goLeft()
        if pressedKeys[K_SPACE]:
            self.setSize()
        self.rect.topleft = [self.x, self.y]

    def setSize(self):
        modifier = randint(10, 100)
        self.width = modifier
        self.height = modifier
        self.surf = pygame.Surface([self.width, self.height])
        self.setColor()

    def setColor(self):
        self.color = COLORS[randint(0,4)]
        self.surf.fill(self.color)


    def setRandomPosition(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
        self.rect.topleft = [self.x, self.y]

    def getPosition(self):
        return self.rect.topleft
    
    def __str__(self):
        return f"{super().__str__()}\t Color: {self.color}"



########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

