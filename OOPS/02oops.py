class Employee:
    # class property
    company = "ABC"


e1 = Employee()
print(e1.company)

e2 = Employee()

# instance attribute
e2.company = "XYZ"
print(e2.company)
print(e1.company)