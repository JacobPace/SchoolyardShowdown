# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
from game import *
from Dialouge import *
import sys
from random import randint
from time import sleep
from Constants import *
pygame.init()

# set some global variables
menuCycleRightDown = [pygame.K_RIGHT, pygame.K_d, pygame.K_s, pygame.K_DOWN]
menuCycleLeftUp = [pygame.K_w, pygame.K_a, pygame.K_LEFT, pygame.K_UP]

# set screen size and initialize some pygame stuff


# set color(s) with the RGB code for html
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)

# gives the window a name
pygame.display.set_caption("Test window")

# Initialize the buttons via the "game" file (where we put the recycleable code)
# when making the buttons the inputs look like this "x, y, image, imgHover, scale, selected by default?"
# start menu buttons


# initalize the player/enemy for testing purposes
lil_dude = pygame.image.load('images/lil_dude.png').convert_alpha()
player = Player(100,100, lil_dude) # taken areguments are the default x,y coordinates

enemyImg = pygame.image.load('images/enemy.png').convert_alpha()
enemyTest = Enemy(enemyImg)

# images class takes x,y values of the top left coordinate, image variable, and scale
playerTest = Image(100, 500, lil_dude, 1)


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

# Print text slowly
def SlowText(string, x, y):
    text = ''
    for i in range(len(string.text)):
        text += string.text[i]
        text_surface = temp_font.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(50)
    string.displayed = True

# not working how i want it to, I will do more testing later
def ChangingButtons(buttons, integral):
    limiter = (len(buttons)-1)
    NegLimiter = (limiter * -1)
    if integral == 1:
        for i in range(len(buttons)+1):
            if buttons[i].selected == True:
                if i+1 > limiter:
                    buttons[i].changeButton(buttons[0])
                    i = 0
                    break
                else:
                    buttons[i].changeButton(buttons[i+1])
                    break

    if integral == -1:
        for i in range(len(buttons)+1):
            i *= -1
            if buttons[i].selected == True:
                if i-1 < NegLimiter:
                    buttons[i].changeButton(buttons[0])
                    i = 0
                    break
                else:
                    buttons[i].changeButton(buttons[i-1])
                    break
    #StartMenu()

##### START MENU #####
def StartMenu():
    screen.fill((0,255,255))
    while True:
        # event checker
        start_button.draw(screen)
        exit_button.draw(screen)
        options_button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                break
        
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                if event.key in menuCycleRightDown and not buttonCooldown:
                    #change selected button from start to exit
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
                        buttonCooldown = True
                        screen.fill(white)
                        StoryMode()
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        BossRush()
                        #pygame.quit()
                if event.key == pygame.K_RETURN and options_button.selected:
                    screen.fill((0,255,255))
                    #OptionsMenu()
                    BossRush()
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
                pygame.display.quit()
                pygame.quit()
                break
                
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key in menuCycleLeftUp or event.key in menuCycleRightDown:
                    
                    if back_button.selected and not buttonCooldown:
                        exit_button2.changeButton(back_button)
                        buttonCooldown = True

                    if exit_button2.selected and not buttonCooldown:
                        back_button.changeButton(exit_button2)
                        buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and back_button.selected:
                    if back_button.action():
                        screen.fill((0,255,255))
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
                pygame.display.quit()
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    StoryMode()
                if event.key == pygame.K_BACKSPACE:
                    paused = False
                    StartMenu()
        pygame.display.update()
        clock.tick(60)
##### END OF PAUSE EMNU #####

##### STORY MODE #####
def StoryMode():
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
                pygame.display.quit()
                pygame.quit()
                break
            
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

            pygame.display.update()
            clock.tick(60)

        # Actual movement of player with border constraints
        if moveRight and player.x<WIDTH-player.width:
            player.x += 5
        if moveLeft and player.x>0:
            player.x -= 5
        if moveDown and player.y<HEIGHT-player.height:
            player.y += 5
        if moveUp and player.y>0:
            player.y -= 5
           
