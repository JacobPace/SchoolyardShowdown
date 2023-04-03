class Test:
    def __init__(self, firstname = "", lastname="", pay = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    @property
    def firstname(self):
        return self._firstname
    @firstname.setter
    def firstname(self, value):
        self._firstname = value.replace(" ", "").lower().capitalize()

    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self, value):
        self._lastname = value.replace(" ", "").lower().capitalize()

    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self, value):
        if self._pay < 20000
        self._pay = value

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
p1 = Test(" laUrA", "Jon es")
p2 = Test("JoH n", " jAmes")
print(p1)
print(p2)
p1.firstname = " JonAthAn"
print(p1)