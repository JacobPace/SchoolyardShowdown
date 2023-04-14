import pygame
from game import Button
pygame.init()

##### START MENU #####
start_img = pygame.image.load('images/StartButton.png').convert_alpha()
start_hover = pygame.image.load('images/StartButtonSelected.png').convert_alpha()

exit_img = pygame.image.load('images/ExitButton.png').convert_alpha()
exit_hover = pygame.image.load('images/ExitButtonSelected.png').convert_alpha()

options_img = pygame.image.load('images/OptionsButton.png').convert_alpha()
options_hover = pygame.image.load('images/OptionsButtonSelected.png').convert_alpha()


back_img = pygame.image.load('images/BackButton.png').convert_alpha()
back_hover = pygame.image.load('images/BackButtonSelected.png').convert_alpha()

# Initialize the buttons via the "" file (where we put the recycleable code)
# when making the buttons the inputs look like this "x, y, image, imgHover, scale, selected by default?"
# start menu buttons
start_button = Button(50, 100, start_img, start_hover, 0.2, True)
exit_button = Button(50, 250, exit_img, exit_hover, 3, False)
options_button = Button(50, 400, options_img, options_hover, 3, False)
# options menu buttons
back_button = Button(50, 500 , back_img, back_hover, 3, True)
exit_button2 = Button(295, 500, exit_img, exit_hover, 3, False)

# attack menu buttons
attackImg = pygame.image.load('images/AttackMenuButton.png').convert_alpha()
attackImgSelected = pygame.image.load('images/AttackMenuButtonSelected.png').convert_alpha()
attackButton = Button(50, 775, attackImg, attackImgSelected, 1, True)

rockImg = pygame.image.load('images/RockButton.png').convert_alpha()
rockImgSelected = pygame.image.load('images/RockButtonSelected.png').convert_alpha()
RockButton = Button(175, 775, rockImg, rockImgSelected, 1, False)

paperImg = pygame.image.load('images/PaperButton.png').convert_alpha()
paperImgSelected = pygame.image.load('images/PaperButtonSelected.png').convert_alpha()
PaperButton = Button(275, 775, paperImg, paperImgSelected, 1, False)

scissorsImg = pygame.image.load('images/ScissorsButton.png').convert_alpha()
scissorsImgSelected = pygame.image.load('images/ScissorsButtonSelected.png').convert_alpha()
ScissorsButton = Button(375, 775, scissorsImg, scissorsImgSelected, 1, False)

backImg = pygame.image.load('images/BackBattleButton.png').convert_alpha()
backImgSelected = pygame.image.load('images/BackBattleButtonSelected.png').convert_alpha()
BackButton = Button(475, 775, backImg, backImgSelected, 1, False)

runImg = pygame.image.load('images/RunButton.png').convert_alpha()
runImgSelected = pygame.image.load('images/RunButtonSelected.png').convert_alpha()
RunButton = Button(175, 775, runImg, runImgSelected, 1, False)

bagImg = pygame.image.load('images/BagButton.png').convert_alpha()
bagImgSelected = pygame.image.load('images/BagButtonSelected.png').convert_alpha()
BagButton = Button(275, 775, bagImg, bagImgSelected, 1, False)