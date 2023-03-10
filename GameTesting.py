import pygame
print(pygame.__version__)
pygame.init()

white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

x = 1000
y = 1000

display_surface = pygame.display.set_mode((x,y), pygame.RESIZABLE)

pygame.display.set_caption("Testing")

font = pygame.font.Font("freesansbold.ttf", 32)

text = font.render('Test', True, black, white)

textRect = text.get_rect()

textRect.center = (500,500)

while True:
    display_surface.fill(white)
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()