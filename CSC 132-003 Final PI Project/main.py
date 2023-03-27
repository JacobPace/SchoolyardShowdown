# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
import game
pygame.init()

# set some global variables
menuCycleHorizontal = [pygame.K_a, pygame.K_d]
menuCycleVertical = [pygame.K_w, pygame.K_s]

# set screen size and initialize some pygame stuff
WIDTH = 1024
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# set color(s) with the RGB code for html
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
# start menu buttons
start_button = game.Button(50, 100, start_img, start_hover, 0.8, True)
exit_button = game.Button(50, 250, exit_img, exit_hover, 0.8, False)
options_button = game.Button(50, 400, options_img, options_hover, 1, False)
# options menu buttons
back_button = game.Button(50, 500 , back_img, back_hover, 1, True)
exit_button2 = game.Button(295, 500, exit_img, exit_hover, 0.8, False)

# initalize the player
lil_dude = pygame.image.load('images/lil_dude.png').convert_alpha()
player = game.Player(100,100, lil_dude) # taken areguments are the default x,y coordinates

##### ACTUAL CODE STARTS HERE #####

# Display the window
pygame.display.flip()

##### DISPLAY TEXT TO SCREEN #####
temp_font = pygame.font.SysFont("Arial", 25)
def draw_text(text, font, text_color,x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y)) 
# when calling this function it should look like
# draw_text("What you want the text to be", your font variable, color of the text, x coordinate, y coordinate)                            

##### START MENU #####
def StartMenu():
    current_menu = "start"
    screen.fill((0,255,255))
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

                    # Change the exit button to the options button
                    if exit_button.selected and not buttonCooldown:
                        options_button.changeButton(exit_button)
                        buttonCooldown = True

                    # Change from options button to start button
                    if options_button.selected and not buttonCooldown:
                        start_button.changeButton(options_button)
                        buttonCooldown = True

                # Press the "A" key to move the selected button to the left
                if event.key == pygame.K_a:
                    # change selected button from start to options
                    if start_button.selected and not buttonCooldown:
                        options_button.changeButton(start_button)
                        buttonCooldown = True

                    # Change the options button to the exit button
                    if options_button.selected and not buttonCooldown:
                        exit_button.changeButton(options_button)
                        buttonCooldown = True

                    # Change from exit to start
                    if exit_button.selected and not buttonCooldown:
                        start_button.changeButton(exit_button)
                        buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and start_button.selected:
                    if start_button.action():
                        #current_menu = None
                        buttonCooldown = True
                        screen.fill(white)
                        Game()
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        print("EXIT")
                        pygame.quit()
                if event.key == pygame.K_RETURN and options_button.selected:
                    current_menu = "options"
                    screen.fill(white)
                    OptionsMenu()
        pygame.display.update()
        clock.tick(60)
##### END OF CURRENT START MENU CODE #####

##### OPTIONS MENU #####
def OptionsMenu():
    current_menu = "options"
    while current_menu == "options":
        back_button.draw(screen)
        exit_button2.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key in menuCycleHorizontal:
                    
                    if back_button.selected and not buttonCooldown:
                        exit_button2.changeButton(back_button)
                        buttonCooldown = True

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
                        pygame.quit()
        pygame.display.update()
        clock.tick(60)
##### END OF CURRENT OPTIONS MENU CODE #####

##### PAUSE MENU #####
def pauseMenu():
    paused = True
    while paused:
        pygame.draw.rect(screen, white, pygame.Rect(50, 50, 600, 600))
        draw_text("The game is now paused, press 'SPACE' to resume!", temp_font, (0,0,0), 55, 360)
        draw_text("Or press 'BACKSPACE' to return to the start menu!", temp_font, (0,0,0),55, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    Game()
                if event.key == pygame.K_BACKSPACE:
                    paused = False
                    StartMenu()
        pygame.display.update()
        clock.tick(60)
##### END OF PAUSE EMNU #####

##### MAIN GAME LOOP #####
def Game():
    game = True
    moveRight = False
    moveLeft = False
    moveDown = False
    moveUp = False
    while game:
        screen.fill((0,0,0))
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
            
            ##### Movement / Pause Menu #####
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moveLeft = True
                if event.key == pygame.K_s:
                    moveDown = True
                if event.key == pygame.K_w:
                    moveUp = True
                if event.key == pygame.K_d:
                    moveRight = True
                # Check if player wants to pause the game
                if event.key == pygame.K_p:
                    moveDown, moveLeft, moveRight, moveUp = False, False, False, False
                    game = False
                    pauseMenu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moveLeft = False
                if event.key == pygame.K_s:
                    moveDown = False
                if event.key == pygame.K_w:
                    moveUp = False
                if event.key == pygame.K_d:
                    moveRight = False

        # Actual movement of player with border constraints
        if moveRight and player.x<WIDTH-player.width:
            player.x += 5
        if moveLeft and player.x>0:
            player.x -= 5
        if moveDown and player.y<HEIGHT-player.height:
            player.y += 5
        if moveUp and player.y>0:
            player.y -= 5
           
        pygame.display.update()
        clock.tick(60)
##### END OF CURRENT MAIN GAME LOOP #####  

StartMenu()
pygame.quit()