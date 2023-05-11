# Dialouge for the game
class Dialouge:
    def __init__(self, text):
        self.text = text
        self.displayed = False
#need a change to commit nahudjkawbksjBDkjsAJKDASJ
playerOpeningLine1 = Dialouge("I can't win unless I get closer")
playerDialouge = [playerOpeningLine1]

enemyLine1 = Dialouge("OH, you're approaching me?!")
enemyLine2 = Dialouge("HOHO, then come as close as you like!") 

BossLine1 = "Joel: "
PlayerLine1BossFight = "PLayer: "
BosLine2 = "Joel: "
PlayerLine2BossFight = "Player: "

WinRound = Dialouge("Win!")
LoseRound = Dialouge("Lose!")
DrawRound = Dialouge("It's a Draw?")
PlayerBlock = Dialouge("You blocked it!")
EnemyBlock = Dialouge("They blocked!")

enemyLoss = Dialouge("Enemy: OH NO!")
victory = Dialouge("YOU WIN!")
victoryAlt = "YOU WIN!"

##### LORE #####
Lore01 = "It's almost lunch time, time to look at the menu!"
Lore0 = Dialouge("???: Hey! Hey you! Yeah you!")

Lore1 = Dialouge("Joel: Gimme your lunch money, I left mine at home.")
Lore2 = Dialouge("*Rustling*")

Lore3 =  Dialouge("*Your lunch money just got stolen!*")
Lore4 =  Dialouge("HEY! GIVE IT BACK!")

Lore5 =  Dialouge("Joel: Oh, looks like we got a fighter boys!")
Lore6 =  Dialouge("Joel: Well, if you want it back that bad, you gotta beat my boys in a match!")

Lore7 =  Dialouge("Joel: Then I'll let you fight me for it.")
Lore8 =  Dialouge("Joel: Don't worry, I'm a man of my word. If you beat all of us I'll give it back.")

Lore9 =  Dialouge("Joel: If you win, HAHAHAHAHAHA!")
Lore10 =  Dialouge("Joel: Oh yeah, I should introduce the boys. Left to right are Dwayne, Aiden, and Fred.")

Lore11 =  Dialouge("Joel: You'll go against them in that order.")
Lore12 =  Dialouge("Joel: Good luck, you'll need it.")

##### DWAYNE LINES #####
DwayneOpen0 = "Dwayne: Get ready punk!"
DwayneOpen1 = Dialouge("Dwayne: I'm gonna ROCK your world!")
DwayneOpen = [DwayneOpen0, DwayneOpen1]

DwayneDrawLine = "Dwayne: Huh?"

DwayneWinRound0 = "Dwayne: Take that punk!"
DwayneWinRound1 = "Dwayne: You really thought you was gonna win?"
DwayneWinRound2 = "Dwayne: Ya never stood a chance kid."

DwayneLoseRound0 = "Dwayne: That was all luck!"
DwayneLoseRound1 = "Dwayne: How'd you do that?!"
DwayneLoseRound2 = "Dwayne: HUH?!"

DwayneBlockLine = "Dwayne: You can't touch this!"

DwayneBattleScript = [DwayneDrawLine, DwayneWinRound0, DwayneWinRound1, DwayneWinRound2, DwayneLoseRound0, DwayneLoseRound1, DwayneLoseRound2, DwayneBlockLine]

DwayenWinBattle = "Dwayne: You'd never beat the boss if you can't get past me!"
DwayneLoseBattle = "Dwayne: Impossible... Dwayne is conflicted..."

##### AIDEN LINES #####
AidenOpen0 = "Aiden: Wow, you actually beat Dwayne, impressive."
AidenOpen1 = Dialouge("Aiden: Too bad you'll just lose to my calculations!")

AidenDrawLine = "Aiden: Interesting..."

AidenBlockLine = "Aiden: HA! I outsmarted your outsmarting!"

AidenWinRound0 = "Aiden: Just as I predicted!"
AidenWinRound1 = "Aiden: Well within calculations."
AidenWinRound2 = "Aiden: All according to plan."

AidenLoseRound0 = "Aiden: Hmm, a statistical anomaly..."
AidenLoseRound1 = "Aiden: Unexpected, but still within predictions..."
AidenLoseRound2 = "Aiden: ..."

