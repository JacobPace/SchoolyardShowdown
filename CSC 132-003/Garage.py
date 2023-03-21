class Car:
    def __init__(self, name):
        self.tires = 4
        self.engine = True
        self.owner = name

    def __str__(self):
        return f"Car: owner = {self.owner}, tires = {self.tires}, engine = {self.engine}"
    
c1 = Car("Jacob")
print(c1)