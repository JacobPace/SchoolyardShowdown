# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
import game
pygame.init()

# set some global variables
menuCycleHorizontal = [pygame.K_a, pygame.K_d]
menuCycleVertical = [pygame.K_w, pygame.K_s]

# set screen size
res = (720, 720)
screen = pygame.display.set_mode(res)

# set a color witht he RGB code for html
white = (255, 255, 255)
screen.fill(white)

# gives the window a name
pygame.display.set_caption("Test window")

# images for the buttons
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
start_hover = pygame.image.load('images/start_btn_hover.png').convert_alpha()

exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()
exit_hover = pygame.image.load('images/exit_btn_hover.png').convert_alpha()

# Initialize the buttons via the "game" file (where we put the recycleable code)
start_button = game.Button(100, 200, start_img, start_hover, 1, True)
exit_button = game.Button(400, 200, exit_img, exit_hover, 1, False)

# Self explanitory
def changeToStart():
    exit_button.selected = False
    start_button.selected = True
    start_button.default = False

def changeToExit():
    start_button.selected = False
    start_button.default = False
    exit_button.selected = True

### ACTUAL CODE STARTS HERE ###

# Display the window
pygame.display.flip()

# Quit function / close window / event checker
running = True
while running:
    start_button.draw(screen)
    exit_button.draw(screen)

    # event checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            cooldown = False
            if event.key in menuCycleHorizontal:
                
                # Change the exit button to the start button
                if exit_button.selected and not start_button.selected and not cooldown:
                    # change from exit to start
                    changeToStart()
                    cooldown = True

                # Change the start button to the exit button and remove the default value
                if start_button.default and not exit_button.selected and not cooldown:
                    # chage from start to exit
                    changeToExit()
                    cooldown = True
                
                # Change the start button to the exit button and remove the default value
                if start_button.selected and not exit_button.selected and not cooldown:
                    # chage from start to exit
                    changeToExit()
                    cooldown = True

            # Checks for the "Enter / Return" key being pressed and which button is selected
            if event.key == pygame.K_RETURN and start_button.selected or start_button.default:
                if start_button.action():
                    print("Working")
            if event.key == pygame.K_RETURN and exit_button.selected:
                if exit_button.action():
                    print("Test")
    
    # updates the frames of the game 
    pygame.display.update()