##### END OF CURRENT MAIN GAME LOOP #####  

##### BOSS RUSH MODE #####
def BossRush():
    Battle(enemyTest)

def Battle(foe):
    screen.fill(white)
    TextBox.draw(screen)
    playerTest.draw(screen)
    enemyTest.draw(screen)
    turn = 0
    SlowText(enemyLine1, 100, 850) if not enemyLine1.displayed else None
    sleep(2)
    TextBox.draw(screen)
    SlowText(playerOpeningLine1, 100, 850) if not playerOpeningLine1.displayed else None
    sleep(2)
    TextBox.draw(screen)
    SlowText(enemyLine2, 100, 850) if not enemyLine2.displayed else None
    sleep(2)
    TextBox.draw(screen)
    BattleSelectionMenu()

def BattleSelectionMenu():
    while True:
        TextBox.draw(screen)
        AttackButton.draw(screen)
        RunButton.draw(screen)
        BagButton.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_BACKSPACE:
                    StartMenu()
                if event.key in menuCycleRightDown:
                    if AttackButton.selected and not buttonCooldown:
                        RunButton.changeButton(AttackButton)
                        buttonCooldown = True
                    if RunButton.selected and not buttonCooldown:
                        BagButton.changeButton(RunButton)
                        buttonCooldown = True
                    if BagButton.selected and not buttonCooldown:
                        AttackButton.changeButton(BagButton)
                        buttonCooldown = True

                if event.key in menuCycleLeftUp:
                    if AttackButton.selected and not buttonCooldown:
                        BagButton.changeButton(AttackButton)
                        buttonCooldown = True
                    if BagButton.selected and not buttonCooldown:
                        RunButton.changeButton(BagButton)
                        buttonCooldown = True
                    if RunButton.selected and not buttonCooldown:
                        AttackButton.changeButton(RunButton)
                        buttonCooldown = True 

                if event.key == pygame.K_RETURN and AttackButton.selected:
                    BattleAttackMenu()    
        pygame.display.update()
        clock.tick(60)

def BattleAttackMenu():
    while True:
        TextBox.draw(screen)
        RockButton.draw(screen)
        PaperButton.draw(screen)
        ScissorsButton.draw(screen)
        BlockButton.draw(screen)
        BackButton.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key in menuCycleRightDown:
                    if RockButton.selected and not buttonCooldown:
                        PaperButton.changeButton(RockButton)
                        buttonCooldown = True
                    if PaperButton.selected and not buttonCooldown:
                        ScissorsButton.changeButton(PaperButton)
                        buttonCooldown = True
                    if ScissorsButton.selected and not buttonCooldown:
                        BlockButton.changeButton(ScissorsButton)
                        buttonCooldown = True
                    if BlockButton.selected and not buttonCooldown:
                        BackButton.changeButton(BlockButton)
                        buttonCooldown = True
                    if BackButton.selected and not buttonCooldown:
                        RockButton.changeButton(BackButton)
                        buttonCooldown = True

                if event.key in menuCycleLeftUp:
                    if RockButton.selected and not buttonCooldown:
                        BackButton.changeButton(RockButton)
                        buttonCooldown = True
                    if BackButton.selected and not buttonCooldown:
                        BlockButton.changeButton(BackButton)
                        buttonCooldown = True
                    if BlockButton.selected and not buttonCooldown:
                        ScissorsButton.changeButton(BlockButton)
                        buttonCooldown = True
                    if ScissorsButton.selected and not buttonCooldown:
                        PaperButton.changeButton(ScissorsButton)
                        buttonCooldown = True
                    if PaperButton.selected  and not buttonCooldown:
                        RockButton.changeButton(PaperButton)
                        buttonCooldown = True

                if event.key == pygame.K_RETURN and BackButton.selected:
                    BattleSelectionMenu()


        pygame.display.update()
        clock.tick(60)

def Lose():
    pass

def Win():
    pass

def Credits():
    pass


StartMenu()
pygame.display.quit()
pygame.quit()