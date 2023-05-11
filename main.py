# Final PI Project Prototype

# Initialize basic pygame template and all needed globals / images / files ect.
import pygame
from game import *
from Dialouge import *
import sys
from random import randint
from Constants import *
from Controller import *
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
        pygame.time.wait(5)
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
        pygame.time.wait(5)

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
    buttonCooldown = False
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
        
        #need a change for the repo
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
                        #Intro()
                        Finale()
                if event.key == pygame.K_RETURN and exit_button.selected:
                    if exit_button.action():
                        Quit()
                if event.key == pygame.K_RETURN and options_button.selected:
                    DISPLAYSURF.fill((0,255,255))
                    OptionsMenu()
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(buttons, 1)
            #pygame.time.delay(500)
        if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(buttons, -1)
            #pygame.time.delay(500)
        if (GPIO.input(UpButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        if (GPIO.input(DownButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        ##### Controller Select Buttons
        if (GPIO.input(SelectButton) == GPIO.HIGH) and start_button.selected:
            DISPLAYSURF.fill(white)
            Intro()
        if (GPIO.input(SelectButton) == GPIO.HIGH) and exit_button.selected:
            #DISPLAYSURF.fill(white)
            #Quit()
            pass
        if (GPIO.input(SelectButton) == GPIO.HIGH) and options_button.selected:
            DISPLAYSURF.fill((0,255,255))
            OptionsMenu()
        

        pygame.display.update()

##### END OF CURRENT START MENU CODE #####

##### OPTIONS MENU #####
def OptionsMenu():
    buttonCooldown = False
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
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(optionsButtons, 1)
            pygame.time.delay(500)
        if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(optionsButtons, -1)
            pygame.time.delay(500)
        if (GPIO.input(UpButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        if (GPIO.input(DownButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        ##### Controller Select Buttons
        if (GPIO.input(SelectButton) == GPIO.HIGH) and back_button.selected:
            StartMenu()
        if (GPIO.input(SelectButton) == GPIO.HIGH) and exit_button2.selected:
            #DISPLAYSURF.fill(white)
            #Quit()
            pass
        
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
                Quit()
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
                Quit()
            
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

def Intro():
    buttonCooldown = False
    DISPLAYSURF.fill(white)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(Lore01, 100, 675)
    iteration = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    iteration += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            iteration += 1
        # Move through text
        if iteration == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore0, 100, 675) if not Lore0.displayed else draw_text(Lore0.text, temp_font, black, 100, 675)
        if iteration == 2:
            JoelIdle.draw(DISPLAYSURF)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore1, 100, 675) if not Lore1.displayed else draw_text(Lore1.text, temp_font, black, 100, 675)
        if iteration == 3:
            DISPLAYSURF.fill(black)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore2, 100, 675) if not Lore2.displayed else draw_text(Lore2.text, temp_font, black, 100, 675)
        if iteration == 4:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore3, 100, 675) if not Lore3.displayed else draw_text(Lore3.text, temp_font, black, 100, 675)
        if iteration == 5:
            DISPLAYSURF.fill(white)
            PlayerIdle.draw(DISPLAYSURF)
            JoelIdle.draw(DISPLAYSURF)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore4, 100, 675) if not Lore4.displayed else draw_text(Lore4.text, temp_font, black, 100, 675)
        if iteration == 6:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore5, 100, 675) if not Lore5.displayed else draw_text(Lore5.text, temp_font, black, 100, 675)
        if iteration == 7:
            DwayneIntro.draw(DISPLAYSURF)
            AidenIntro.draw(DISPLAYSURF)
            FredIntro.draw(DISPLAYSURF)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore6, 100, 675) if not Lore6.displayed else draw_text(Lore6.text, temp_font, black, 100, 675)
        if iteration == 8:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore7, 100, 675) if not Lore7.displayed else draw_text(Lore7.text, temp_font, black, 100, 675)
        if iteration == 9:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore8, 100, 675) if not Lore8.displayed else draw_text(Lore8.text, temp_font, black, 100, 675)
        if iteration == 10:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore9, 100, 675) if not Lore9.displayed else draw_text(Lore9.text, temp_font, black, 100, 675)
        if iteration == 11:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore10, 100, 675) if not Lore10.displayed else draw_text(Lore10.text, temp_font, black, 100, 675)
        if iteration == 12:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore11, 100, 675) if not Lore11.displayed else draw_text(Lore11.text, temp_font, black, 100, 675)
        if iteration == 13:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Lore12, 100, 675) if not Lore12.displayed else draw_text(Lore12.text, temp_font, black, 100, 675)
        if iteration == 14:
            break
        clock.tick(60)
        pygame.display.update()
    BossRush()

