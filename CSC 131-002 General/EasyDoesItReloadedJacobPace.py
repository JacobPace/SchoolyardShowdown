##########################################################################
#Name: Jacob Pace
#Date: 10/04/2022
#Description: Asks for and receives the user's name and test scores
##########################################################################

# A function that prompts the user for a name and returns it to the
# calling statement.
def getName():
    global userName
    userName = input("What is your name? ")
    return userName

# A function that prompts the user for a score and returns it to the
# calling statement.
def getScores(userName):
    global testScore1
    global testScore2
    testScore1 = float(input("What did you score on your first test {}? " .format(userName)))
    testScore2 = float(input("What did you score on your second test? "))
    return testScore1, testScore2

# A function that receives two numbers and returns the average of those
# two values to the calling statement.
def calcAverage(testScore1, testScore2):
    global average
    average = (testScore1 + testScore2) / 2
    return average

# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def runProgram(userName, average):
    print(f"Ok {userName}, the average between your two test scores is {average}!")

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
getName()

# prompt for two scores
getScores(userName)

# calculate the average
calcAverage(testScore1, testScore2)

# display the final output
runProgram(userName, average)