class Complex:
    def __init__(self, a=0,b=0):
        self.a = a
        self.b = b
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        self._a = value
    
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, value):
        self._b = value

    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b}i"

    def __sub__(self, other):
        return f"{self.a - other.a} - {abs(self.b - other.b)}i"

    def __mul__(self, other):
        return f"{(self.a*other.a-self.b*other.b)} + {(self.a*other.b+self.b*other.a)}i"

    def __truediv__(self, other):
        return f"{self.a*(other.a/(other.a**2+other.b**2))*self.b} - {abs(self.a*((other.b/(other.a**2+other.b**2)))*self.b)}i"
    
    def __eq__(self, other):
        if (self.a == other.a and self.b == other.b):
            return "True"
        else:
            return "False"

    def reciprocal(other):
        return f"{other.a/(other.a**2+other.b**2)} - {abs(other.b/(other.a**2+other.b**2))}i"
    
    def conjugate(self):
        if self.b<=0:
            return f"{self.a} + {abs(self.b)}i"
        else:
            return f"{self.a} - {self.b}i"

    def __str__(self):
        if self.b>=0:
            return f"{self.a} + {self.b}i"
        else:
            return f"{self.a} - {abs(self.b)}i"