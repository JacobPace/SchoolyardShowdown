import pygame
from game import *
import math
pygame.init()

WIDTH = 1920
HEIGHT = 1000
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # FPS controller
results = (None, None)
PlayerAction = None
FoeAction = None

##### IMAGES/BUTTONS #####

bg = pygame.image.load('images/StartMenuBackground.png').convert_alpha()
tiles = math.ceil(WIDTH/ bg.get_width()) + 1
##### START MENU #####
start_img = pygame.image.load('images/StartMenuButtons/StartButton.png').convert_alpha()
start_hover = pygame.image.load('images/StartMenuButtons/StartButtonSelected.png').convert_alpha()
start_button = Button(50, 100, start_img, start_hover, 0.2, True)

exit_img = pygame.image.load('images/StartMenuButtons/ExitButton.png').convert_alpha()
exit_hover = pygame.image.load('images/StartMenuButtons/ExitButtonSelected.png').convert_alpha()
exit_button = Button(50, 250, exit_img, exit_hover, 3, False)

options_img = pygame.image.load('images/StartMenuButtons/OptionsButton.png').convert_alpha()
options_hover = pygame.image.load('images/StartMenuButtons/OptionsButtonSelected.png').convert_alpha()
options_button = Button(50, 400, options_img, options_hover, 3, False)

##### OPTIONS MENU #####
back_img = pygame.image.load('images/OptionsMenuButtons/BackButton.png').convert_alpha()
back_hover = pygame.image.load('images/OptionsMenuButtons/BackButtonSelected.png').convert_alpha()
back_button = Button(50, 500 , back_img, back_hover, 3, True)

exit_button2 = Button(295, 500, exit_img, exit_hover, 3, False)

##### BATTLE SELECTION DISPLAYSURF BUTTONS #####
attackImg = pygame.image.load('images/BattleSelectionMenuButtons/AttackMenuButton.png').convert_alpha()
attackImgSelected = pygame.image.load('images/BattleSelectionMenuButtons/AttackMenuButtonSelected.png').convert_alpha()
AttackButton = Button(790, 785, attackImg, attackImgSelected, 1.01, True)

#runImg = pygame.image.load('images/RunButton.png').convert_alpha()
#runImgSelected = pygame.image.load('images/RunButtonSelected.png').convert_alpha()
#RunButton = Button(1311, 785, runImg, runImgSelected, 1.01, False)

bagImg = pygame.image.load('images/BattleSelectionMenuButtons/BagButton.png').convert_alpha()
bagImgSelected = pygame.image.load('images/BattleSelectionMenuButtons/BagButtonSelected.png').convert_alpha()
BagButton = Button(788, 880, bagImg, bagImgSelected, 1.01, False)

blockImg = pygame.image.load('images/BattleSelectionMenuButtons/BlockButton.png').convert_alpha()
blockImgSelected = pygame.image.load('images/BattleSelectionMenuButtons/BlockButtonSelected.png').convert_alpha()
BlockButton = Button(1311, 785, blockImg, blockImgSelected, 1.01, False)

##### ATTACK MENU BUTTONS #####
rockImg = pygame.image.load('images/BattleAttackMenuButtons/RockButton.png').convert_alpha()
rockImgSelected = pygame.image.load('images/BattleAttackMenuButtons/RockButtonSelected.png').convert_alpha()
RockButton = Button(788, 785, rockImg, rockImgSelected, 1.01, True)

paperImg = pygame.image.load('images/BattleAttackMenuButtons/PaperButton.png').convert_alpha()
paperImgSelected = pygame.image.load('images/BattleAttackMenuButtons/PaperButtonSelected.png').convert_alpha()
PaperButton = Button(1311, 785, paperImg, paperImgSelected, 1.01, False)

scissorsImg = pygame.image.load('images/BattleAttackMenuButtons/ScissorsButton.png').convert_alpha()
scissorsImgSelected = pygame.image.load('images/BattleAttackMenuButtons/ScissorsButtonSelected.png').convert_alpha()
ScissorsButton = Button(788, 880, scissorsImg, scissorsImgSelected, 1.01, False)

backImg = pygame.image.load('images/BattleAttackMenuButtons/BackBattleButton.png').convert_alpha()
backImgSelected = pygame.image.load('images/BattleAttackMenuButtons/BackBattleButtonSelected.png').convert_alpha()
BackButton = Button(1309, 880, backImg, backImgSelected, 1.01, False)

##### BAG MENU BUTTONS #####
BagMenuBackButton = Button(1309, 785, backImg, backImgSelected, 1.01, False)

BandAid5Img = pygame.image.load('images/BattleBagMenuButtons/BandageX5.png').convert_alpha()
BandAid5ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX5Selected.png').convert_alpha()

