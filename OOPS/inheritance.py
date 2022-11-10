'''

inheritance -> inheriting attributes and methods from the parent class

single inheritance
multiple inheritance
multilevel in

'''

# class A:
#     def show(self):
#         print("I am in class A")

# class B(A):
#     def show2(self):
#         print("I am in class B")

# obj = B()
# obj.show()


class Company:
    company = "ABC"

    @staticmethod
    def greet():
        print("WELCOME")

class Employee(Company):

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name is {self.name}")

obj = Employee("John")

obj.show()
obj.greet()
