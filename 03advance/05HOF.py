'''
Everything im Python is an object including the functions.
Functions that take other functions as an argument are called as 
high order functions.
'''

def add(ele):
    return ele + 1

def cal(operator, num):
    return operator(num)

print(cal(add,5))