BandAid4Img = pygame.image.load('images/BattleBagMenuButtons/BandageX4.png').convert_alpha()
BandAid4ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX4Selected.png').convert_alpha()

BandAid3Img = pygame.image.load('images/BattleBagMenuButtons/BandageX3.png').convert_alpha()
BandAid3ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX3Selected.png').convert_alpha()

BandAid2Img = pygame.image.load('images/BattleBagMenuButtons/BandageX2.png').convert_alpha()
BandAid2ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX2Selected.png').convert_alpha()

BandAid1Img = pygame.image.load('images/BattleBagMenuButtons/BandageX1.png').convert_alpha()
BandAid1ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX1Selected.png').convert_alpha()

BandAid0Img = pygame.image.load('images/BattleBagMenuButtons/BandageX0.png').convert_alpha()
BandAid0ImgSelected = pygame.image.load('images/BattleBagMenuButtons/BandageX0Selected.png').convert_alpha()

BandAid = Button(788, 785, BandAid5Img, BandAid5ImgSelected, 1, True)



##### IMAGE TO DISPLAY DIALOGUE ON #####
textBoxImg = pygame.image.load('images/TextBox.png').convert_alpha()
TextBox = Image(0, 750, textBoxImg, 1)

BattleSelectionMenuBoxImg = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu.png').convert_alpha()
BattleSelectionMenu = Image(0, 750, BattleSelectionMenuBoxImg, 1)

BattleSelctionMenu3Img = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu3.png').convert_alpha()
BattleSelectionMenu3 = Image(0, 750, BattleSelctionMenu3Img, 1)

BattleSelctionMenu2Img = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu2.png').convert_alpha()
BattleSelectionMenu2 = Image(0, 750, BattleSelctionMenu2Img, 1)

SpeechBoxImg = pygame.image.load('images/SpeechBox.png').convert_alpha()
SpeechBox = Image(0, 750, SpeechBoxImg, 1)

##### BATTLE RESULTS #####
BattleDrawImg = pygame.image.load('images/BattleResults/BattleDraw.png').convert_alpha()
BattleDraw = Image(190, 828, BattleDrawImg, 1)

LostBattleImg = pygame.image.load('images/BattleResults/PlayerBattleLost.png').convert_alpha()
LostBattle = Image(190, 828, LostBattleImg, 1)

WonBattleImg = pygame.image.load('images/BattleResults/PlayerBattleWon.png').convert_alpha()
WonBattle = Image(190, 828, WonBattleImg, 1)

WonRoundImg = pygame.image.load('images/BattleResults/PlayerRoundWon.png').convert_alpha()
WonRound = Image(190, 828, WonRoundImg, 1)

LostRoundImg = pygame.image.load('images/BattleResults/PlayerRoundLost.png').convert_alpha()
LostRound = Image(190, 828, LostRoundImg, 1)

PlayerBlockedImg = pygame.image.load('images/BattleResults/PlayerBlocked.png').convert_alpha()
PlayerBlocked = Image(190, 828, PlayerBlockedImg, 1)

EnemyBlockedImg = pygame.image.load('images/BattleResults/EnemyBlocked.png').convert_alpha()
EnemyBlocked = Image(190, 828, EnemyBlockedImg, 1)

PlayerBlockedFailedImg = pygame.image.load('images/BattleResults/BlockFailed.png').convert_alpha()
PlayerBlockFailed = Image(190, 828, PlayerBlockedFailedImg, 1)

BlankResultImg = pygame.image.load('images/BattleResults/Blank.png').convert_alpha()
BlankResult = Image(190, 828, BlankResultImg, 1)

##### CHANGE PLAYER/ENEMY PICTURE IN FIGHT #####
# initalize the player/enemy for testing purposes
lil_dude = pygame.image.load('images/lil_dude.png').convert_alpha()
player = Player(100,100, lil_dude) # taken areguments are the default x,y coordinates

enemyImg = pygame.image.load('images/enemy.png').convert_alpha()
Ronald = Enemy("Ronald")
enemytest = Image(1500, 100, enemyImg, 10)



# Player battle images
PlayerStandingImg = pygame.image.load('images/PlayerActions/PlayerStanding.png').convert_alpha()
PlayerStanding = Image(100, 400, PlayerStandingImg, 5)

PlayerBlockImg = pygame.image.load('images/PlayerActions/PlayerBlock.png').convert_alpha()
PlayerBlockPic = Image(100, 400 ,PlayerBlockImg, 5)

PlayerRockImg = pygame.image.load('images/PlayerActions/PlayerRock.png').convert_alpha()
PlayerRock = Image(100, 400, PlayerRockImg, 5)

