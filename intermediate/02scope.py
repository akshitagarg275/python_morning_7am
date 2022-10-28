'''
namespaces
global -> it can be accessed throughout the program
local -> It can be accessed withinn a function
nonlocal
'''

# global variable
from re import A, X


a = 10
b = 30

def func():
    # local to the function func
    # a = 20

    # To access the global variable
    # global a
    # a = 50
    # print(globals()['b'])
    print("In func: ",a)

def outer():
    x = 20
    print("Outer x: ",x)

    def inner():
        # x = 40
        nonlocal x
        x = 40
        print("Inner x: ",x)
    inner()

    print("AFTER: Outer x: ",x)
# func()
# print("Outside: ",a)

outer()
