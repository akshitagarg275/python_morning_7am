'''
GENERATORS:
It is a kind of function only. It generates a sequence of values that we can iterate on.
Unlike functions, generators doesn't terminate after returning a value
yield keyword is used in generators
Like list , tuple, generator is also an iterable
'''

def my_generator():
    n = 1
    print("First time: ")
    yield n

    n = n+1
    print("Second Time: ")
    yield n

my_gen = my_generator()
# print(my_gen)

print(next(my_gen))
print(next(my_gen))