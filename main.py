# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
from game import *
from Dialouge import *
import sys
from random import randint
from time import sleep
from Constants import *
import math
pygame.init()

# set some global variables

menuCycleRightDown = [pygame.K_RIGHT, pygame.K_d, pygame.K_s, pygame.K_DOWN]
menuCycleLeftUp = [pygame.K_w, pygame.K_a, pygame.K_LEFT, pygame.K_UP]
scroll = 0
turn = 0

# set DISPLAYSURF size and initialize some pygame stuff

# set color(s) with the RGB code for html
white = (255, 255, 255)
black = (0, 0, 0)
DISPLAYSURF.fill(white)

# gives the window a name
pygame.display.set_caption("Test window")

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

# Function to dynamically change the buttons in menus
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

def Quit():
    pygame.display.quit()
    pygame.quit()
    quit()

##### START MENU #####
def StartMenu():
    buttons = [start_button, exit_button, options_button]
    scroll = 0
    while True:
        clock.tick(33)
        for i in range(0, tiles):
            DISPLAYSURF.blit(bg, (bg.get_width()*i+ scroll, 0))
            i += 1
        # FRAME FOR SCROLLING
        scroll -= 6
  
        # RESET THE SCROLL FRAME
        if abs(scroll) > bg.get_width():
            scroll = 0
        # CLOSING THE FRAME OF SCROLLING
        start_button.draw(DISPLAYSURF)
        exit_button.draw(DISPLAYSURF)
        options_button.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
        
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()

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
                        BossRush()
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        Quit()
                if event.key == pygame.K_RETURN and options_button.selected:
                    DISPLAYSURF.fill((0,255,255))
                    OptionsMenu()

        pygame.display.update()

##### END OF CURRENT START MENU CODE #####

##### OPTIONS MENU #####
def OptionsMenu():
    optionsButtons = [exit_button2, back_button]
    while True:
        back_button.draw(DISPLAYSURF)
        exit_button2.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(optionsButtons, -1)
                    buttonCooldown = True
                if event.key in menuCycleRightDown and not buttonCooldown:
                    ChangingButtons(optionsButtons, 1)
                    buttonCooldown = True
                    
                # Checks for the "Enter / Return" key being pressed and which button is selected
                if event.key == pygame.K_RETURN and back_button.selected:
                    if back_button.action():
                        DISPLAYSURF.fill((0,255,255))
                        StartMenu()
                        
                if event.key == pygame.K_RETURN and exit_button2.selected:
                    if exit_button2.action():
                        Quit()
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

##### BOSS RUSH MODE #####
def BossRush():
    Battle(Ronald, None)

def Battle(foe, voiceLines):
    voiceLines = None
    DISPLAYSURF.fill(white)
    #BattleSelectionMenu.draw(DISPLAYSURF)
    playerTest.draw(DISPLAYSURF)
    enemytest.draw(DISPLAYSURF)
    GruntHealthBar5.draw(DISPLAYSURF) if foe.type != "boss" else None
    #draw_text(foe.name, temp_font, black, 1125, 125)
    PlayerHealthBarFull.draw(DISPLAYSURF)
    #draw_text("Player", temp_font, black, 425, 325)
    #turn = 0
    #for i in voiceLines:
    #    SpeechBox.draw(DISPLAYSURF)
    #    pygame.display.update()
    #    SlowText2(i, 100, 850)
    #    pygame.display.update()
    #    sleep(2)
    #    SpeechBox.draw(DISPLAYSURF)
    #    pygame.display.update()
    
    BattleSelectMenu(foe)

def ThrowHands(PlayerAction, FoeAction, pBlock, fBlock, draw, playerWon, enemyWon):
    for i in range(0, 3):
        ##### ITERATION #####
        DISPLAYSURF.fill(white)
        PlayerThrow.draw(DISPLAYSURF)
        EnemyThrow.draw(DISPLAYSURF)
        pygame.time.wait(500)
        pygame.display.update()
        DISPLAYSURF.fill(white)
        PlayerRock.draw(DISPLAYSURF)
        enemytest.draw(DISPLAYSURF)
        pygame.time.wait(500)
        pygame.display.update()              
        DISPLAYSURF.fill(white)
    if draw:
        EnemyRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
        EnemyPaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
        EnemyScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
        EnemyBlockPic.draw(DISPLAYSURF) if FoeAction == "Block" else None
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        PlayerBlockPic.draw(DISPLAYSURF) if PlayerAction == "Block" else None
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        BattleDraw.draw(DISPLAYSURF)
        pygame.time.wait(500)
    elif PlayerAction == "Block" and not draw:
        if pBlock:
            PlayerBlockPic.draw(DISPLAYSURF)
            EnemyRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
            EnemyPaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
            EnemyScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
            BattleSelectionMenu3.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
            BagButton.draw(DISPLAYSURF)
            PlayerBlocked.draw(DISPLAYSURF)
            pygame.time.wait(500)
        elif not pBlock:
            PlayerStanding.draw(DISPLAYSURF)
            EnemyRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
            EnemyPaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
            EnemyScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
            BattleSelectionMenu3.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
            BagButton.draw(DISPLAYSURF)
            PlayerBlockFailed.draw(DISPLAYSURF)
            pygame.time.wait(500)
    elif fBlock and not draw:
        EnemyBlockPic.draw(DISPLAYSURF)
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        EnemyBlocked.draw(DISPLAYSURF)
        pygame.time.wait(500)
    else:
        EnemyRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
        EnemyPaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
        EnemyScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        pygame.time.wait(500)
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        WonRound.draw(DISPLAYSURF) if playerWon else None
        LostRound.draw(DISPLAYSURF) if enemyWon else None
    pygame.display.update()
    
            
