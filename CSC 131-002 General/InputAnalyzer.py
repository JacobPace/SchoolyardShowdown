################################################
# Name: Jacob Pace
# Date: 2/15/2023
# Description: Input Analyzer
################################################

##############
# DISCLAIMER #
##############
# I do not know if the pyenchant stuff will actually work bc I kept getting the same issues
# as everyone else, but everything else works just fine, idk why pyenchant doesn't work

from tkinter import *
import enchant
dictionary = enchant.Dict("en_US")
window = Tk()

# This is the first frame the user will see
f1 = Frame(window)

# This is the frame that will display when the user analyzes their input
f2 = Frame(window)

# Setting a global variable just incase to have a value that can be reset to "None"
word = None

# The entry goes onto the first frame
e1 = Entry(f1)
e1.grid(row=0,column=0)

# Button 1 also goes onto the first frame and runs the command to analyze the input and move to the next frame
b1 = Button(f1, text="Analyze", command=lambda : Analysis())
b1.grid(row=0,column=1)

# The label is on frame 2 and displays all the information to the user about what was input
l1 = Label(f2,text="")
l1.grid(row=0,column=0)

# The second button returns the user to the first frame to do another input
b2 = Button(f2, text="Another one", command=lambda: Home())
b2.grid(row=0,column=1)

# Resets the user to the first frame and sets the input to None just in case
def Home():
    f1.pack()
    f2.pack_forget()
    global word
    word = None
    
# Sets the user to the second frame to display all the data from the analysis
def Analysis():
    f2.pack()
    f1.pack_forget()
    global word
    word = None
    word = e1.get()
    Analyze(word)

# Analyzes the data from the input
def Analyze(test):
    # This checks to see if the input is either an int or a float
    if (test.replace('.','',1).isdigit()==True):
        try: # This runs if the inut is a pure integer
            test = int(test)
            wordEven = isEven(test)
            wordPrime = isPrime(test)
            if (wordPrime == True): # This runs is the integer is prime
                l1.config(text=f"NUMBER ({word})\nInteger.\n{wordEven}\nPrime.")
                test = None
            else: # If not prime
                l1.config(text=f"NUMBER ({word})\nInteger.\n{wordEven}")
                test = None
        except ValueError: # This runs if the input is not a pure integer, i.e it has a decimal point bc it is a float
            test = float(test)
            l1.config(text=f"NUMBER ({word})\nDecimal.")
            test = None
    # This runs if the input is neither an int or a float, bc it is therefore a string
    elif (isinstance(test, str) == True):
        test = str(test)
        wordLen = len(test)
        wordValid = dictionary.check(test)
        if wordValid == False:  # If the string is an actual word this runs
            wordList = dictionary.suggest(test)
            l1.config(text = f"STRING ({test})\n{wordLen} characters\nClose english words include:\n{wordList}")
        else:  # If the string is not a word, this returns a list of words that are close to it
            l1.config(text = f"STRING ({test})\n{wordLen} characters\nValid English word")
            test = None
    test = None
    
# Checks to see if the integer is even or odd
def isEven(e):
    if (e % 2) == 0:
        return "Even."
    else:
        return "Odd."

# Checks to see if the integer is a prime number
def isPrime(prime):
    check = 2
    if prime > 1:
        while check <= (prime/2):
            if (prime % check ) == 0:
                return False
            else:
                return True
    else:
        return False

# On initialization, the "Home" frame is automatically displayed
Home()
window.title("Analyzer ver 1.0")
window.geometry("400x200")
window.mainloop()