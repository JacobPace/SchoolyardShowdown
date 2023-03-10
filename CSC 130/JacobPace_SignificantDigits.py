##########################################################################
# author: Jacob Pace 
# date: 12/9/2022  
# desc: A program that generates a list of random numbers and returns all significant digits
#########################################################################
from random import randint, seed
SHOWLIST = False 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.

# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def listSize():
    global size
    size = int(input("How large do you want the list to be?: "))
    global seedNum
    seedNum = int(input("What seed do you want?: "))
    return size, seedNum

# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def output(a,b):
    print(f"MSD:\t{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}\t{a[4]}\t{a[5]}\t{a[6]}\t{a[7]}\t{a[8]}\t{a[9]}")
    print(f"LSD:\t{b[0]}\t{b[1]}\t{b[2]}\t{b[3]}\t{b[4]}\t{b[5]}\t{b[6]}\t{b[7]}\t{b[8]}\t{b[9]}")
    return

# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def numList(a, b):
    num = []
    seed(b)
    while a > 0:
        num.append(randint(MIN, MAX))
        a -= 1
    return num

# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.
def MSD(a):
    msd0 = 0
    msd1 = 0
    msd2 = 0
    msd3 = 0
    msd4 = 0
    msd5 = 0
    msd6 = 0
    msd7 = 0
    msd8 = 0
    msd9 = 0
    for i in a:
        i = str(i)
        b = int(i[0])
        if (b == 0):
            msd0 += 1
        elif (b == 1):
            msd1 += 1
        elif (b == 2):
            msd2 += 1
        elif (b == 3):
            msd3 += 1
        elif (b == 4):
            msd4 += 1
        elif (b == 5):
            msd5 += 1
        elif (b == 6):
            msd6 += 1
        elif (b == 7):
            msd7 += 1
        elif (b == 8):
            msd8 += 1
        elif (b == 9):
            msd9 += 1
    msd = [msd0, msd1, msd2, msd3, msd4, msd5, msd6, msd7, msd8, msd9]
    return msd

# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def LSD(a):
    lsd0 = 0
    lsd1 = 0
    lsd2 = 0
    lsd3 = 0
    lsd4 = 0
    lsd5 = 0
    lsd6 = 0
    lsd7 = 0
    lsd8 = 0
    lsd9 = 0
    for i in a:
        i = str(i)
        b = int(i[-1])
        if (b == 0):
            lsd0 += 1
        elif (b == 1):
            lsd1 += 1
        elif (b == 2):
            lsd2 += 1
        elif (b == 3):
            lsd3 += 1
        elif (b == 4):
            lsd4 += 1
        elif (b == 5):
            lsd5 += 1
        elif (b == 6):
            lsd6 += 1
        elif (b == 7):
            lsd7 += 1
        elif (b == 8):
            lsd8 += 1
        elif (b == 9):
            lsd9 += 1
    lsd = [lsd0, lsd1, lsd2, lsd3, lsd4, lsd5, lsd6, lsd7, lsd8, lsd9]
    return lsd
###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
listSize()
#   create the list of random numbers
nums = numList(size, seedNum)
#   If SHOWLIST is selected, print out the list of numbers

#   print the head of the table which just shows the numbers 0-9
print(f"\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
print("-"*83)
#   Calculate the MSD and LSD, and print out their statistics.
output(MSD(nums),LSD(nums))