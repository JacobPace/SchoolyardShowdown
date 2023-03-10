#################################################################################
# name: Jacob Pace
# date: 10/13/2022
# description: Number Properties HW 3
#################################################################################

# A function that prompts the user for a number and returns it.
def getNum():
    number=int(input("Input a number: "))
    print(f"You typed {num}")
    return number

# A function that receives two numbers as arguments, and returns the
# larger of the two numbers.
def larger(a,b):
    if a > b:
        return a
    else:
        return b

# A function that receives three numbers as arguments, and returns the
# largest of the three numbers.
def largest(a,b,c):
    print(larger(larger(a,b),c), "is the largest number you entered!")
    return larger(larger(a,b),c)

# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def productOfLargest(a,b,c):
    global count
    count = 0
    while count<2:
        if a>b and a>c and b>c:
            count+=1
            largest(a,b,c)
            print(a*b, "is the product of the two largest numbers you entered!")
            return a*b
        elif c>a and c>b and a>c:
            count+=1
            largest(a,b,c)
            print(c*a, "is the product of the two largest numbers you entered!")
            return c*a
        elif c>a and c>b and b>a:
            count+=1
            largest(a,b,c)
            print(c*b, "is the product of the two largest numbers you entered!")
            return c*b 

# A function that receives an argument and returns a string representing
# whether that argument is even or odd.
def isEven(e):
    if (e % 2) == 0:
        e="Even"
        return e
    else:
        e="Odd"
        return e

# A function that receives an argument and determines whether that
# argument is a prime number.
def isPrime(prime):
    global check
    check = 2
    if prime > 1:
        while check <= (prime/2):
            if (prime % check ) == 0:
                prime="False"
                return prime
            else:
                prime="True"
                return prime
    else:
        prime="False"
        return prime

##################################### MAIN PROGRAM #######################
# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################


# Prompt for three different numbers and store them appropriately.
def getNums():
    global num
    num = int(input("Please type a number!: "))
    return num

#Variables for final output
num1=getNums()
num1Even=isEven(num1)
num1Prime=isPrime(num1)

num2=getNums()
num2Even=isEven(num2)
num2Prime=isPrime(num2)

num3=getNums()
num3Even=isEven(num3)
num3Prime=isPrime(num3)

# Print out the table header information.
print("----------------------")
print("Num\tEven\tPrime")
print("----------------------")
# Print out the table contents for each of the three numbers.
#print(f"{a}\t{aEven}\t{aPrime}")
print(f"{num1}\t{num1Even}\t{num1Prime}")
print(f"{num2}\t{num2Even}\t{num2Prime}")
print(f"{num3}\t{num3Even}\t{num3Prime}")
# Print out the identity of the largest number and the largest product
# from the given numbers.
productOfLargest(num1,num2,num3)