def HealedResult(foe, FoeAction):
    if player.health + 3 > 7:
        player.health = 7
    else:
        player.health += 3
    for i in range(0, 3):
        ##### ITERATION #####
        DISPLAYSURF.fill(white)
        EnemyThrow.draw(DISPLAYSURF)
        pygame.time.wait(500)
        pygame.display.update()
        DISPLAYSURF.fill(white)
        enemytest.draw(DISPLAYSURF)
        pygame.time.wait(500)
        pygame.display.update()              
        DISPLAYSURF.fill(white)
    FoeAction = foe.action()
    player.bandAids -= 1
    EnemyRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
    EnemyPaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
    EnemyScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
    EnemyBlockPic.draw(DISPLAYSURF) if FoeAction == "Block" else None
    print(FoeAction)
    pygame.display.update()
    pygame.time.wait(1000)
    BattleSelectMenu(foe)

def BattleSelectMenu(foe):
    DISPLAYSURF.fill(white)
    PlayerStanding.draw(DISPLAYSURF)
    enemytest.draw(DISPLAYSURF)
    PlayerAction = ""
    FoeAction = ""
    #FinalResult = ""
    SelectMenuButtons = [AttackButton, BlockButton, BagButton]
    PlayerHealthBar = [PlayerHealthBarEmpty, PlayerHealthBar1, PlayerHealthBar2, PlayerHealthBar3, PlayerHealthBar4, PlayerHealthBar5, PlayerHealthBar6, PlayerHealthBarFull]
    GruntHealthBar = [GruntHealthBar0, GruntHealthBar1, GruntHealthBar2, GruntHealthBar3, GruntHealthBar4, GruntHealthBar5]
    #BossHealthBar = []
    while True:
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    pygame.display.quit()
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(SelectMenuButtons, -1)
                    buttonCooldown = True
                if event.key in menuCycleRightDown and not buttonCooldown:
                    ChangingButtons(SelectMenuButtons, 1)
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and not buttonCooldown and AttackButton.selected:
                    if AttackButton.action():
                        BattleAttackMenu(foe)
                if event.key == pygame.K_RETURN and not buttonCooldown and BlockButton.selected:
                    PlayerAction = "Block"
                    FoeAction = foe.action()
                    RoundResults(foe, PlayerAction, FoeAction)
                if event.key == pygame.K_RETURN and not buttonCooldown and BagButton.selected:
                    if BagButton.action:
                        BattleBagMenu(foe)

            if foe.type != "boss":
                if foe.health == 0:
                    GruntHealthBar[0].draw(DISPLAYSURF)
                if foe.health > 0:
                    GruntHealthBar[foe.health].draw(DISPLAYSURF)
            draw_text(foe.name, temp_font, black, 1125, 70)
            if player.health == 0:
                PlayerHealthBar[0].draw(DISPLAYSURF)
            if player.health > 0:
                PlayerHealthBar[player.health].draw(DISPLAYSURF)
            draw_text("Player", temp_font, black, 425, 320)
            clock.tick(60)
            pygame.display.update()

def BattleBagMenu(foe):
    BagButtons = [BandAid, BagMenuBackButton]
    BandAidImg = [BandAid0Img, BandAid1Img, BandAid2Img, BandAid3Img, BandAid4Img, BandAid5Img]
    BandAidImgSelected = [BandAid0ImgSelected, BandAid1ImgSelected, BandAid2ImgSelected, BandAid3ImgSelected, BandAid4ImgSelected, BandAid5ImgSelected]
    while True:
        BattleSelectionMenu2.draw(DISPLAYSURF)
        BandAid.draw(DISPLAYSURF)
        BagMenuBackButton.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(BagButtons, -1)
                    buttonCooldown = True
                if event.key in menuCycleRightDown and not buttonCooldown:
                    ChangingButtons(BagButtons, 1)
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and not buttonCooldown and BagMenuBackButton.selected:
                    if BagMenuBackButton.action():
                        BattleSelectMenu(foe)
                if event.key == pygame.K_RETURN and not buttonCooldown and BandAid.selected:
                    if player.health == 7:
                        SpeechBox.draw(DISPLAYSURF)

                    elif BandAid.action():
                        FoeAction = foe.action
                        HealedResult(foe, FoeAction)
        BandAid.image = BandAidImg[player.bandAids]
        BandAid.imgHover = BandAidImgSelected[player.bandAids]
        clock.tick(60)
        pygame.display.update()
        