AidenBattleScript = [AidenDrawLine, AidenWinRound0, AidenWinRound1, AidenWinRound2, AidenLoseRound0, AidenLoseRound1, AidenLoseRound2, AidenBlockLine]

AidenWinBattle = "Aiden: You were a fool to think you could beat me!"
AidenLoseBattle = "Aiden: WHAT! IMPOSSIBLE! FRED! Put this punk in his place!"
##### FRED LINES #####
FredOpen0 = "Fred: Man I'm right next to you so stop yelling!"
FredOpen1 = Dialouge("Fred: Sorry about that guy, he can be pretty annoying.")
FredOpen2 = Dialouge("Fred: You'll find that I'm a bit more CUT back than the those guys.")

FredDrawLine = "Fred: Wow, you're putting up a good fight."

FredBlockLine = "Fred: Good, but not good enough!"

FredWinRound0 = "Fred: Oof, better luck next round."
FredWinRound1 = "Fred: Today is not your day is it?"
FredWinRound2 = "Fred: Man, are you even trying?"

FredLoseRound0 = "Fred: Hey, not bad kid."
FredLoseRound1 = "Fred: I wasn't expecting that."
FredLoseRound2 = "Fred: Woah, I better be careful!"

FredBattleScript = [FredDrawLine, FredWinRound0, FredWinRound1, FredWinRound2, FredLoseRound0, FredLoseRound1, FredLoseRound2, FredBlockLine]

FredWinBattle = "Fred: So close yet so far, better luck next time."
FredLoseBattle = "Fred: Wow! your pretty good kid, but the boss won't go easy on ya. Good luck, you'll need it."
##### JOEL LINES #####
JoelOpen0 = "Joel: Wow. You actually beat them. I'm impressed."
JoelOpen1 = Dialouge("Joel: Even still, like I said, you gotta beat me if you want your lunch money back!")
JoelOpen2 = Dialouge("Joel: So, what are ya waiting for! Let's get this show on the road!")

JoelDrawLine = "Joel: This is boring."

JoelBlockLine = "Joel: You're gonna have to try harder than that!"

JoelWinRound0 = "Joel: C'mon, are you even trying?"
JoelWinRound1 = "Joel: This is too easy!"
JoelWinRound2 = "Joel: Do you even want your lunch money back?!"

JoelLoseRound0 = "Joel: Not bad..."
JoelLoseRound1 = "Joel: I might just have to get serious after all."
JoelLoseRound2 = "Joel: One lucky guy right here."

JoelBattleScript = [JoelDrawLine, JoelWinRound0, JoelWinRound1, JoelWinRound2, JoelLoseRound0, JoelLoseRound1, JoelLoseRound2, JoelBlockLine]

JoelWinBattle = "Joel: HA! Try again another time, see ya later shtinky!"

##### FINALE LINES #####
Finale0 = "Joel: Wow, you're actually pretty good."
Finale1 = Dialouge("Joel: Too bad I gotta crush you.")

# Turn 1
Finale2 = Dialouge("Joel: ...")
Finale3 = Dialouge("Joel: Huh, thats pretty funny.")
Finale4 = Dialouge("Joel: Now I'm gonna crush you!")

# Turn 2
Finale5 = Dialouge("Joel: ...")
Finale6 = Dialouge("Joel: Ok then, that's wierd...")
Finale7 = Dialouge("Joel: How about this!")

# Turn 3
Finale8 = Dialouge("Joel: ...")
Finale9 = Dialouge("Joel: What...")
Finale10 = Dialouge("Joel: Ok, now this is getting annoying.")
Finale11 = Dialouge("Joel: Lets finish this already, lunch is about to start.")

##### Actual Finale #####
Finale12 = Dialouge("Joel: WHAT! NO! THAT'S CHEATING!")
Finale13 = Dialouge("Fred: Boss, to be fair you never set any rules.")
Finale14 = Dialouge("Joel: ...")
Finale15 = Dialouge("Joel: FINE! Here's your stupid lunch money.")
Finale16 = Dialouge("Joel: You won't get so lucky next time!")
Finale17 = Dialouge("Joel: Lets get out of here boys!")

GameOver = Dialouge("OH NO! YOU LOST! Press any button to return to roll the credits!")
GameWon = Dialouge("Congratulations! You got the lunch money back! Press any button to continue!")