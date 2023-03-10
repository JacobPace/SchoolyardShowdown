#############################################################
# author: Jacob Pace
# date: 1/25/2023
# desc: Simple Patient Class Reloaded
#############################################################

# The patient class has a name, age, and weight. Only the name and age
# are provided as arguments to the constructor. The weight is set to 150
# by default for all objects. A Patient also has an increaseAge function
# that increases the age by 1.
class Patient:
    def __init__(self, patient_name, patient_age):
        self.name = patient_name
        self.age = patient_age
        self.weight = 150
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def increaseAge(self):
        self.age += 1
        self._age = self.age
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if weight >= 0 and weight <= 1400:
            self._weight = weight
        else:
            weight = 150

# An In class which is a subclass of the Patient class and refers to an
# in-patient. An in-patient also contains a "stay" instance variable 
# that stores the number of days that that patient will stay in the
# hospital. Its constructor receives the name, age and stay duration as
# arguments. On top of appropriate accessors and mutators, the In class
# also has a __str__ function to define how an In object would be printed.
class In(Patient):
    def __init__(self, name, age, stay=0):
        super().__init__(name, age)
        self.stay = stay
    @property
    def stay(self):
        return self._stay
    @stay.setter
    def stay(self, stay):
        if stay >= 0:
            self._stay = stay
        else:
            self._stay = 0

    def __str__(self):
        return f"IN-\t{self.name}\t{self.age}\t{self.weight}\t{self.stay}"

# An Out class, which is a subclass of the Patient class and refers to
# an out-patient. An outpatient receives the name and age as arguments
# to its constructor. It also has a __str__ function that defines how an
# Out object would be printed.
class Out(Patient):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"OUT-\t{self.name}\t{self.age}\t{self.weight}"

# An ICU class which is a subclass of the In class and refers to a
# patient in the ICU. The ICU class receives the name and age as
# arguments to its constructor. It also has a class variable called days
# with the value 5 stored in it. This class variable is used to
# determine what the stay of the patient will be.
class ICU(In):
    def __init__(self, name, age, days=5):
        super().__init__(name, age)
        self.days = days

    @property
    def days(self):
        return self._days
    @days.setter
    def days(self, days):
        if days >= 0:
            self._days = days
        else:
            self._days = 0

    def __str__(self):
        return f"IN-\t{self.name}\t{self.age}\t{self.weight}\t{self.days}"

# A CheckUp class which is a subclass of the Out class and refers to a
# patient who is getting a checkup at the hospital. It receives the name
# and age as arguments for its constructor.
class CheckUp(Out):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"OUT-\t{self.name}\t{self.age}\t{self.weight}"