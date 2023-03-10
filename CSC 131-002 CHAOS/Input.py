from tkinter import *
import enchant
dictionary = enchant.Dict("en_US")
window = Tk()
f1 = Frame(window)
f2 = Frame(window)


e1 = Entry(f1)
e1.grid(row=0,column=0)

b1 = Button(f1, text="Analyze", command=lambda : Analyze(e1.get()))
b1.grid(row=0,column=1)

l1 = Label(f2,text="")
l1.grid(row=0,column=0)
b2 = Button(f2, text="Anoteher one", command=lambda: Home)
b2.grid(row=0,column=1)

def Home():
    f1.pack()
    f2.pack_forget

def Analyze(word):
    f2.pack
    f1.pack_forget
    if (isinstance(str, word) == True):
        wordLen = len(word)
        wordValid = dictionary.check(word)
        if wordValid == False:
            wordList = dictionary.suggest(word)
            l1.config(text = f"STRING ({word})\n{wordLen} characters\nClose english words include:\n{wordList}")
        else:
            l1.config(text = f"STRING ({word})\n{wordLen} characters\nValid English word")
    elif (isinstance(int, word) == True):
        wordEven = isEven(word)
        wordPrime = isPrime(word)
        if (wordPrime == True):
            l1.config(text=f"NUMBER ({word})\nInteger.\n{wordEven}\nPrime.")
        else:
            l1.config(text=f"NUMBER ({word})\nInteger.\n{wordEven}")
    elif (isinstance(float, word) == True):
        l1.config(text=f"NUMBER ({word})\nDecimal.")
  
def isEven(e):
    if (e % 2) == 0:
        return "Even."
    else:
        return "Odd."

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

window.title("Analyzer ver 1.0")
window.geometry("400x200")
window.mainloop()