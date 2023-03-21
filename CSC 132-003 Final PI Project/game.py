import pygame
pygame.init()
class Button:
    def __init__(self, x, y, image, imgHover, scale, default):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.imgHover = pygame.transform.scale(imgHover, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.selected = False
        self.cooldown = False
        self.default = default

    def draw(self, surface):
        if self.selected or self.default:
            surface.blit(self.imgHover, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

    def action(self):
        return True