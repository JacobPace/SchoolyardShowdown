#######################################################################
# author: Jacob Pace
# date: 12/5/2022
# desc: A program that asks for a limit and finds all prime numbers from 1 to that limit and returns it to the user
########################################################################

# A function to prompt the user for a number and return that value to
# the calling statement.
def getNum():
    a = int(input("Please input an integer for a limit: "))
    return a

# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def checkIfPrime(a):
    if a > 1:
        for n in range(2, a):
            if a % n == 0:
                return False
        else:
            primes.append(a)
            return True
    else:
        return
        
################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.
limit = getNum()
primes = []
def output(a):
    for i in range(1, a, 1):
        i = checkIfPrime(i)
    return

if limit >= 1:
    output(limit)
    print(f"There are {len(primes)} prime numbers less than {limit}.")
    print(primes)
else:
    print(f"There are 0 prime numbers less than {limit}.")

