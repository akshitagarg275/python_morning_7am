'''
multiple inheritance

when a child class has 2 parent classes

MRO ->Method Resolution Order
'''

class A:
    def show(self):
        print("I am in class A")

class B:
    def show(self):
        print("I am in class B")

class C ( B, A ):
    def display(self):
        print("I am in class C")
    
# obj = C()
# obj.show()

class Person:
    eyes = 2

    def breathe(self):
        print("I do breathe...")

class Employee :
    company = "ABC"
    salary = 20000

    def breathe(self):
        print("Breathing somehow.....")


class Programmer ( Person, Employee):
    language = "Python"

    def __init__(self, name):
        self.name = name

    def breathe(self):
        print("Hardly gets time to breathe....")
        super().breathe()
        super().breathe()

p1 = Programmer("John")
p1.breathe()