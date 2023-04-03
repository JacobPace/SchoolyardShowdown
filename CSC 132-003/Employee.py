#####################################################################
# author:  Jacob Pace     
# date:    4/3/2023
# description:  Employee Homework Assignment
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################
class Employee(ABC):
    def __init__(self, firstname="", lastname="", pay=0, position=None):
        self.firstname = firstname.replace(" ", "").lower().capitalize()
        self.lastname = lastname.replace(" ", "").lower().capitalize()
        self.pay = pay
        self.email = self.createEmail()
        self.position = position

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
        if value < 20000:
            value = 20000
        self._pay = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if ("@latech.edu" not in value):
            pass
        else:
            self._email = value

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        self._position = value
    
    def createEmail(self):
        return f"{self.firstname}.{self.lastname}@latech.edu".lower()
    
    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email})"
    
    def fixNames(self):
        self.firstname=self.firstname.replace(" ", "").lower().capitalize()
        self.lastname=self.lastname.replace(" ", "").lower().capitalize()
    
    @abstractmethod
    def applyRaise(self, rate):
        raise NotImplementedError("Not implemented for superclass!")


######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self, firstname = "", lastname = "", position = "", pay = 50000):
        Employee.__init__(self, firstname, lastname, pay)
        self.position = position
        self.pay = 50000
    
    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self, value):
        self._pay = value

    def applyRaise(self, rate):
        if rate > 0:
            self.pay *= rate
        else: self.pay = self.pay

    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email}) -- {self.position}"
    

######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################
class Staff(Employee):
    def __init__(self, firstname="", lastname="", pay =40000):
        Employee.__init__(self, firstname, lastname, pay)
        self.pay = 40000

    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self, value):
        self._pay = value

    def applyRaise(self, rate):
        if rate > 0:
            self.pay += rate
        else:
            self.pay = self.pay

