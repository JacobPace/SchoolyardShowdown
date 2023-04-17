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
AttackButton = Button("Attack", 790, 785, attackImg, attackImgSelected, 1.01, True)

runImg = pygame.image.load('images/RunButton.png').convert_alpha()
runImgSelected = pygame.image.load('images/RunButtonSelected.png').convert_alpha()
RunButton = Button("Run", 1311, 785, runImg, runImgSelected, 1.01, False)

bagImg = pygame.image.load('images/BagButton.png').convert_alpha()
bagImgSelected = pygame.image.load('images/BagButtonSelected.png').convert_alpha()
BagButton = Button("Bag", 788, 880, bagImg, bagImgSelected, 1.01, False)

blockImg = pygame.image.load('images/BlockButton.png').convert_alpha()
blockImgSelected = pygame.image.load('images/BlockButtonSelected.png').convert_alpha()
BlockButton = Button("Block", 1311, 880, blockImg, blockImgSelected, 1.01, False)

##### ATTACK MENU BUTTONS #####
rockImg = pygame.image.load('images/RockButton.png').convert_alpha()
rockImgSelected = pygame.image.load('images/RockButtonSelected.png').convert_alpha()
RockButton = Button("Rock", 788, 785, rockImg, rockImgSelected, 1.01, True)

paperImg = pygame.image.load('images/PaperButton.png').convert_alpha()
paperImgSelected = pygame.image.load('images/PaperButtonSelected.png').convert_alpha()
PaperButton = Button("Paper", 1311, 785, paperImg, paperImgSelected, 1.01, False)

scissorsImg = pygame.image.load('images/ScissorsButton.png').convert_alpha()
scissorsImgSelected = pygame.image.load('images/ScissorsButtonSelected.png').convert_alpha()
ScissorsButton = Button("Scissors", 788, 880, scissorsImg, scissorsImgSelected, 1.01, False)

backImg = pygame.image.load('images/BackBattleButton.png').convert_alpha()
backImgSelected = pygame.image.load('images/BackBattleButtonSelected.png').convert_alpha()
BackButton = Button("Back", 1309, 880, backImg, backImgSelected, 1.01, False)

##### IMAGE TO DISPLAY DIALOGUE ON #####
textBoxImg = pygame.image.load('images/TextBox.png').convert_alpha()
TextBox = Image(0, 750, textBoxImg, 1)

BattleSelectionMenuBoxImg = pygame.image.load('images/BattleSelectionMenu.png').convert_alpha()
BattleSelectionMenu = Image(0, 750, BattleSelectionMenuBoxImg, 1)

SpeechBoxImg = pygame.image.load('images/SpeechBox.png').convert_alpha()
SpeechBox = Image(0, 750, SpeechBoxImg, 1)

BattleDrawImg = pygame.image.load('images/BattleDraw.png').convert_alpha()
BattleDraw = Image(190, 828, BattleDrawImg, 1)

LostBattleImg = pygame.image.load('images/PlayerBattleLost.png').convert_alpha()
LostBattle = Image(190, 828, LostBattleImg, 1)

WonBattleImg = pygame.image.load('images/PlayerBattleWon.png').convert_alpha()
WonBattle = Image(190, 828, WonBattleImg, 1)

WonRoundImg = pygame.image.load('images/PlayerRoundWon.png').convert_alpha()
WonRound = Image(190, 828, WonRoundImg, 1)

LostRoundImg = pygame.image.load('images/PlayerRoundLost.png').convert_alpha()
LostRound = Image(190, 828, LostRoundImg, 1)

PlayerBlockedImg = pygame.image.load('images/PlayerBlocked.png').convert_alpha()
PlayerBlock = Image(190, 828, PlayerBlockedImg, 1)

EnemyBlockedImg = pygame.image.load('images/EnemyBlocked.png').convert_alpha()