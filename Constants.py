import pygame
from game import *
import math
pygame.init()

WIDTH = 1600
HEIGHT = 800
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # FPS controller
results = (None, None)
PlayerAction = None
FoeAction = None

##### IMAGES/BUTTONS #####

bg = pygame.image.load('images/StartMenuBackgroundTest.png').convert_alpha()
tiles = math.ceil(WIDTH/ bg.get_width()) + 1

creditsImg = pygame.image.load('images/Credits.png').convert_alpha()

credits = Image(0, 0, creditsImg, 0.5)
credits = Image(0, 0, creditsImg, 1)
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
AttackButton = Button(490, 680, attackImg, attackImgSelected, 0.65, True)

#runImg = pygame.image.load('images/RunButton.png').convert_alpha()
#runImgSelected = pygame.image.load('images/RunButtonSelected.png').convert_alpha()
#RunButton = Button(1311, 785, runImg, runImgSelected, 1.01, False)

bagImg = pygame.image.load('images/BattleSelectionMenuButtons/BagButton.png').convert_alpha()
bagImgSelected = pygame.image.load('images/BattleSelectionMenuButtons/BagButtonSelected.png').convert_alpha()
BagButton = Button(825, 680, bagImg, bagImgSelected, 0.65, False)

blockImg = pygame.image.load('images/BattleSelectionMenuButtons/BlockButton.png').convert_alpha()
blockImgSelected = pygame.image.load('images/BattleSelectionMenuButtons/BlockButtonSelected.png').convert_alpha()
BlockButton = Button(490, 750, blockImg, blockImgSelected, 0.65, False)

##### ATTACK MENU BUTTONS #####
rockImg = pygame.image.load('images/BattleAttackMenuButtons/RockButton.png').convert_alpha()
rockImgSelected = pygame.image.load('images/BattleAttackMenuButtons/RockButtonSelected.png').convert_alpha()
RockButton = Button(490, 680, rockImg, rockImgSelected, 0.65, True)

paperImg = pygame.image.load('images/BattleAttackMenuButtons/PaperButton.png').convert_alpha()
paperImgSelected = pygame.image.load('images/BattleAttackMenuButtons/PaperButtonSelected.png').convert_alpha()
PaperButton = Button(825, 680, paperImg, paperImgSelected, 0.65, False)

scissorsImg = pygame.image.load('images/BattleAttackMenuButtons/ScissorsButton.png').convert_alpha()
scissorsImgSelected = pygame.image.load('images/BattleAttackMenuButtons/ScissorsButtonSelected.png').convert_alpha()
ScissorsButton = Button(490, 750, scissorsImg, scissorsImgSelected, 0.65, False)

backImg = pygame.image.load('images/BattleAttackMenuButtons/BackBattleButton.png').convert_alpha()
backImgSelected = pygame.image.load('images/BattleAttackMenuButtons/BackBattleButtonSelected.png').convert_alpha()
BackButton = Button(825, 750, backImg, backImgSelected, 0.65, False)

MysteryItemImg = pygame.image.load('images/BattleAttackMenuButtons/MysteryItem.png').convert_alpha()
MysteryItemImgSelected = pygame.image.load('images/BattleAttackMenuButtons/MysteryItemSelected.png').convert_alpha()
MysteryItemButton = Button(490, 680, MysteryItemImg, MysteryItemImgSelected, 0.75, True)
BackButtonFinale = Button(825, 750, backImg, backImgSelected, 0.65, False)

MysteryItemImg = pygame.image.load('images/BattleAttackMenuButtons/MysteryItem.png').convert_alpha()
MysteryItemImgSelected = pygame.image.load('images/BattleAttackMenuButtons/MysteryItemSelected.png').convert_alpha()
MysteryItemButton = Button(788, 785, MysteryItemImg, MysteryItemImgSelected, 1.01, True)
BackButtonFinale = Button(1311, 785, backImg, backImgSelected, 1.01, False)

##### BAG MENU BUTTONS #####
BagMenuBackButton = Button(825, 680, backImg, backImgSelected, 0.65, False)

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

BandAid = Button(490, 680, BandAid5Img, BandAid5ImgSelected, 0.01, True)
BandAid = Button(788, 785, BandAid5Img, BandAid5ImgSelected, 1, True)

