'''
static method
we create static method when the fucntion does not 
change on the basis of object calling it
'''

class Employee:

    @staticmethod
    def greet():
        print("WELCOME!")


e1 = Employee()
e2 = Employee()

e1.greet()
e2.greet()