def BattleAttackMenu(foe):
    PlayerAction = ""
    FoeAction = ""
    #FinalResult = ""
    AttackButtons = [RockButton, PaperButton, ScissorsButton, BackButton]
    while True:
        BattleSelectionMenu.draw(DISPLAYSURF)
        RockButton.draw(DISPLAYSURF)
        PaperButton.draw(DISPLAYSURF)
        ScissorsButton.draw(DISPLAYSURF)
        BackButton.draw(DISPLAYSURF)

        if foe.health <= 0:
            TextBox.draw(DISPLAYSURF)
            SlowText(enemyLoss, 100, 850) if not enemyLoss.displayed else None
            pygame.time.wait(2000)
            TextBox.draw(DISPLAYSURF)
            SlowText(victory, 100, 850) if not victory.displayed else None
            draw_text(victoryAlt, temp_font,black, 100, 850)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()
                # BUTTON CYCLE AND EVENT CHECKER
                if event.key in menuCycleRightDown and not buttonCooldown:
                    ChangingButtons(AttackButtons, 1)
                    buttonCooldown = True
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(AttackButtons, -1) 
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and RockButton.selected and not buttonCooldown:
                    if RockButton.action():
                        PlayerAction = "Rock"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction)
                if event.key == pygame.K_RETURN and PaperButton.selected and not buttonCooldown:
                    if PaperButton.action():
                        PlayerAction = "Paper"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction)
                if event.key == pygame.K_RETURN and ScissorsButton.selected and not buttonCooldown:
                    if ScissorsButton.action():
                        PlayerAction = "Scissors"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction)
                if event.key == pygame.K_RETURN and BlockButton.selected and not buttonCooldown:
                    if BlockButton.action():
                        PlayerAction = "Block"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction)
                if event.key == pygame.K_RETURN and BackButton.selected and not buttonCooldown:
                    if BackButton.action:
                        BattleSelectMenu(foe)
        pygame.display.update()
        clock.tick(60)

def RoundResults(foe, PlayerAction, FoeAction):
    if PlayerAction == "Heal":
        HealedResult(FoeAction)
        FinalResult = "You healed!"
    elif PlayerAction == FoeAction:
        ThrowHands(PlayerAction, FoeAction, False, False, True, False, False)
        FinalResult = "It's a draw?!"
    elif PlayerAction == "Block":
        blockChance = randint(1, 10)
        if blockChance > 1:
            ThrowHands(PlayerAction, FoeAction, True, False, False, False, False)
            FinalResult = "You blocked it!"
        elif blockChance == 1:
            FinalResult = "Your block Failed!"
            ThrowHands(PlayerAction, FoeAction, False, True, False, False, True)
            pygame.display.update()
            player.health -= 1
            pygame.display.update()
        elif FoeAction == "Block":
            ThrowHands(PlayerAction, FoeAction, False, False, False, False, False)
            FinalResult = "They blocked!"
            pygame.display.update()

    ##### PLAYER CHOOSE ROCK #####
    elif PlayerAction == "Rock" and FoeAction == "Paper":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True)
        FinalResult = "That hurt!"
        player.health -= 1
    elif PlayerAction == "Rock" and FoeAction == "Scissors":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False)
        FinalResult = "That'll show them!"
        pygame.display.update()
        foe.health -= 1
        
    ##### PLAYER CHOOSE PAPER #####
    elif PlayerAction == "Paper" and FoeAction == "Scissors":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True)
        FinalResult = "That hurt!"
        pygame.display.update()
        player.health -= 1
    elif PlayerAction == "Paper" and FoeAction == "Rock":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False)
        FinalResult = "That'll show them!"
        pygame.display.update()
        foe.health -= 1

    ##### PLAYER CHOOSE SCISSORS #####
    elif PlayerAction == "Scissors" and FoeAction == "Rock":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True)
        FinalResult = "That hurt!"
        pygame.display.update()
        player.health -= 1
    elif PlayerAction == "Scissors" and FoeAction == "Paper":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False)
        FinalResult = "That'll show them!"
        pygame.display.update()
        foe.health -= 1
    pygame.time.wait(1000)
    BattleSelectMenu(foe)

def Phase2(boss, turn):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        if turn < 3:
            pass
        clock.tick(60)
        pygame.display.update()

def LoseGame():
    Reset()

def WinGame():
    Reset()

def Credits():
    StartMenu()

def Reset():
    player.health = 7
    player.bandAids = 5
    Landon.health = 5
    Aiden.health = 5
    Fred.health = 5
    Joel.health = 7

StartMenu()