##### BOSS RUSH MODE #####
def BossRush():
    cont = 0
    buttonCooldown = False
    DISPLAYSURF.fill(white)
    DwayneIdle.draw(DISPLAYSURF)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(DwayneOpen0, 100, 675)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    cont += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            cont += 1
        if cont == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(DwayneOpen1, 100, 675) if not DwayneOpen1.displayed else draw_text(DwayneOpen1.text, temp_font, black, 100, 675)
        if cont == 2:
            break
        clock.tick(60)
        pygame.display.update()
    Battle(Dwayne, DwayneBattleScript, DwayneIdle, DwayneThrow, DwayneHurt, DwayneBlock, DwayneRock, DwaynePaper, DwayneScissors)

def Level2():
    buttonCooldown = False
    cont = 0
    DISPLAYSURF.fill(white)
    AidenIdle.draw(DISPLAYSURF)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(AidenOpen0, 100, 675)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    cont += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            cont += 1
        if cont == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(AidenOpen1, 100, 675) if not AidenOpen1.displayed else draw_text(AidenOpen1.text, temp_font, black, 100, 675)
        if cont == 2:
            break
        clock.tick(60)
        pygame.display.update()
    Battle(Aiden, AidenBattleScript, AidenIdle, AidenThrow, AidenHurt, AidenBlock, AidenRock, AidenPaper, AidenScissors)

def Level3():
    buttonCooldown = False
    cont = 0
    DISPLAYSURF.fill(white)
    FredIdle.draw(DISPLAYSURF)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(FredOpen0, 100, 675)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    cont += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            cont += 1
        if cont == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(FredOpen1, 100, 675) if not FredOpen1.displayed else draw_text(FredOpen1.text, temp_font, black, 100, 675)
        if cont == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(FredOpen2, 100, 675) if not FredOpen2.displayed else draw_text(FredOpen2.text, temp_font, black, 100, 675)
        if cont == 3:
            break
        clock.tick(60)
        pygame.display.update()
    Battle(Fred, FredBattleScript, FredIdle, FredThrow, FredHurt, FredBlock, FredRock, FredPaper, FredScissors)

def BossFight():
    buttonCooldown = False
    cont = 0
    DISPLAYSURF.fill(white)
    JoelIdle.draw(DISPLAYSURF)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(JoelOpen0, 100, 675)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    cont += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            cont += 1
        if cont == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(JoelOpen1, 100, 675) if not JoelOpen1.displayed else draw_text(JoelOpen1.text, temp_font, black, 100, 675)
        if cont == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(JoelOpen2, 100, 675) if not JoelOpen2.displayed else draw_text(JoelOpen2.text, temp_font, black, 100, 675)
        if cont == 3:
            break
        clock.tick(60)
        pygame.display.update()
    Battle(Joel, JoelBattleScript, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors)

def Battle(foe, script, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors):
    buttonCooldown = False
    DISPLAYSURF.fill(white)
    PlayerIdle.draw(DISPLAYSURF)
    FoeIdle.draw(DISPLAYSURF)
    GruntHealthBar3.draw(DISPLAYSURF) if foe.type != "boss" else None
    BossHealthBar5.draw(DISPLAYSURF) if foe.type == "boss" else None
    PlayerHealthBarFull.draw(DISPLAYSURF)
    draw_text(foe.name, temp_font, black, 1000, 70)
    draw_text("Player", temp_font, black, 325, 320)
    pygame.display.update()
    BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)