##### IMAGE TO DISPLAY DIALOGUE ON #####
textBoxImg = pygame.image.load('images/TextBox.png').convert_alpha()
TextBox = Image(0, 750, textBoxImg, 0.75)

BattleSelectionMenuBoxImg = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu.png').convert_alpha()
BattleSelectionMenu = Image(0, 650, BattleSelectionMenuBoxImg, 0.75)

BattleSelctionMenu3Img = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu3.png').convert_alpha()
BattleSelectionMenu3 = Image(0, 650, BattleSelctionMenu3Img, 0.75)

BattleSelctionMenu2Img = pygame.image.load('images/BattleSelectionMenuButtons/BattleSelectionMenu2.png').convert_alpha()
BattleSelectionMenu2 = Image(0, 650, BattleSelctionMenu2Img, 0.75)

SpeechBoxImg = pygame.image.load('images/SpeechBox.png').convert_alpha()
SpeechBox = Image(0, 650, SpeechBoxImg, 0.75)

##### BATTLE RESULTS #####
BattleDrawImg = pygame.image.load('images/BattleResults/BattleDraw.png').convert_alpha()
BattleDraw = Image(100, 700, BattleDrawImg, 0.75)

LostBattleImg = pygame.image.load('images/BattleResults/PlayerBattleLost.png').convert_alpha()
LostBattle = Image(100, 700, LostBattleImg, 0.75)

WonBattleImg = pygame.image.load('images/BattleResults/PlayerBattleWon.png').convert_alpha()
WonBattle = Image(100, 700, WonBattleImg, 0.75)

WonRoundImg = pygame.image.load('images/BattleResults/PlayerRoundWon.png').convert_alpha()
WonRound = Image(100, 700, WonRoundImg, 0.75)

LostRoundImg = pygame.image.load('images/BattleResults/PlayerRoundLost.png').convert_alpha()
LostRound = Image(100, 700, LostRoundImg, 0.75)

PlayerBlockedImg = pygame.image.load('images/BattleResults/PlayerBlocked.png').convert_alpha()
PlayerBlocked = Image(100, 700, PlayerBlockedImg, 0.75)

EnemyBlockedImg = pygame.image.load('images/BattleResults/EnemyBlocked.png').convert_alpha()
EnemyBlocked = Image(100, 700, EnemyBlockedImg, 0.75)

PlayerBlockedFailedImg = pygame.image.load('images/BattleResults/BlockFailed.png').convert_alpha()
PlayerBlockFailed = Image(100, 700, PlayerBlockedFailedImg, 0.75)

BlankResultImg = pygame.image.load('images/BattleResults/Blank.png').convert_alpha()
BlankResult = Image(100, 700, BlankResultImg, 0.75)

##### CHANGE PLAYER/ENEMY PICTURE IN FIGHT #####
# initalize the player/enemy for testing purposes
#lil_dude = pygame.image.load('images/lil_dude.png').convert_alpha()
player = Player(100,100) # taken areguments are the default x,y coordinates
"""
enemyImg = pygame.image.load('images/enemy.png').convert_alpha()
#Ronald = Enemy("Ronald")
enemytest = Image(1500, 100, enemyImg, 10)
"""
# Player battle images
PlayerIdleImg = pygame.image.load('images/PlayerActions/PlayerStanding.png').convert_alpha()
PlayerIdle = Image(100, 275, PlayerIdleImg, 5)
PlayerIdle = Image(100, 400, PlayerIdleImg, 5)

PlayerBlockImg = pygame.image.load('images/PlayerActions/PlayerBlock.png').convert_alpha()
PlayerBlockPic = Image(100, 275 ,PlayerBlockImg, 5)

PlayerRockImg = pygame.image.load('images/PlayerActions/PlayerRock.png').convert_alpha()
PlayerRock = Image(100, 275, PlayerRockImg, 5)

PlayerPaperImg = pygame.image.load('images/PlayerActions/PlayerPaper.png').convert_alpha()
PlayerPaper = Image(100, 275, PlayerPaperImg, 5)

PlayerScissorsImg = pygame.image.load('images/PlayerActions/PlayerScissors.png').convert_alpha()
PlayerScissors = Image(100, 275, PlayerScissorsImg, 5)

