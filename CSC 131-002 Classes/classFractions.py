class Fraction:
    def __init__(self, num = 1, den = 1):
        self.num = num
        if den == 0:
            self.den = 1
        else:
            self.den = den

    #Getter for the numerator
    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, num):
        self._num = num

    #Getter for the denominator
    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, den):
        self._den = den

    #Calculates the fractions decimal value as a float
    def getReal(self):
        return float(self.num) / self.den

    # magic function to allow us to call an instance
    # and get a string representation of the fraction class
    def __str__(self):
        return f"{self.num}/{self.den} = {self.getReal()}"

#main
f1 = Fraction() #0/1
f2 = Fraction(1, 2) #1/2
f3 = Fraction(0, 0) #0/1
print(f1)
print(f2)
print(f3)
