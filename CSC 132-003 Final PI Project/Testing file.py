# Testing file
import sys
from time import sleep
import pygame
pygame.init()

#WIDTH = 500
#HEIGHT = 500
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#clock = pygame.time.Clock() # FPS controller

# set color(s) with the RGB code for html
#white = (255, 255, 255)
#black = (0, 0, 0)
#screen.fill(white)

# gives the window a name
#pygame.display.set_caption("Test window")


#temp_font = pygame.font.SysFont("Arial", 25)
#def draw_text(text, font, text_color,x, y):
#    img = font.render(text, True, text_color)
#    screen.blit(img, (x, y)) 
# draw_text("What you want the text to be", your font variable, color of the text, x coordinate, y coordinate)

#words = "Testing"
#text = "New text"

#def SlowText(text):
#    result = []
#    for char in text:
#        sleep(0.5)
#        result.append(char)
#        yield result

#def display_text_animation(string, start_time):
#    current_time = pygame.time.get_ticks()  
#    letters = (current_time - start_time) // 100 
#    text = string[:letters]
#    WHITE = (255, 255, 255)
#    text_surface = temp_font.render(text, True, black)
#    text_rect = text_surface.get_rect()
#    text_rect.center = (500/2, 500/2)
#    screen.blit(text_surface, text_rect)

#class Words:
#    def __init__(self, text):
#        self.text = text
#        self.displayed = False

#test = Words("Testing this")


#def display_text_animation(string):
#    text = ''
#    for i in range(len(string.text)):
#        screen.fill(white)
#        text += string.text[i]
#        text_surface = temp_font.render(text, True, black)
#        text_rect = text_surface.get_rect()
#        text_rect.center = (WIDTH/2, HEIGHT/2)
#        screen.blit(text_surface, text_rect)
#        pygame.display.update()
#        pygame.time.wait(100)
#    string.displayed = True

#pygame.display.flip()
#start_time = pygame.time.get_ticks()
#while True:
    #draw_text(, temp_font, black, 250, 250)
#    display_text_animation(test) if not test.displayed else None
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            break
#    pygame.display.update()
#    clock.tick(60)

class Button:
    def __init__(self, selected, name):
        self.selected = selected
        self.name = name

    def changeSelected(self, other):
        self.selected = False
        other.selected = True
    

    def __str__(self):
        return f"{self.name} : {self.selected}"



b1 = Button(True, "b1")
b2 = Button(False, "b2")
b3 = Button(False, "b3")
b4 = Button(False, "b4")

B1 = True
B2 = False
B3 = False
B4 = False

buttonList = [b1, b2, b3, b4]

def changeButtons(buttons):
    while True:
        integral = int(input("Gib numbah: "))
        if integral == 1:
            for i in range(len(buttons)):
                if buttons[i].selected == True:
                    buttons[i].selected = False
                    buttons[i+1].selected = True
                    print(f"edited : {buttons[i]}\t tring to edit : {buttons[i+1]}")
                    break
            print(f"b1 : {b1.selected}\tb2 : {b2.selected}\t b3 : {b3.selected}\t b4 : {b4.selected}")
        if integral == 0:
            break

"""
print(f"{b1}\t{b2}\t{b3}\t{b4}")
limiter = (len(buttonList)-1)
print(limiter)
NegLimiter = (limiter * -1)
print(NegLimiter)
while True:
        integral = int(input("Gib numbah: "))
        if integral == 1:
            for i in range(len(buttonList)+1):
                if buttonList[i].selected == True:
                    if i+1 > limiter:
                        buttonList[i].changeSelected(buttonList[0])
                        i = 0
                        break
                    else:
                        buttonList[i].changeSelected(buttonList[i+1])
                        break
            print(f"{b1}\t{b2}\t{b3}\t{b4}")
        if integral == 0:
            break
        if integral == 2:
            for i in range(len(buttonList)+1):
                i *= -1
                if buttonList[i].selected == True:
                    if i-1 < NegLimiter:
                        buttonList[i].changeSelected(buttonList[0])
                        i = 0
                        break
                    else:
                        buttonList[i].changeSelected(buttonList[i-1])
                        break
            print(f"{b1}\t{b2}\t{b3}\t{b4}")
            """
#changeButtons(buttonList)
#print(buttonList[2])

results = ("test", "test2")
result1, result2 = results[0], results[1]
print(results)
print(result1)
print(result2)