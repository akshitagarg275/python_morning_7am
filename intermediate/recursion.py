'''
recursion -> self calling function is recursion
In recursion we split a bigger problem to a smaller ones
then we try to solve the smaller problem first which eventually
will solve the bigger one.

Base Case
solving smaller problem
'''

# WAP to find sum of first n nums
# n = 5
# 1 + 2 + 3 + 4 + 5
'''
f(5) = 5 + f(4)
f(4) = 4 + f(3)
f(3) = 3 + f(2)
f(2) = 2 + f(1)
f(1) = 1
'''
def func(n):
    # base case
    if n == 1:
        return 1
    return n + func(n-1)

# print(func)

# WAP to find fiboancci series
# 0 1 1 2 3 5 8 13

def fib(n):
    # base case
    if n==1 or n==0:
        return n
    
    return fib(n-1) + fib(n-2)

# print(fib(5))

for i in range(5):
    print(fib(i) , end=" ")

# WAP to find factorial of a given num
# WAP  a program to find power using recursion

# pow(2, 3) = 2*2*2 = 8







