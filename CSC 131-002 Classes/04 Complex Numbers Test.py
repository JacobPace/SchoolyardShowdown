###################################################################
# name:         anky
# date:         28th December, 2020
# Description:  Test program to check on the creation of a Complex
#               Number class
# Make sure that your complex class design is in  a file called
# Complex.py and that it is in the same folder as this ComplexTest.py
# file. You will only be required to submit the Complex.py file for the
# assignment. 
##################################################################

# DO NOT CHANGE ANYTHING IN THIS FILE. ALL ADJUSTMENTS TO MAKE THIS WORK
# SHOULD BE DONE IN YOUR Complex.py FILE WHERE THE COMPLEX NUMBER CLASS
# EXISTS.

from Complex import *   # import everything from the Complex.py file.

# Testing creation and printing of the Complex number objects
a = Complex(4, 5)
b = Complex(2, 6)
c = Complex(4, -3)
d = Complex()
e = Complex(-3)
print("a = {}".format(a))
print("b = {}".format(b))
print("c = {}".format(c))
print("d = {}".format(d))
print("e = {}".format(e))
print("-" * 50)

# Testing reciprocal, equality, and the conjugate
d = b.reciprocal()
e = c.reciprocal()
print("1/({}) = {}".format(b, d))
print("1/({}) = {}".format(c, e))
print("{} == {}: {}".format(a, b, (a==b)))
d = c
print("{} == {}: {}".format(c, d, (c==d)))
print("({})* = {}".format(c, c.conjugate()))
print("({})* = {}".format(a, a.conjugate()))
print("-" * 50)

# Testing mathematical operators
print("({}) + ({}) = {}".format(a, b, (a+b)))
print("({}) + ({}) = {}".format(a, c, (a+c)))
print("({}) - ({}) = {}".format(a, b, (a-b)))
print("({}) - ({}) = {}".format(c, a, (c-a)))
print("({}) * ({}) = {}".format(a, b, (a*b)))
print("({}) * ({}) = {}".format(b, c, (b*c)))
print("({}) / ({}) = {}".format(a, b, (a/b)))
print("({}) / ({}) = {}".format(c, b, (c/b)))
print("=" * 50)