PlayerThrowImg = pygame.image.load('images/PlayerActions/PlayerThrow.png').convert_alpha()
PlayerThrow = Image(100, 275, PlayerThrowImg, 5)

PlayerMysteryItemImg = pygame.image.load('images/PlayerActions/PlayerMysteryItem2.png').convert_alpha()
PlayerMysteryItem = Image(100, 275, PlayerMysteryItemImg, 5)

PlayerHurtImg = pygame.image.load('images/PlayerActions/PlayerHurt.png').convert_alpha()
PlayerHurt = Image(100, 275, PlayerHurtImg, 5)

PlayerMysteryItem = Image(100, 400, PlayerMysteryItemImg, 5)

PlayerHurtImg = pygame.image.load('images/PlayerActions/PlayerHurt.png').convert_alpha()
PlayerHurt = Image(100, 400, PlayerHurtImg, 5)

"""
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
"""
##### DWAYNE IMAGES #####
DwayneIdleImg = pygame.image.load('images/Dwayne/Dwayne.png').convert_alpha()

DwayneIdle = Image(1200, 100, DwayneIdleImg, 5)

DwayneThrowImg = pygame.image.load('images/Dwayne/DwayneThrow.png').convert_alpha()
DwayneThrow =  Image(1200, 100, DwayneThrowImg, 5)

DwayneRockImg = pygame.image.load('images/Dwayne/DwayneRock.png').convert_alpha()
DwayneRock = Image(1200, 100, DwayneRockImg, 5)

DwaynePaperImg = pygame.image.load('images/Dwayne/DwaynePaper.png').convert_alpha()
DwaynePaper = Image(1200, 100, DwaynePaperImg, 5)

DwayneScissorsImg = pygame.image.load('images/Dwayne/DwayneScissors.png').convert_alpha()
DwayneScissors = Image(1200, 100, DwayneScissorsImg, 5)

DwayneBlockImg = pygame.image.load('images/Dwayne/DwayneBlock.png').convert_alpha()
DwayneBlock = Image(1200, 100, DwayneBlockImg, 5)

DwayneHurtImg = pygame.image.load('images/Dwayne/DwayneHurt.png').convert_alpha()
DwayneHurt = Image(1200, 100, DwayneHurtImg, 5)

##### AIDEN IMAGES #####
AidenIdleImg = pygame.image.load('images/Aiden/AidenIdle.png').convert_alpha()
AidenIdle = Image(1200, 100, AidenIdleImg, 5)

AidenThrowImg = pygame.image.load('images/Aiden/AidenThrow.png').convert_alpha()
AidenThrow =  Image(1200, 100, AidenThrowImg, 5)

AidenRockImg = pygame.image.load('images/Aiden/AidenRock.png').convert_alpha()
AidenRock = Image(1200, 100, AidenRockImg, 5)

AidenPaperImg = pygame.image.load('images/Aiden/AidenPaper.png').convert_alpha()
AidenPaper = Image(1200, 100, AidenPaperImg, 5)

AidenScissorsImg = pygame.image.load('images/Aiden/AidenScissors.png').convert_alpha()
AidenScissors = Image(1200, 100, AidenScissorsImg, 5)

AidenBlockImg = pygame.image.load('images/Aiden/AidenBlock.png').convert_alpha()
AidenBlock = Image(1200, 100, AidenBlockImg, 5)

AidenHurtImg = pygame.image.load('images/Aiden/AidenHurt.png').convert_alpha()
AidenHurt = Image(1200, 100, AidenHurtImg, 5)

##### FRED IMAGES #####
FredIdleImg = pygame.image.load('images/Fred/FredIdle.png').convert_alpha()
FredIdle = Image(1200, 100, FredIdleImg, 5)

FredThrowImg = pygame.image.load('images/Fred/FredThrow.png').convert_alpha()
FredThrow =  Image(1200, 100, FredThrowImg, 5)

FredRockImg = pygame.image.load('images/Fred/FredRock.png').convert_alpha()
FredRock = Image(1200, 100, FredRockImg, 5)

FredPaperImg = pygame.image.load('images/Fred/FredPaper.png').convert_alpha()
FredPaper = Image(1200, 100, FredPaperImg, 5)