PlayerPaperImg = pygame.image.load('images/PlayerActions/PlayerPaper.png').convert_alpha()
PlayerPaper = Image(100, 400, PlayerPaperImg, 5)

PlayerScissorsImg = pygame.image.load('images/PlayerActions/PlayerScissors.png').convert_alpha()
PlayerScissors = Image(100, 400, PlayerScissorsImg, 5)

PlayerThrowImg = pygame.image.load('images/PlayerActions/PlayerThrow.png').convert_alpha()
PlayerThrow = Image(100, 400, PlayerThrowImg, 5)

# Enemy Test
EnemyBlockImg = pygame.image.load('images/EnemyBlock.png').convert_alpha()
EnemyBlockPic = Image(1500, 100 ,EnemyBlockImg, 10)

EnemyRockImg = pygame.image.load('images/EnemyRock.png').convert_alpha()
EnemyRock = Image(1500, 100, EnemyRockImg, 10)

EnemyPaperImg = pygame.image.load('images/EnemyPaper.png').convert_alpha()
EnemyPaper = Image(1500, 100, EnemyPaperImg, 10)

EnemyScissorsImg = pygame.image.load('images/EnemyScissors.png').convert_alpha()
EnemyScissors = Image(1500, 100, EnemyScissorsImg, 10)

EnemyThrowImg = pygame.image.load('images/EnemyThrow.png').convert_alpha()
EnemyThrow = Image(1500, 100, EnemyThrowImg, 10)

##### ENEMY HEALTH BAR #####
GruntHealthBar5Img = pygame.image.load('images/HealthBars/GruntHealthBar5.png').convert_alpha()
GruntHealthBar5 = Image(1100, 50, GruntHealthBar5Img, 2)

GruntHealthBar4Img = pygame.image.load('images/HealthBars/GruntHealthBar4.png').convert_alpha()
GruntHealthBar4 = Image(1100, 50, GruntHealthBar4Img, 2)

GruntHealthBar3Img = pygame.image.load('images/HealthBars/GruntHealthBar3.png').convert_alpha()
GruntHealthBar3 = Image(1100, 50, GruntHealthBar3Img, 2)

GruntHealthBar2Img = pygame.image.load('images/HealthBars/GruntHealthBar2.png').convert_alpha()
GruntHealthBar2 = Image(1100, 50, GruntHealthBar2Img, 2)

GruntHealthBar1Img = pygame.image.load('images/HealthBars/GruntHealthBar1.png').convert_alpha()
GruntHealthBar1 = Image(1100, 50, GruntHealthBar1Img, 2)

GruntHealthBar0Img = pygame.image.load('images/HealthBars/GruntHealthBar0.png').convert_alpha()
GruntHealthBar0 = Image(1100, 50, GruntHealthBar0Img, 2)

##### PLAYER HEALTH BAR #####
BigHealthBar7Img = pygame.image.load('images/HealthBars/BigHealthBar7.png').convert_alpha()
PlayerHealthBarFull  = Image(400, 300, BigHealthBar7Img, 2)

BigHealthBar6Img = pygame.image.load('images/HealthBars/BigHealthBar6.png').convert_alpha()
PlayerHealthBar6  = Image(400, 300, BigHealthBar6Img, 2)

BigHealthBar5Img = pygame.image.load('images/HealthBars/BigHealthBar5.png').convert_alpha()
PlayerHealthBar5  = Image(400, 300, BigHealthBar5Img, 2)

BigHealthBar4Img = pygame.image.load('images/HealthBars/BigHealthBar4.png').convert_alpha()
PlayerHealthBar4  = Image(400, 300, BigHealthBar4Img, 2)

BigHealthBar3Img = pygame.image.load('images/HealthBars/BigHealthBar3.png').convert_alpha()
PlayerHealthBar3  = Image(400, 300, BigHealthBar3Img, 2)

BigHealthBar2Img = pygame.image.load('images/HealthBars/BigHealthBar2.png').convert_alpha()
PlayerHealthBar2  = Image(400, 300, BigHealthBar2Img, 2)

BigHealthBar1Img = pygame.image.load('images/HealthBars/BigHealthBar1.png').convert_alpha()
PlayerHealthBar1  = Image(400, 300, BigHealthBar1Img, 2)

BigHealthBar0Img = pygame.image.load('images/HealthBars/BigHealthBar0.png').convert_alpha()
PlayerHealthBarEmpty  = Image(400, 300, BigHealthBar0Img, 2)

##### CHARACTERS #####
Landon = RockGrunt("Landon")
Aiden = PaperGrunt("Aiden")
Fred = ScissorsGrunt("Fred")
Joel = Boss("Joel")