########################################################################
# author: Jacob Pace
# date: Oct 29 / 2022
# description: Logbook
########################################################################
from math import log10
# A function that prompts the user for the minimum value and returns it
# to the calling statement. Function to also deal with range checking to
# make sure that minimum value provided is greater than 0
def getMin():
    a = float(input("Input a minimum value greater than 0: "))
    if a > 0:
        return a
    else:
        print("Number must be greater than 0!")
        return getMin()

# A function that prompts the user for the maximum value and returns it
# to the calling statement. Function receives argument that is used in
# range checking to make sure maximum value provided by user is greater
# than minimum value (provided in function argument)
def getMax(min):
    a = float(input("Input a maximum value greater then the minmum: "))
    if a > min:
        return a
    else:
        print("Value should be greater than the minimum!")
        return getMax(min)

# A function that prompts the user for the step size and returns it to
# the calling statement. Function also deals with range checking to make
# sure that step size provided is greater than 0.
def getStep():
    a = float(input("Input a value to increment by, must be greater than 0: "))
    if a > 0:
        return a
    else:
        print("Value must be greater than 0!")
        return getStep()

# A function that receives a number as an argument and returns the log
# of that number rounded to 4 decimal places.
def outLog(value):
    out = log10(round(value, 4))
    return out

# A function that receives the value at the left size of the log table
# (i.e. the value whose logarithms should be calculated). The function
# then creates a row of logarithmic values for that argument counting
# upwards in steps of 1 significant figure more than the argument. i.e.
# if the argument is 1.3, then the row gives values of the logs for
# 1.30, 1.31, 1.32, 1.33, ..., 1.39. If the argument is 2.456, then it
# gives logs for 2.4560, 2.4561, 2.4562, 2.4563, ..., 2.4569
increment = 0
def row(num, out, incre):
    if incre <= 9:
        findLog = round(float(str(num)+str(incre)), 5)
        out2 = str(round(outLog(findLog), 5))
        out += out2 + "\t"
        incre += 1
        row(num, out, incre)
    else:
        print(out)
        quit


# A function that receives the minimum, maximum and step size as
# arguments, and prints the table (making use of the function that
# creates a single row defined earlier)
def makeTable(min, max, step):
    out = str(min) + "\t"
    outMax = str(max) + "\t"
    while min < max:
        row(min, out, increment)
        min += step
        temp = round(float(min), 5)
        out = str(temp) + "\t"
    row(max, outMax, increment)
    return

####################### MAIN #########################################
# Get the minimum, maximum and step size from the user using functions
# defined earlier.
minimum = getMin()
max = getMax(minimum)
step = getStep()

# create the table using the function defined eariler.
print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9")
print("-"*86)
makeTable(minimum, max, step)