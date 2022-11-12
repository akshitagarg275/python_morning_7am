'''
Constructor: It is the first function that gets called
when an object is created

It gets called by itself when an object is created

def __init__(self)


'''

class Employee:
    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.sal = salary
        # print("This is a constructor")

    def getDetails(self):
        print(f"emp name is {self.name} and salary is {self.sal} and company name is {self.company}")

    @classmethod
    def changeCompany(cls, new_name):
        cls.company = new_name
    
    # Changing class attribute using object
    # def changeCompany(self, new_name):
    #     self.__class__.company = new_name

e1 = Employee("John" , 1000000)
e2 = Employee("Jane" , 2000000)

# Employee.changeCompany("XYZ")

e1.changeCompany("PQR")


e1.getDetails()
e2.getDetails()