def ThrowHands(PlayerAction, FoeAction, pBlock, fBlock, draw, playerWon, enemyWon, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    buttonCooldown = False
    for i in range(0, 3):
        ##### ITERATION #####
        DISPLAYSURF.fill(white)
        PlayerThrow.draw(DISPLAYSURF)
        FoeThrow.draw(DISPLAYSURF)
        pygame.time.delay(500)
        pygame.display.update()
        DISPLAYSURF.fill(white)
        PlayerRock.draw(DISPLAYSURF)
        FoeRock.draw(DISPLAYSURF)
        pygame.time.delay(500)
        pygame.display.update()              
        DISPLAYSURF.fill(white)
    pygame.time.delay(1000)
    if draw:
        FoeRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
        FoePaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
        FoeScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
        FoeBlock.draw(DISPLAYSURF) if FoeAction == "Block" else None
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        PlayerBlockPic.draw(DISPLAYSURF) if PlayerAction == "Block" else None
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        BattleDraw.draw(DISPLAYSURF)
        pygame.display.update()
        pygame.time.delay(1500)
    elif PlayerAction == "Block" and not draw:
        if pBlock:
            PlayerBlockPic.draw(DISPLAYSURF)
            FoeRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
            FoePaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
            FoeScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
            BattleSelectionMenu3.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
            BagButton.draw(DISPLAYSURF)
            PlayerBlocked.draw(DISPLAYSURF)
            pygame.display.update()
            pygame.time.delay(1500)
        elif not pBlock:
            PlayerHurt.draw(DISPLAYSURF)
            FoeRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
            FoePaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
            FoeScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
            BattleSelectionMenu3.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
            BagButton.draw(DISPLAYSURF)
            PlayerBlockFailed.draw(DISPLAYSURF)
            pygame.display.update()
            pygame.time.delay(1500)
    elif fBlock and not draw:
        FoeBlock.draw(DISPLAYSURF)
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        EnemyBlocked.draw(DISPLAYSURF)
        pygame.display.update()
        pygame.time.delay(1500)
    else:
        FoeRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
        FoePaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
        FoeScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
        PlayerRock.draw(DISPLAYSURF) if PlayerAction == "Rock" else None
        PlayerPaper.draw(DISPLAYSURF) if PlayerAction == "Paper" else None
        PlayerScissors.draw(DISPLAYSURF) if PlayerAction == "Scissors" else None
        pygame.time.delay(1500)
        if playerWon:
            FoeHurt.draw(DISPLAYSURF)
        if enemyWon:
            PlayerHurt.draw(DISPLAYSURF)
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        WonRound.draw(DISPLAYSURF) if playerWon else None
        LostRound.draw(DISPLAYSURF) if enemyWon else None
        pygame.display.update()
        pygame.time.delay(1500)
    DISPLAYSURF.fill(white)
    PlayerIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    FoeIdle.draw(DISPLAYSURF)
    if draw:
        SlowText2(script[0], 100, 675)
    elif PlayerAction == "Block":
        if pBlock:
            SlowText2(script[randint(4, 6)], 100, 675)
        elif not pBlock:
            SlowText2(script[randint(1, 3)], 100, 675)
    elif fBlock:
        SlowText2(script[7], 100, 675)
    elif not draw and PlayerAction != "Block" and not fBlock:
        if playerWon:
            SlowText2(script[randint(4, 6)], 100, 675)
        if enemyWon:
            SlowText2(script[randint(1, 3)], 100, 675)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            break
        clock.tick(60)
        pygame.display.update()
            
def HealedResult(foe, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    buttonCooldown = False
    if player.health + 3 > 7:
        player.health = 7
    else:
        player.health += 3
    for i in range(0, 3):
        ##### ITERATION #####
        DISPLAYSURF.fill(white)
        PlayerIdle.draw(DISPLAYSURF)
        FoeThrow.draw(DISPLAYSURF)
        pygame.time.delay(500)
        pygame.display.update()
        DISPLAYSURF.fill(white)
        PlayerIdle.draw(DISPLAYSURF)
        FoeRock.draw(DISPLAYSURF)
        pygame.time.delay(500)
        pygame.display.update()              
        DISPLAYSURF.fill(white)
    FoeAction = foe.action()
    player.bandAids -= 1
    PlayerIdle.draw(DISPLAYSURF)
    if FoeAction != "Block":
        FoeRock.draw(DISPLAYSURF) if FoeAction == "Rock" else None
        FoePaper.draw(DISPLAYSURF) if FoeAction == "Paper" else None
        FoeScissors.draw(DISPLAYSURF) if FoeAction == "Scissors" else None
        player.health -= 1
    FoeBlock.draw(DISPLAYSURF) if FoeAction == "Block" else None
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        clock.tick(60)
        pygame.display.update()

def BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    buttonCooldown = False
    DISPLAYSURF.fill(white)
    PlayerIdle.draw(DISPLAYSURF)
    FoeIdle.draw(DISPLAYSURF)
    PlayerAction = ""
    FoeAction = ""
    SelectMenuButtons = [AttackButton, BlockButton, BagButton]
    BossHealthBar = [BossHealthBar0, BossHealthBar1, BossHealthBar2, BossHealthBar3, BossHealthBar4, BossHealthBar5]
    GruntHealthBar = [GruntHealthBar0, GruntHealthBar1, GruntHealthBar2, GruntHealthBar3]
    BattleSelectionMenu3.draw(DISPLAYSURF)
    AttackButton.draw(DISPLAYSURF)
    BagButton.draw(DISPLAYSURF)
    BlockButton.draw(DISPLAYSURF)
    BossHealthBar[foe.health].draw(DISPLAYSURF) if foe.type == "boss" else None
    GruntHealthBar[foe.health].draw(DISPLAYSURF) if foe.type != "boss" else None
    PlayerHealthBar[player.health].draw(DISPLAYSURF)
    draw_text(foe.name, temp_font, black, 1000, 70)
    draw_text("Player", temp_font, black, 325, 220)
    pygame.display.update()
    while True:
        BattleSelectionMenu3.draw(DISPLAYSURF)
        AttackButton.draw(DISPLAYSURF)
        BagButton.draw(DISPLAYSURF)
        BlockButton.draw(DISPLAYSURF)
        draw_text(foe.name, temp_font, black, 1125, 70)
        draw_text("Player", temp_font, black, 325, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key in menuCycleLeftUp and not buttonCooldown:
                    ChangingButtons(SelectMenuButtons, -1)
                    buttonCooldown = True
                if event.key in menuCycleRightDown and not buttonCooldown:
                    ChangingButtons(SelectMenuButtons, 1)
                    buttonCooldown = True
                if event.key == pygame.K_RETURN and not buttonCooldown and AttackButton.selected:
                    if AttackButton.action():
                        BattleAttackMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and not buttonCooldown and BlockButton.selected:
                    PlayerAction = "Block"
                    FoeAction = foe.action()
                    RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and not buttonCooldown and BagButton.selected:
                    if BagButton.action:
                        BattleBagMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(SelectMenuButtons, 1)
            pygame.time.delay(500)
        if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(SelectMenuButtons, -1)
            pygame.time.delay(500)
        if (GPIO.input(UpButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        if (GPIO.input(DownButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        ##### Controller Select Buttons
        if (GPIO.input(SelectButton) == GPIO.HIGH) and AttackButton.selected:
            BattleAttackMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        if (GPIO.input(SelectButton) == GPIO.HIGH) and BlockButton.selected:
            PlayerAction = "Block"
            FoeAction = foe.action()
            RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        if (GPIO.input(SelectButton) == GPIO.HIGH) and BagButton.selected:
            BattleBagMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)

        if foe.type != "boss":
            GruntHealthBar[foe.health].draw(DISPLAYSURF)
            if foe.health == 0:
                if foe.name == "Dwayne":
                    SpeechBox.draw(DISPLAYSURF)
                    SlowText2(DwayneLoseBattle, 100, 675)
                    pygame.time.delay(2000)
                    Level2()
                if foe.name == "Aiden":
                    SpeechBox.draw(DISPLAYSURF)
                    SlowText2(AidenLoseBattle, 100, 675)
                    pygame.time.delay(2000)
                    Level3()
                if foe.name == "Fred":
                    SpeechBox.draw(DISPLAYSURF)
                    SlowText2(FredLoseBattle, 100, 675)
                    pygame.time.delay(2000)
                    BossFight()
        if foe.type == "boss":
            BossHealthBar[foe.health].draw(DISPLAYSURF)
            if foe.health == 1:
                Phase2(foe, turn)
        if player.health == 0:
            if foe.name == "Dwayne":
                LoseGame(DwayenWinBattle)
            if foe.name == "Aiden":
                LoseGame(AidenWinBattle)
            if foe.name == "Fred":
                LoseGame(FredWinBattle)
            if foe.name == "Joel":
                LoseGame(JoelWinBattle)
        PlayerHealthBar[player.health].draw(DISPLAYSURF)
        draw_text(foe.name, temp_font, black, 1125, 70)
        draw_text("Player", temp_font, black, 325, 220)
        clock.tick(60)
        pygame.display.update()

def BattleBagMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    pygame.time.delay(500)
    buttonCooldown = FalsebuttonCooldown = False
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
                        BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and not buttonCooldown and BandAid.selected:
                    if player.health == 7:
                        SpeechBox.draw(DISPLAYSURF)
                        SlowText2("There's no point, you are at full HP.", 100, 675)

                    elif BandAid.action():
                        FoeAction = foe.action
                        HealedResult(foe, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(BagButtons, 1)
            pygame.time.delay(500)
        if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(BagButtons, -1)
            pygame.time.delay(500)
        if (GPIO.input(UpButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        if (GPIO.input(DownButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        ##### Controller Select Buttons
        if (GPIO.input(SelectButton) == GPIO.HIGH) and BandAid.selected:
            if player.health == 7:
                SpeechBox.draw(DISPLAYSURF)
                SlowText2("There's no point, you are at full HP.", 100, 675)

            elif BandAid.action():
                FoeAction = foe.action
                HealedResult(foe, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        if (GPIO.input(SelectButton) == GPIO.HIGH) and BagMenuBackButton.selected:
            BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        BandAid.image = BandAidImg[player.bandAids]
        BandAid.imgHover = BandAidImgSelected[player.bandAids]
        clock.tick(60)
        pygame.display.update()
        
def BattleAttackMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    buttonCooldown = False
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
                        RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                        pygame.time.delay(500)
                        BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and PaperButton.selected and not buttonCooldown:
                    if PaperButton.action():
                        PlayerAction = "Paper"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                        pygame.time.delay(500)
                        BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and ScissorsButton.selected and not buttonCooldown:
                    if ScissorsButton.action():
                        PlayerAction = "Scissors"
                        FoeAction = foe.action()
                        RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                        pygame.time.delay(500)
                        BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
                if event.key == pygame.K_RETURN and BackButton.selected and not buttonCooldown:
                    if BackButton.action:
                        pygame.time.delay(500)
                        BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        ##### Controller Input
        if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(AttackButtons, 1)
            pygame.time.delay(500)
        if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
            buttonCooldown = True
            ChangingButtons(AttackButtons, -1)
            pygame.time.delay(500)
        if (GPIO.input(UpButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        if (GPIO.input(DownButton) == GPIO.LOW) and buttonCooldown:
            buttonCooldown = False
        ##### Controller Select Buttons
        if (GPIO.input(SelectButton) == GPIO.HIGH) and RockButton.selected:
            PlayerAction = "Rock"
            FoeAction = foe.action()
            RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.time.delay(500)
           
        if (GPIO.input(SelectButton) == GPIO.HIGH) and PaperButton.selected:
            PlayerAction = "Paper"
            FoeAction = foe.action()
            RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.time.delay(500)
            BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)

        if (GPIO.input(SelectButton) == GPIO.HIGH) and ScissorsButton.selected:
            PlayerAction = "Scissors"
            FoeAction = foe.action()
            RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.time.delay(500)
            BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)

        if (GPIO.input(SelectButton) == GPIO.HIGH) and BackButton.selected:
            pygame.time.delay(500)
            BattleSelectMenu(foe, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        
        pygame.display.update()
        clock.tick(60)

def RoundResults(foe, PlayerAction, FoeAction, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script):
    buttonCooldown = False
    if PlayerAction == "Heal":
        HealedResult(FoeAction)
        pygame.display.update()
    elif PlayerAction == FoeAction:
        ThrowHands(PlayerAction, FoeAction, False, False, True, False, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
    elif PlayerAction == "Block":
        blockChance = randint(1, 10)
        if blockChance > 1:
            ThrowHands(PlayerAction, FoeAction, True, False, False, False, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.display.update()
        elif blockChance == 1:
            ThrowHands(PlayerAction, FoeAction, False, True, False, False, True, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.display.update()
            player.health -= 1
            pygame.display.update()
        elif FoeAction == "Block":
            ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
            pygame.display.update()

    ##### PLAYER CHOOSE ROCK #####
    elif PlayerAction == "Rock" and FoeAction == "Paper":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        player.health -= 1
    elif PlayerAction == "Rock" and FoeAction == "Scissors":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
        foe.health -= 1
        
    ##### PLAYER CHOOSE PAPER #####
    elif PlayerAction == "Paper" and FoeAction == "Scissors":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
        player.health -= 1
    elif PlayerAction == "Paper" and FoeAction == "Rock":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
        foe.health -= 1

    ##### PLAYER CHOOSE SCISSORS #####
    elif PlayerAction == "Scissors" and FoeAction == "Rock":
        ThrowHands(PlayerAction, FoeAction, False, False, False, False, True, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
        player.health -= 1
    elif PlayerAction == "Scissors" and FoeAction == "Paper":
        ThrowHands(PlayerAction, FoeAction, False, False, False, True, False, FoeIdle, FoeThrow, FoeHurt, FoeBlock, FoeRock, FoePaper, FoeScissors, script)
        pygame.display.update()
        foe.health -= 1
    pygame.time.delay(1000)

def Phase2(boss, turn):
    buttonCooldown = False
    DISPLAYSURF.fill(white)
    PlayerIdle.draw(DISPLAYSURF)
    JoelIdle.draw(DISPLAYSURF)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(Finale0, 100, 675)
    pygame.time.delay(1000)
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(Finale1.text, 100, 675)
    pygame.time.delay(1000)
    SelectButtons = [AttackButton, BlockButton]
    AttackButtons = [RockButton, PaperButton, ScissorsButton, BackButton]
    FinaleButtons = [MysteryItemButton, BackButtonFinale]
    menu = "select"
    PlayerAction = ""
    FoeAction = ""
    PlayerHealthBar[player.health].draw(DISPLAYSURF)
    BossHealthBar1.draw(DISPLAYSURF)
    draw_text(boss.name, temp_font, black, 1125, 70)
    draw_text("Player", temp_font, black, 325, 220)
    pygame.display.update()
    while True:
        if menu == "select":
            BattleSelectionMenu2.draw(DISPLAYSURF)
            AttackButton.draw(DISPLAYSURF)
            BlockButton.draw(DISPLAYSURF)
        if menu == "attack":
            if turn < 3:
                BattleSelectionMenu.draw(DISPLAYSURF)
                RockButton.draw(DISPLAYSURF)
                PaperButton.draw(DISPLAYSURF)
                ScissorsButton.draw(DISPLAYSURF)
                BackButton.draw(DISPLAYSURF)
            if turn >= 3:
                BattleSelectionMenu2.draw(DISPLAYSURF)
                MysteryItemButton.draw(DISPLAYSURF)
                BackButtonFinale.draw(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                buttonCooldown = False
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if menu == "select":
                    if event.key in menuCycleRightDown and not buttonCooldown:
                        ChangingButtons(SelectButtons, 1)
                        buttonCooldown = True
                    if event.key in menuCycleLeftUp and not buttonCooldown:
                        ChangingButtons(SelectButtons, -1)
                    if event.key == pygame.K_RETURN:
                        if AttackButton.selected and not buttonCooldown:
                            buttonCooldown = True
                            menu = "attack"
                        if BlockButton.selected and not buttonCooldown:
                            if turn == 3:
                                SpeechBox.draw(DISPLAYSURF)
                                SlowText2("You should really just finish the fight, lunch is about to start!", 100, 675)
                                pygame.time.delay(1000)
                            else:
                                buttonCooldown = True
                                PlayerAction = "Block"
                                FoeAction = "Block"
                                turn += 1
                                ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
                if menu == "attack" and turn < 3:
                    if event.key in menuCycleRightDown and not buttonCooldown:
                        ChangingButtons(AttackButtons, 1)
                        buttonCooldown = True
                    if event.key in menuCycleLeftUp and not buttonCooldown:
                        ChangingButtons(AttackButtons, -1)
                    if event.key == pygame.K_RETURN:
                        if BackButton.selected and not buttonCooldown:
                            buttonCooldown = True
                            menu = "select"
                        if RockButton.selected and not buttonCooldown:
                            buttonCooldown = True
                            PlayerAction = "Rock"
                            FoeAction = "Rock"
                            turn += 1
                            ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
                            menu = "select"
                        if PaperButton.selected and not buttonCooldown:
                            buttonCooldown = True
                            PlayerAction = "Paper"
                            FoeAction = "Paper"
                            turn += 1
                            ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
                            menu = "select"
                        if ScissorsButton.selected and not buttonCooldown:
                            buttonCooldown = True
                            PlayerAction = "Scissors"
                            FoeAction = "Scissors"
                            turn += 1
                            ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
                            menu = "select"
                if menu == "attack" and turn >= 3:
                    if event.key in menuCycleRightDown and not buttonCooldown:
                        ChangingButtons(FinaleButtons, 1)
                        buttonCooldown = True
                    if event.key in menuCycleLeftUp and not buttonCooldown:
                        ChangingButtons(FinaleButtons, -1)
                    if event.key == pygame.K_RETURN:
                        if BackButtonFinale.selected and not buttonCooldown:
                            buttonCooldown = True
                            menu = "select"
                        if MysteryItemButton.selected and not buttonCooldown:
                            Finale()
        if menu == "select":
            ##### Controller Select Buttons
            if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(SelectButtons, 1)
                pygame.time.delay(500)
           
            if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(SelectButtons, -1)
                pygame.time.delay(500)

            if (GPIO.input(UpButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False
           
            if (GPIO.input(DownButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False

            if (GPIO.input(SelectButton) == GPIO.HIGH) and AttackButton.selected:
                buttonCooldown = False
                menu = "attack"
               
            if (GPIO.input(SelectButton) == GPIO.HIGH) and BlockButton.selected:
                if turn == 3:
                    SpeechBox.draw(DISPLAYSURF)
                    SlowText2("You should really just finish the fight, lunch is about to start!", 100, 675)
                    pygame.time.delay(1000)
                else:
                    buttonCooldown = True
                    PlayerAction = "Block"
                    FoeAction = "Block"
                    turn += 1
                    ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
        if menu == "attack" and turn != 3:
             ##### Controller Select Buttons
            if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(AttackButtons, 1)
                pygame.time.delay(500)
           
            if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(AttackButtons, -1)
                pygame.time.delay(500)

            if (GPIO.input(UpButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False
           
            if (GPIO.input(DownButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False

            if (GPIO.input(SelectButton) == GPIO.HIGH) and RockButton.selected:
                buttonCooldown = True
                PlayerAction = "Rock"
                FoeAction = "Rock"
                turn += 1
                ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)

            if (GPIO.input(SelectButton) == GPIO.HIGH) and PaperButton.selected:
                buttonCooldown = True
                PlayerAction = "Paper"
                FoeAction = "Paper"
                turn += 1
                ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)

            if (GPIO.input(SelectButton) == GPIO.HIGH) and ScissorsButton.selected:
                buttonCooldown = True
                PlayerAction = "Scissors"
                FoeAction = "Scissors"
                turn += 1
                ThrowHands(PlayerAction, FoeAction, False, False, False, False, False, JoelIdle, JoelThrow, JoelHurt, JoelBlock, JoelRock, JoelPaper, JoelScissors, JoelBattleScript)
            
            if (GPIO.input(SelectButton) == GPIO.HIGH) and BackButton.selected:
                buttonCooldown = True
                menu = "select"

        if menu == "attack" and turn >= 3:
             ##### Controller Select Buttons
            if (GPIO.input(UpButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(FinaleButtons, 1)
                pygame.time.delay(500)
           
            if (GPIO.input(DownButton) == GPIO.HIGH) and not buttonCooldown:
                buttonCooldown = True
                ChangingButtons(FinaleButtons, -1)
                pygame.time.delay(500)

            if (GPIO.input(UpButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False
           
            if (GPIO.input(DownButton) == GPIO.LOW) and not buttonCooldown:
                buttonCooldown = False

            if (GPIO.input(SelectButton) == GPIO.HIGH) and BackButton.selected:
                buttonCooldown = True
                menu = "select"

            if (GPIO.input(SelectButton) == GPIO.HIGH) and MysteryItemButton.selected:
                Finale()

        if turn == 1 and not Finale2.displayed:
            FinaleBanterTurn1()
        if turn == 2 and not Finale5.displayed:
            FinaleBanterTurn2()
        if turn == 3 and not Finale8.displayed:
            FinaleBanterTurn3()
        clock.tick(60)
        pygame.display.update()

def FinaleBanterTurn1():
    buttonCooldown = False
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale2, 100, 675) if not Finale2.displayed else draw_text(Finale2.text, temp_font, black, 100, 675)
        if count == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale3, 100, 675) if not Finale3.displayed else draw_text(Finale3.text, temp_font, black, 100, 675)
        if count == 3:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale4, 100, 675) if not Finale4.displayed else draw_text(Finale4.text, temp_font, black, 100, 675)
        if count == 4:
            break
        clock.tick(60)
        pygame.display.update()

def FinaleBanterTurn2():
    buttonCooldown = False
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale5, 100, 675) if not Finale5.displayed else draw_text(Finale5.text, temp_font, black, 100, 675)
        if count == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale6, 100, 675) if not Finale6.displayed else draw_text(Finale6.text, temp_font, black, 100, 675)
        if count == 3:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale7, 100, 675) if not Finale7.displayed else draw_text(Finale7.text, temp_font, black, 100, 675)
        if count == 4:
            break
        clock.tick(60)
        pygame.display.update()

def FinaleBanterTurn3():
    buttonCooldown = False
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale8, 100, 675) if not Finale8.displayed else draw_text(Finale8.text, temp_font, black, 100, 675)
        if count == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale9, 100, 675) if not Finale9.displayed else draw_text(Finale9.text, temp_font, black, 100, 675)
        if count == 3:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale10, 100, 675) if not Finale10.displayed else draw_text(Finale10.text, temp_font, black, 100, 675)
        if count == 4:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale11, 100, 675) if not Finale11.displayed else draw_text(Finale11.text, temp_font, black, 100, 675)
        if count == 5:
            break
        clock.tick(60)
        pygame.display.update()

def Finale():
    buttonCooldown = False
    for i in range(0, 3):
        DISPLAYSURF.fill(white)
        PlayerThrow.draw(DISPLAYSURF)
        JoelThrow.draw(DISPLAYSURF)
        pygame.display.update()
        pygame.time.delay(500)
        DISPLAYSURF.fill(white)
        PlayerRock.draw(DISPLAYSURF)
        JoelRock.draw(DISPLAYSURF)
        pygame.display.update()
        pygame.time.delay(500)
        DISPLAYSURF.fill(white)
        pygame.time.delay(500)
    PlayerMysteryItem.draw(DISPLAYSURF)
    JoelShock.draw(DISPLAYSURF)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            DwayneIntro.draw(DISPLAYSURF)
            AidenIntro.draw(DISPLAYSURF)
            FredIntro.draw(DISPLAYSURF)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale12, 100, 675) if not Finale12.displayed else draw_text(Finale12.text, temp_font, black, 100, 675)
        if count == 2:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale13, 100, 675) if not Finale13.displayed else draw_text(Finale13.text, temp_font, black, 100, 675)
        if count == 3:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale14, 100, 675) if not Finale14.displayed else draw_text(Finale14.text, temp_font, black, 100, 675)
        if count == 4:
            DISPLAYSURF.fill(white)
            DwayneIntro.draw(DISPLAYSURF)
            AidenIntro.draw(DISPLAYSURF)
            FredIntro.draw(DISPLAYSURF)
            JoelIdle.draw(DISPLAYSURF)
            PlayerIdle.draw(DISPLAYSURF)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale15, 100, 675) if not Finale15.displayed else draw_text(Finale15.text, temp_font, black, 100, 675)
        if count == 5:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale16, 100, 675) if not Finale16.displayed else draw_text(Finale16.text, temp_font, black, 100, 675)
        if count == 6:
            SpeechBox.draw(DISPLAYSURF)
            SlowText(Finale17, 100, 675) if not Finale17.displayed else draw_text(Finale17.text, temp_font, black, 100, 675)
        if count == 7:
            break
        clock.tick(60)
        pygame.display.update()
    WinGame(GameWon)
#need a change to commit nahudjkawbksjBDkjsAJKDASJ
def LoseGame(script):
    buttonCooldown = False
    SpeechBox.draw(DISPLAYSURF)
    SlowText2(script, 100, 675)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            DISPLAYSURF.fill(black)
            SpeechBox.draw(DISPLAYSURF)
            SlowText(GameOver, 100, 675) if not GameOver.displayed else draw_text(GameOver.text, temp_font, black, 100, 675)
        if count == 2:
            break
        clock.tick(60)
        pygame.display.update()
    Reset()

def WinGame(script):
    buttonCooldown = False
    DISPLAYSURF.fill(black)
    SpeechBox.draw(DISPLAYSURF)
    SlowText(script, 100, 675)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            break
        clock.tick(60)
        pygame.display.update()
    Reset()

def Credits():
    buttonCooldown = False
    credits.draw(DISPLAYSURF)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
                if event.key != pygame.K_ESCAPE:
                    count += 1
        if (GPIO.input(UpButton) == GPIO.HIGH) or (GPIO.input(DownButton) == GPIO.HIGH) or (GPIO.input(SelectButton) == GPIO.HIGH):
            count += 1
        if count == 1:
            break
        clock.tick(60)
        pygame.display.update()
    StartMenu()

def Reset():
    player.health = 7
    player.bandAids = 5
    Dwayne.health = 3
    Aiden.health = 3
    Fred.health = 3
    Joel.health = 5
    Credits()

StartMenu()
