###########################################################################
#name: Jacob Pace
#date: 1
#description: Blocks in a pryramid HW
###########################################################################

#A function to prompt the user for the number of levels that pyramid will have
#and return it to the calling statement
def levelInput():
    numLevels=int(input("How many levels does your pyramid have?: "))
    return numLevels
        
#A function that recives the number of pyramid levels and the number of blocks as arguments
#and prints the appropriate results to the screen
def outPut(a,b):
    print(f"Your pyramid has {a} levels and it has {b} blocks!")

#A recursive function that recives the number of levels, calculates the number of blocks required, and
#returns the result to the calling statment
def calcBlocks(a,b):
    while(a>=1):
        a -= 1
        b += (a**2)
        calcBlocks(a,b)
    return b
       
#################################MAIN##############################################
#Using the function(s) defined above, ask the user for the number of pyramid levels
levels=levelInput()
blocks = (levels**2)

#Using the function(s) defined above, calculate and display the final results
outPut(levels, calcBlocks(levels,blocks))