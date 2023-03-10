class Vehicle:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

        @property
        def year(self):
            return self._year
        @year.setter
        def year(self, value):
            self._year = value

        @property
        def make(self):
            return self._make
        @make.setter
        def make(self, value):
            self._make = value

        @property
        def model(self):
            return self._model
        @model.setter
        def model(self, value):
            self._model = value

    def __str__(self):
        return f"Year: {self.year}\nMake: {self.make}\nModel: {self.model}"

class Engine:
    def __init__(self, kind):
        self.kind = kind

        @property
        def kind(self):
            return self._kind
        @kind.setter
        def kind(self, value):
            self._kind = value

    def __str__(self):
        return f"V6"

class DodgeRam(Vehicle):
    make = "Dodge"
    model = "Ram"

    def __init__(self, name=None, year=None):
        super().__init__(year, DodgeRam.make, DodgeRam.model)
        self.name = name

        @property
        def name(self):
            return self._name
        @name.setter
        def name(self, value):
            self._name = value

    def __str__(self):
        return f"Name: {self.name}\n{super().__str__()}\nEngine: {Engine.kind}"

d1 = DodgeRam("me", 1999)
eng = Engine("V6")
print(d1)
