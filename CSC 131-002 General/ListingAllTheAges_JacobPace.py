##############################################################################
# author: Jacob Pace
# date: 11/ /2022
# description:List All the Ages
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def getNum():
    num = int(input("How many peoples' ages are you going to be comparing?: "))
    return num

# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def getNames(a,b):
    names = []
    while a >= 1:
        b += 1
        name = input(f"Please type person {b}'s name: ")
        names.append(name)
        a -= 1
    return names

# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def getAges(a,b):
    ages = []
    while a >= 1:
        b += 1
        age = int(input(f"How old is person {b}?: "))
        ages.append(age)
        a -= 1
    return ages

################################ MAIN ################################
# Ask for the number of people using one of the functions defined above.
counter = 0
num = getNum()
print("-"*50)

# Ask for the names of the people using one of the functions defined
# above.
names = getNames(num, counter)

# Ask for the ages of the people using one of the functions defined
# above.
ages = getAges(num, counter)

# Identify the names of the youngest and oldest people in the list.
ageIndex1 = 0
largest = ages[0]
for number in ages:
    if number > largest:
        largest = number
        ageIndex1 = ages.index(largest)

Index2 = 0
smallest = ages[0]
for age in ages:
    if smallest > age:
        smallest = age
        Index2 = ages.index(smallest)

calcAverage = 0
for inte in ages:
    calcAverage += inte
    average = calcAverage / num
    
# Display information about the lists.
print("-"*50)
print(f"{names[ageIndex1]} is the oldest at {largest} years old!")
print(f"{names[Index2]} is the youngest at {smallest} years old!")
print(f"The average of all the ages is {average}")