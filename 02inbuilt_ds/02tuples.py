'''
tuples -> ()
tuple()

iterable , ordered , immutable
'''

from ctypes import sizeof


fruits = ("mango", "apple", "banana", "papaya", "grapes", "guava")

# print(fruits)
# print(type(fruits))

# for i in fruits:
#     print(i)

# print(fruits[0])
# print(fruits[-1])

# fruits[0] = "orange"

# TODO: slicing
# print(fruits[ : : -1])

# print(fruits.count("mango"))

# print(fruits.index("mango"))

# print( (1, 2) + (3, 4))

# tup = ( [1, 2] , [3, 4] )
# print(tup)
# print(tup[0][1])
# tup[0][1] = 5
# print(tup)

tup = (1, 2, 3)
print(tup.__sizeof__())
li = [1, 2, 3]
print(li.__sizeof__())