FredScissorsImg = pygame.image.load('images/Fred/FredScissors.png').convert_alpha()
FredScissors = Image(1200, 100, FredScissorsImg, 5)

FredBlockImg = pygame.image.load('images/Fred/FredBlock.png').convert_alpha()
FredBlock = Image(1200, 100, FredBlockImg, 5)

FredHurtImg = pygame.image.load('images/Fred/FredHurt.png').convert_alpha()
FredHurt = Image(1200, 100, FredHurtImg, 5)

##### JOEL IMAGES #####
JoelIdleImg = pygame.image.load('images/Joel/JoelIdle.png').convert_alpha()
JoelIdle = Image(1200, 100, JoelIdleImg, 5)

JoelThrowImg = pygame.image.load('images/Joel/JoelThrow.png').convert_alpha()
JoelThrow =  Image(1200, 100, JoelThrowImg, 5)

JoelRockImg = pygame.image.load('images/Joel/JoelRock.png').convert_alpha()
JoelRock = Image(1200, 100, JoelRockImg, 5)

JoelPaperImg = pygame.image.load('images/Joel/JoelPaper.png').convert_alpha()
JoelPaper = Image(1200, 100, JoelPaperImg, 5)

JoelScissorsImg = pygame.image.load('images/Joel/JoelScissors.png').convert_alpha()
JoelScissors = Image(1200, 100, JoelScissorsImg, 5)

JoelBlockImg = pygame.image.load('images/Joel/JoelBlock.png').convert_alpha()
JoelBlock = Image(1200, 100, JoelBlockImg, 5)

JoelHurtImg = pygame.image.load('images/Joel/JoelHurt.png').convert_alpha()
JoelHurt = Image(1200, 100, JoelHurtImg, 5)

JoelShockImg = pygame.image.load('images/Joel/JoelShock.png').convert_alpha()
JoelShock = Image(1200, 100, JoelShockImg, 5)

##### Intro Images #####
FredIntro = Image(600, 100, FredIdleImg, 5)
AidenIntro = Image(400, 100, AidenIdleImg, 5)
DwayneIntro = Image(200, 100, DwayneIdleImg, 5)

##### ENEMY HEALTH BAR #####
BossHealthBar5Img = pygame.image.load('images/HealthBars/BossHealthBar5.png').convert_alpha()

BossHealthBar5 = Image(900, 50, BossHealthBar5Img, 2)

BossHealthBar4Img = pygame.image.load('images/HealthBars/BossHealthBar4.png').convert_alpha()
BossHealthBar4 = Image(900, 50, BossHealthBar4Img, 2)

BossHealthBar3Img = pygame.image.load('images/HealthBars/BossHealthBar3.png').convert_alpha()
BossHealthBar3 = Image(900, 50, BossHealthBar3Img, 2)

BossHealthBar2Img = pygame.image.load('images/HealthBars/BossHealthBar2.png').convert_alpha()
BossHealthBar2 = Image(900, 50, BossHealthBar2Img, 2)

BossHealthBar1Img = pygame.image.load('images/HealthBars/BossHealthBar1.png').convert_alpha()
BossHealthBar1 = Image(900, 50, BossHealthBar1Img, 2)

BossHealthBar0Img = pygame.image.load('images/HealthBars/BossHealthBar0.png').convert_alpha()
BossHealthBar0 = Image(900, 50, BossHealthBar0Img, 2)

# Grunt Health bar
GruntHealthBar3Img = pygame.image.load('images/HealthBars/GruntHealthBar3.png').convert_alpha()
GruntHealthBar3 = Image(900, 50, GruntHealthBar3Img, 2)

GruntHealthBar2Img = pygame.image.load('images/HealthBars/GruntHealthBar2.png').convert_alpha()
GruntHealthBar2 = Image(900, 50, GruntHealthBar2Img, 2)

GruntHealthBar1Img = pygame.image.load('images/HealthBars/GruntHealthBar1.png').convert_alpha()
GruntHealthBar1 = Image(900, 50, GruntHealthBar1Img, 2)

