'''
RETURN vs YIELD
yield returns a value and pauses the execution while maintaining the internal states
return statement returns a value and terminated the execution of the function

when a generator is called, it returns an object(iterator) but doesnot start the execution immediately.
Local variables and their states are remembered between successive calls
'''

def counter_func(n):
    i=1
    while i<=n:
        return i
        i=i+1

# print(counter_func(3))

def counter_gen(n):
    i=1
    while i<=n:
        yield i
        i=i+1

my_gen = counter_gen(3)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))