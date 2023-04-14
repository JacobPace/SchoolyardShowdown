# Dialouge for the game
class Dialouge:
    def __init__(self, text):
        self.text = text
        self.displayed = False

playerOpeningLine1 = Dialouge("I can't win unless I get closer")
playerDialouge = [playerOpeningLine1]

enemyLine1 = Dialouge("OH, you're approaching me?!")
enemyLine2 = Dialouge("HOHO, then come as close as you like!") 
enemyTempDialouge = [enemyLine1, enemyLine2]

WinRound = Dialouge("Win!")
LoseRound = Dialouge("Lose!")
DrawRound = Dialouge("It's a Draw?")
PlayerBlock = Dialouge("You blocked it!")
EnemyBlock = Dialouge("They blocked!")