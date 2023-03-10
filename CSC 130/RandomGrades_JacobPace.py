##################################################################
# author: Jacob Pace
# date: 11/6/2022
# desc: Random Grade Assignments
##################################################################
from random import randint
# Constants defined to limit the scope of the randomly generated grades.
lowest = 65
highest = 100

# A function that prompts the user for the number of students in the class.
def getStudents():
    num = int(input("How many students are in the class?: "))
    return num

# A function that recieves the number of students as a calling argument, and
# creates a list of random integers of that size.  The complete list is
# returned to the caling statement.
def makeList(a):
    grades = []
    while a > 0:
        rand = randint(lowest, highest)
        grades.append(rand)
        a -= 1
    return grades

# A function that recieves a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.
def getGrade(a):
    if (a >= 90 and a <= 100):
        a = "A"
    elif (a <= 89 and a >= 80):
        a = "B"
    elif (a <= 79 and a >= 70):
        a = "C"
    elif (a <= 69 and a >= 65):
        a = "D"
    return a

# A function that recieves a list of values, and prints them in order
# separated by a tab space.
def sortList(a):
    print(*a, sep='\t')

# A function that recieves a list of values (corresponding to
# the numerical grades), and creates a list of corresponding letter
# grades.  This list of letter grades is then returned to the calling statement.
def makeGrades(a):
    b = []
    for num in a:
        num = getGrade(num)
        b.append(num)
    return b

# A function that recieves a list of numerical values, and returns the
# mean/average of that list
def getAverage(a, b):
    add = sum(a)
    average = add / b
    return average

######################################## MAIN #####################################

# Using functions defined above, get the class size, numerical grade
# list, and letter grade list.
classSize = getStudents()
numberGrades = makeList(classSize)
grade = makeGrades(numberGrades)
average = getAverage(numberGrades, classSize)

# Print out both numerical and letter grades as well as the average
print("Numerical Grades:")
sortList(numberGrades)
print("Letter Grades:")
sortList(grade)
print(f"The average for the class is {average}!")