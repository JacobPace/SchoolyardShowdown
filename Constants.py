import pygame
from game import *
pygame.init()

WIDTH = 1920
HEIGHT = 1000
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # FPS controller
results = (None, None)
PlayerAction = None
FoeAction = None
##### START MENU #####
start_img = pygame.image.load('images/StartButton.png').convert_alpha()
start_hover = pygame.image.load('images/StartButtonSelected.png').convert_alpha()
start_button = Button("Start Button", 50, 100, start_img, start_hover, 0.2, True)

exit_img = pygame.image.load('images/ExitButton.png').convert_alpha()
exit_hover = pygame.image.load('images/ExitButtonSelected.png').convert_alpha()
exit_button = Button("Exit Button", 50, 250, exit_img, exit_hover, 3, False)

options_img = pygame.image.load('images/OptionsButton.png').convert_alpha()
options_hover = pygame.image.load('images/OptionsButtonSelected.png').convert_alpha()
options_button = Button("Options Button", 50, 400, options_img, options_hover, 3, False)

##### OPTIONS MENU #####
back_img = pygame.image.load('images/BackButton.png').convert_alpha()
back_hover = pygame.image.load('images/BackButtonSelected.png').convert_alpha()
back_button = Button("Back Button", 50, 500 , back_img, back_hover, 3, True)

exit_button2 = Button("Options Menu Exit Button", 295, 500, exit_img, exit_hover, 3, False)

##### BATTLE SELECTION DISPLAYSURF BUTTONS #####
attackImg = pygame.image.load('images/AttackMenuButton.png').convert_alpha()
attackImgSelected = pygame.image.load('images/AttackMenuButtonSelected.png').convert_alpha()
AttackButton = Button("Attack", 150, 775, attackImg, attackImgSelected, 1, True)

runImg = pygame.image.load('images/RunButton.png').convert_alpha()
runImgSelected = pygame.image.load('images/RunButtonSelected.png').convert_alpha()
RunButton = Button("Run", 275, 775, runImg, runImgSelected, 1, False)

bagImg = pygame.image.load('images/BagButton.png').convert_alpha()
bagImgSelected = pygame.image.load('images/BagButtonSelected.png').convert_alpha()
BagButton = Button("Bag", 375, 775, bagImg, bagImgSelected, 1, False)

##### ATTACK MENU BUTTONS #####
rockImg = pygame.image.load('images/RockButton.png').convert_alpha()
rockImgSelected = pygame.image.load('images/RockButtonSelected.png').convert_alpha()
RockButton = Button("Rock", 175, 775, rockImg, rockImgSelected, 1, True)

paperImg = pygame.image.load('images/PaperButton.png').convert_alpha()
paperImgSelected = pygame.image.load('images/PaperButtonSelected.png').convert_alpha()
PaperButton = Button("Paper", 275, 775, paperImg, paperImgSelected, 1, False)

scissorsImg = pygame.image.load('images/ScissorsButton.png').convert_alpha()
scissorsImgSelected = pygame.image.load('images/ScissorsButtonSelected.png').convert_alpha()
ScissorsButton = Button("Scissors", 375, 775, scissorsImg, scissorsImgSelected, 1, False)

blockImg = pygame.image.load('images/BlockButton.png').convert_alpha()
blockImgSelected = pygame.image.load('images/BlockButtonSelected.png').convert_alpha()
BlockButton = Button("Block", 475, 775, blockImg, blockImgSelected, 1, False)

backImg = pygame.image.load('images/BackBattleButton.png').convert_alpha()
backImgSelected = pygame.image.load('images/BackBattleButtonSelected.png').convert_alpha()
BackButton = Button("Back", 575, 775, backImg, backImgSelected, 1, False)

##### IMAGE TO DISPLAY DIALOGUE ON #####
textBoxImg = pygame.image.load('images/TextBox.png').convert_alpha()
TextBox = Image(0, 750, textBoxImg, 1)