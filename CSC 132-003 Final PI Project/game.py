import pygame
pygame.init()

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
    
class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        #self.image.fill((255,0,0))
        

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))   