GruntHealthBar0Img = pygame.image.load('images/HealthBars/GruntHealthBar0.png').convert_alpha()
GruntHealthBar0 = Image(900, 50, GruntHealthBar0Img, 2)

##### PLAYER HEALTH BAR #####
BigHealthBar7Img = pygame.image.load('images/HealthBars/PlayerHealthBar7.png').convert_alpha()

PlayerHealthBarFull  = Image(400, 200, BigHealthBar7Img, 2)

BigHealthBar6Img = pygame.image.load('images/HealthBars/PlayerHealthBar6.png').convert_alpha()
PlayerHealthBar6  = Image(400, 200, BigHealthBar6Img, 2)

BigHealthBar5Img = pygame.image.load('images/HealthBars/PlayerHealthBar5.png').convert_alpha()
PlayerHealthBar5  = Image(400, 200, BigHealthBar5Img, 2)

BigHealthBar4Img = pygame.image.load('images/HealthBars/PlayerHealthBar4.png').convert_alpha()
PlayerHealthBar4  = Image(400, 200, BigHealthBar4Img, 2)

BigHealthBar3Img = pygame.image.load('images/HealthBars/PlayerHealthBar3.png').convert_alpha()
PlayerHealthBar3  = Image(400, 200, BigHealthBar3Img, 2)

BigHealthBar2Img = pygame.image.load('images/HealthBars/PlayerHealthBar2.png').convert_alpha()
PlayerHealthBar2  = Image(400, 200, BigHealthBar2Img, 2)

BigHealthBar1Img = pygame.image.load('images/HealthBars/PlayerHealthBar1.png').convert_alpha()
PlayerHealthBar1  = Image(400, 200, BigHealthBar1Img, 2)

BigHealthBar0Img = pygame.image.load('images/HealthBars/PlayerHealthBar0.png').convert_alpha()
PlayerHealthBarEmpty  = Image(400, 200, BigHealthBar0Img, 2)

PlayerHealthBar = [PlayerHealthBarEmpty, PlayerHealthBar1, PlayerHealthBar2, PlayerHealthBar3, PlayerHealthBar4, PlayerHealthBar5, PlayerHealthBar6, PlayerHealthBarFull]
PlayerHealthBarFull  = Image(400, 300, BigHealthBar7Img, 2)

BigHealthBar6Img = pygame.image.load('images/HealthBars/PlayerHealthBar6.png').convert_alpha()
PlayerHealthBar6  = Image(400, 300, BigHealthBar6Img, 2)

BigHealthBar5Img = pygame.image.load('images/HealthBars/PlayerHealthBar5.png').convert_alpha()
PlayerHealthBar5  = Image(400, 300, BigHealthBar5Img, 2)

BigHealthBar4Img = pygame.image.load('images/HealthBars/PlayerHealthBar4.png').convert_alpha()
PlayerHealthBar4  = Image(400, 300, BigHealthBar4Img, 2)

BigHealthBar3Img = pygame.image.load('images/HealthBars/PlayerHealthBar3.png').convert_alpha()
PlayerHealthBar3  = Image(400, 300, BigHealthBar3Img, 2)

BigHealthBar2Img = pygame.image.load('images/HealthBars/PlayerHealthBar2.png').convert_alpha()
PlayerHealthBar2  = Image(400, 300, BigHealthBar2Img, 2)

BigHealthBar1Img = pygame.image.load('images/HealthBars/PlayerHealthBar1.png').convert_alpha()
PlayerHealthBar1  = Image(400, 300, BigHealthBar1Img, 2)
#need a change to commit nahudjkawbksjBDkjsAJKDASJ
BigHealthBar0Img = pygame.image.load('images/HealthBars/PlayerHealthBar0.png').convert_alpha()
PlayerHealthBarEmpty  = Image(400, 300, BigHealthBar0Img, 2)


PlayerHealthBar = [PlayerHealthBarEmpty, PlayerHealthBar1, PlayerHealthBar2, PlayerHealthBar3, PlayerHealthBar4, PlayerHealthBar5, PlayerHealthBar6, PlayerHealthBarFull]

##### CHARACTERS #####
Dwayne = RockGrunt("Dwayne")
Aiden = PaperGrunt("Aiden")
Fred = ScissorsGrunt("Fred")
Joel = Boss("Joel")