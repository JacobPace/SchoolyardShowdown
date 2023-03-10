######################################################################
# author: Jacob Pace
# date: Feb 6, 2023    
# desc: Exam Prep Simulation
#####################################################################
import random

# Setup global static variables
DEBUG = True   # Activate intermediate output 
random.seed("131-2023")
sim = 1

# Print out the header and get all needed information from the user
print("Simluation Setup:")
print("="*50)
Questions = int(input("What is the size of the question bank? "))
Studied = int(input("How many of those questions have you studied? "))
Test = int(input("How many questions does the test have? "))
Passing = int(input("How many questions must you answer correctly to pass the test? "))
print("="*50)
Runs = int(input("How many simulations do you want to run? "))
print("="*50)

# Generate the question bank, what you studied, what you got correct,
# your chance of passing, and the DEBUG output if desired
def CheckIfPassed(Test, sim):
    # Static for calculating the passing score
    passing = 0

    # Statics for when DEBUG is True
    correct = []
    Score = 0

    # Generating random lists of non-duplicating numbers for the test and
    # what you studied

    # Test question bank
    questions = (random.sample(range(1, Questions+1), k=Test))

    # What you studied
    studied = (random.sample(range(1, Questions+1), k=Studied))

    # Find all correct answers and use them for the outputs
    for j in questions:
        if j in studied:
            correct.append(j)
            Score += 1
            passing += 1

    # When DEBUG is True this will run and produce the desired output
    if (DEBUG ==True):
        print(f"Simluation No. {sim}")
        print(f"Questions you were asked: {questions}")
        print(f"Questions you studied: {studied}")
        print(f"Questions you passed: {correct}")
        print(f"Which means you scored: {Score}/{Test}")
        print("-"*50)

        # Used for the passing percentage chance
        if passing >= Passing:
            return 1
        else:
            return 0

    # When DEBUG is True, the first if statement will run and produce the
    # DEBUG output as desired, in the case of DEBUG being False,
    # the non-DEBUG output will run only producing the chance of
    # the user passing
    elif (passing >= Passing and DEBUG == False):
        return 1
    elif (passing < Passing and DEBUG == False):
        return 0
    
# Run the desired number of simulations
def Sim(Runs,sim):
    # Static for average output
    passed = 0

    # Run all desired simulations
    for i in range(1, Runs+1):
        passed += CheckIfPassed(Test, sim)
        sim +=1

    # Calulate chance of passing and output
    avg = passed / Runs
    print(f"You passed the test {avg*100}% of the time!")

# Output
print("="*50)
Sim(Runs,sim)