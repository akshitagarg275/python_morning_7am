'''
functions: DRY -> Donot Repeat Yourself
functions contain a set of code which can be called
any number of times

def function_name():
    #function_statements

'''
# function defination
def greetings():
    print("Hello")

# function calling
# greetings()
# greetings()

def profile(name , age):
    print(f"Name is : {name} and age is {age}")

# profile("John" , 34)
n = "Jane"
a= 23

# profile(n , a)

# profile(a , n)


def profile(name , age):
    print(f"Name is : {name} and age is {age}")

# keyword arguments
# profile(age = a , name = n)


# TODO: default parameters
# def profile(name ="NA" , age = "NA"):
#     print(f"Name is : {name} and age is {age}")
# NOTE: non-default argument cannot follow default argument
# def profile(name ="NA" , age):
#     print(f"Name is : {name} and age is {age}")


# profile("Jane")
# profile()
# profile(16)

# TODO: return statment

def calc(n1, n2):
    sum = n1 + n2
    sub = n1 - n2
    return sum , sub

# print(calc(2,4))

# ans , ans2 = calc(5,6)
# print(ans)
# print(ans2)


# TODO: variable length arguments

def func(*args):
    # print(args)
    # print(type(args))

    for i in args:
        print(i)

# func(12,1,4,5,6)

# TODO: variable length keyword arguments
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for k,v in kwargs.items():
        print(f"{k} --> {v}")

# func(fname = "John" , lname = "Doe" )


# TODO: Lambda functions
# Anonymous functions
# variable_name = lambda parameters : expression

# def isEven(num):
#     return num%2 == 0


# isEven = lambda num : num%2 == 0


# print(isEven(7))
# print(isEven(72))


func = lambda num : num**2 if num % 2 ==0 else num**3

# print(func(7))
# print(func(2))

nums = [1,2,3,4,5,6]

# TODO: map
sqr_list = list(map(lambda x : x**2 , nums))
# print(sqr_list)

# TODO: filter
# even = list(filter(lambda x : x%2==0 , nums))
# print(even)

# TODO: reduce

from functools import reduce

mul = reduce(lambda a,b : a*b , nums)
print(mul)
