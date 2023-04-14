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

# set DISPLAYSURF size and initialize some pygame stuff

# set color(s) with the RGB code for html
white = (255, 255, 255)
black = (0, 0, 0)
DISPLAYSURF.fill(white)

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
enemytest = Image(1500, 100, enemyImg, 10)

# images class takes x,y values of the top left coordinate, image variable, and scale
playerTest = Image(100, 400, lil_dude, 10)

##### ACTUAL CODE STARTS HERE #####

# Display the window
pygame.display.flip()

##### DISPLAY TEXT TO DISPLAYSURF #####
temp_font = pygame.font.SysFont("Arial", 25)
def draw_text(text, font, text_color,x, y):
    img = font.render(text, True, text_color)
    DISPLAYSURF.blit(img, (x, y)) 
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
        DISPLAYSURF.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(50)
    string.displayed = True

# Print text slowly not from the dialouge class
def SlowText2(string, x, y):
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = temp_font.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        DISPLAYSURF.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(50)

# not working how i want it to, I will do more testing later
def ChangingButtons(buttons, integral):
    limiter = (len(buttons)-1)
    NegLimiter = (limiter * -1)
    if integral == 1:
        for i in range(len(buttons)+1):
            if buttons[i].selected == True:
                if i+1 > limiter:
                    buttons[0].changeButton(buttons[i])
                    i = 0
                    break
                else:
                    buttons[i+1].changeButton(buttons[i])
                    break

    if integral == -1:
        for i in range(len(buttons)+1):
            i *= -1
            if buttons[i].selected == True:
                if i-1 < NegLimiter:
                    buttons[0].changeButton(buttons[i])
                    i = 0
                    break
                else:
                    buttons[i-1].changeButton(buttons[i])
                    break

##### START MENU #####
def StartMenu():
    DISPLAYSURF.fill((0,255,255))
    buttons = [start_button, exit_button, options_button]
    while True:
        # event checker
        start_button.draw(DISPLAYSURF)
        exit_button.draw(DISPLAYSURF)
        options_button.draw(DISPLAYSURF)
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
                    ChangingButtons(buttons, 1)
                    buttonCooldown = True
                    
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(buttons, -1)
                    buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and start_button.selected:
                    if start_button.action():
                        buttonCooldown = True
                        DISPLAYSURF.fill(white)
                        StoryMode()
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        BossRush()
                        #pygame.quit()
                if event.key == pygame.K_RETURN and options_button.selected:
                    DISPLAYSURF.fill((0,255,255))
                    #OptionsMenu()
                    BossRush()
                    break
            pygame.display.update()
            clock.tick(60)
##### END OF CURRENT START MENU CODE #####

##### OPTIONS MENU #####
def OptionsMenu():
    current_menu = "options"
    while current_menu == "options":
        back_button.draw(DISPLAYSURF)
        exit_button2.draw(DISPLAYSURF)
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
                        DISPLAYSURF.fill((0,255,255))
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
        pygame.draw.rect(DISPLAYSURF, white, pygame.Rect(50, 50, 600, 600))
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
        DISPLAYSURF.fill((0,0,0))
        player.draw(DISPLAYSURF)
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
    DISPLAYSURF.fill(white)
    TextBox.draw(DISPLAYSURF)
    playerTest.draw(DISPLAYSURF)
    enemytest.draw(DISPLAYSURF)
    #turn = 0
    
    SlowText(enemyLine1, 100, 850) if not enemyLine1.displayed else None
    sleep(2)
    TextBox.draw(DISPLAYSURF)
    SlowText(playerOpeningLine1, 100, 850) if not playerOpeningLine1.displayed else None
    sleep(2)
    TextBox.draw(DISPLAYSURF)
    SlowText(enemyLine2, 100, 850) if not enemyLine2.displayed else None
    sleep(2)
    TextBox.draw(DISPLAYSURF)
    
    BattleAttackMenu(foe)
    
