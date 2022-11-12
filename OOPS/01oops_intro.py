'''

# OOPS -> Object Oriented Programming System

class -> It is a blueprint

object -> instance/entity of the class

variables are known as properties in class
functions are known as methods in class

4 pillars of OOPS
1) Abstraction -> unnecessary details are hidden
2) Encapsulation -> it combines properties(variables) and methods(functions) in a class
3) Inheritance -> child class(derived class) inherits the properties and methods from parent class(super class)
4) Polymorphism-> poly (many) + morph(forms)

2 + 2 = 4
'2' + '2' = 22

classes will be named on the basis of Pascal Convention
SuperMan


until and unless an object is not created, till then there is no memory allocation

class do not reserve any space in the memory
objects reserve the memry space

'''

class Employee:
    company = "ABC"

    def greeting(self):
        print("WELCOME!")   
        print(self)     

# object_name = class_name()

e1 = Employee()
e2 = Employee()
# print(e1)
e1.greeting()
e2.greeting()
# just for learning -> greeting(e1)


# print(e1.company)

print(type(5))