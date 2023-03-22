# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
import game
pygame.init()

# set some global variables
menuCycleHorizontal = [pygame.K_a, pygame.K_d]
menuCycleVertical = [pygame.K_w, pygame.K_s]

# making the menu states
current_menu = "start"
prev_menu = None

# set screen size
res = (720, 720)
screen = pygame.display.set_mode(res)

# set a color witht he RGB code for html
white = (255, 255, 255)
screen.fill(white)

# gives the window a name
pygame.display.set_caption("Test window")

# images for the buttons (start menu)
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
start_hover = pygame.image.load('images/start_btn_hover.png').convert_alpha()

exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()
exit_hover = pygame.image.load('images/exit_btn_hover.png').convert_alpha()

options_img = pygame.image.load('images/button_options.png').convert_alpha()
options_hover = pygame.image.load('images/button_options_hover.png').convert_alpha()

#################################################################################
# images for options menu
back_img = pygame.image.load('images/button_back.png').convert_alpha()
back_hover = pygame.image.load('images/button_back_hover.png').convert_alpha()

# Initialize the buttons via the "game" file (where we put the recycleable code)
# when making the buttons the inputs look like this "x, y, image, imgHover, scale, selected by default?"
start_button = game.Button(50, 500, start_img, start_hover, 0.8, True)
exit_button = game.Button(295, 500, exit_img, exit_hover, 0.8, False)
options_button = game.Button(500, 500, options_img, options_hover, 1, False)


back_button = game.Button(50, 500 , back_img, back_hover, 1, True)
exit_button2 = game.Button(295, 500, exit_img, exit_hover, 0.8, False)

##### ACTUAL CODE STARTS HERE #####

# Display the window
pygame.display.flip()

##### START MENU #####
def StartMenu():
    current_menu = "start"
    while current_menu == "start":
        # event checker
        start_button.draw(screen)
        exit_button.draw(screen)
        options_button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False

                # Press the "D" key to move slected button to the right
                if event.key == pygame.K_d:
                    # change selected button from start to exit
                    if start_button.selected and not buttonCooldown:
                        exit_button.changeButton(start_button)
                        buttonCooldown = True

                    # Change the exit button to the start button
                    if exit_button.selected and not buttonCooldown:
                        options_button.changeButton(exit_button)
                        buttonCooldown = True

                    if options_button.selected and not buttonCooldown:
                        start_button.changeButton(options_button)
                        buttonCooldown = True

                # Press the "A" key to move the selected button to the left
                if event.key == pygame.K_a:
                    # change selected button from start to exit
                    if start_button.selected and not buttonCooldown:
                        options_button.changeButton(start_button)
                        buttonCooldown = True

                    # Change the exit button to the start button
                    if options_button.selected and not buttonCooldown:
                        exit_button.changeButton(options_button)
                        buttonCooldown = True

                    if exit_button.selected and not buttonCooldown:
                        start_button.changeButton(exit_button)
                        buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and start_button.selected:
                    if start_button.action():
                        print("START")
                        buttonCooldown = True
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        print("EXIT")
                        buttonCooldown = True
                if event.key == pygame.K_RETURN and options_button.selected:
                    current_menu = "options"
                    screen.fill(white)
                    OptionsMenu()
                if event.key == pygame.K_SPACE:
                    current_menu = "options"
                    screen.fill(white)
        pygame.display.update()
##### END OF CURRENT START MENU CODE #####

##### OPTIONS MENU #####
def OptionsMenu():
    current_menu = "options"
    while current_menu == "options":
        back_button.draw(screen)
        exit_button2.draw(screen)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key in menuCycleHorizontal:
                    # change selected button from start to exit
                    if back_button.selected and not buttonCooldown:
                        exit_button2.changeButton(back_button)
                        buttonCooldown = True

                    # Change the exit button to the start button
                    if exit_button2.selected and not buttonCooldown:
                        back_button.changeButton(exit_button2)
                        buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and back_button.selected:
                    if back_button.action():
                        screen.fill(white)
                        StartMenu()
                        
                if event.key == pygame.K_RETURN and exit_button2.selected:
                    if exit_button2.action():
                        print("EXIT")
        pygame.display.update()
    # updates the frames of the game 
StartMenu()
pygame.quit()