def BattleAttackMenu(foe):
    PlayerAction = ""
    FoeAction = ""
    FinalResult = ""
    menu = "selection"
    BattleSelctionButtons = [AttackButton, RunButton, BagButton]
    AttackButtons = [RockButton, PaperButton, ScissorsButton, BlockButton, BackButton]
    while True:
        PlayerAction = ""
        FoeAction = ""
        FinalResult = ""

        if foe.health <= 0:
            TextBox.draw(DISPLAYSURF)
            SlowText(enemyLoss, 100, 850) if not enemyLoss.displayed else None
            sleep(1)
            TextBox.draw(DISPLAYSURF)
            SlowText(victory, 100, 850) if not victory.displayed else None
            draw_text(victoryAlt, temp_font,black, 100, 850)

        if menu == "selection" and foe.health > 0:
            TextBox.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            RunButton.draw(DISPLAYSURF)
            BagButton.draw(DISPLAYSURF)
            pygame.display.update()

        if menu == "action" and foe.health > 0:
            TextBox.draw(DISPLAYSURF)
            RockButton.draw(DISPLAYSURF)
            PaperButton.draw(DISPLAYSURF)
            ScissorsButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
            BackButton.draw(DISPLAYSURF)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_BACKSPACE:
                    StartMenu()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break
                if event.key in menuCycleRightDown and not buttonCooldown and menu =="selection":
                    ChangingButtons(BattleSelctionButtons, 1)
                    buttonCooldown = True
                if event.key in menuCycleLeftUp and not buttonCooldown and menu == "selection":
                    ChangingButtons(BattleSelctionButtons, -1) 
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and AttackButton.selected and menu == "selection":
                    if AttackButton.action():
                        menu = "action"

                #if event.key == pygame.K_RETURN and AttackButton.selected and menu == "action":
                #    menu = "selection"
                    buttonCooldown = True
                if event.key in menuCycleRightDown and not buttonCooldown and menu == "action":
                    ChangingButtons(AttackButtons, 1)
                    buttonCooldown = True
                if event.key in menuCycleLeftUp and not buttonCooldown and menu == "action":
                    ChangingButtons(AttackButtons, -1)
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and RockButton.selected and menu == "action" and not buttonCooldown:
                    if RockButton.action():
                        PlayerAction = "Rock"
                        FoeAction = foe.action()
                        buttonCooldown = True
                if event.key == pygame.K_RETURN and PaperButton.selected and menu == "action":
                    if PaperButton.action():
                        PlayerAction = "Paper"
                        FoeAction = foe.action()
                if event.key == pygame.K_RETURN and ScissorsButton.selected and menu == "action":
                    if ScissorsButton.action():
                        PlayerAction = "Scissors"
                        FoeAction = foe.action()
                if event.key == pygame.K_RETURN and BlockButton.selected and menu == "action":
                    if BlockButton.action():
                        PlayerAction = "Block"
                        FoeAction = foe.action()
                if event.key == pygame.K_RETURN and BackButton.selected and menu == "action":
                    if BackButton.action:
                        menu = "selection"

        if PlayerAction == FoeAction:
            FinalResult = "It's a draw?"
        elif PlayerAction == "Block":
            FinalResult = "You blocked it!"
        elif FoeAction == "Block":
            FinalResult = "They blocked!"

        elif PlayerAction == "Rock" and FoeAction == "Paper":
            FinalResult = "That hurt!"
            player.health -= 1
        elif PlayerAction == "Rock" and FoeAction == "Scissors":
            FinalResult = "That'll show them!"
            foe.health -= 1
        
            
        elif PlayerAction == "Paper" and FoeAction == "Scissors":
            FinalResult = "That hurt!"
            player.health -= 1
        elif PlayerAction == "Paper" and FoeAction == "Rock":
            FinalResult = "That'll show them!"
            foe.health -= 1

        elif PlayerAction == "Scissors" and FoeAction == "Rock":
            FinalResult = "That hurt!"
            player.health -= 1
        elif PlayerAction == "Scissors" and FoeAction == "Paper":
            FinalResult = "That'll show them!"
            foe.health -= 1

        if PlayerAction != "":
            print("Bug fixing")
            print(f"Player: {PlayerAction}")
            print(f"Enemy {FoeAction}")
            TextBox.draw(DISPLAYSURF)
            print(FinalResult)
            SlowText2(FinalResult, 100, 850)
            sleep(2)
            menu == "selection"

        pygame.display.update()
        clock.tick(60)
    
        
        pygame.display.update()
        clock.tick(60)

def LoseGame():
    pass

def WinGame():
    pass

def Credits():
    pass


StartMenu()
pygame.display.quit()
pygame.quit()