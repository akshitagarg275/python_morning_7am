'''
operators
unary -> It will have only one operand
binary -> It will have two operands
    arithmetic
    assignment
    relational
    logical
    bitwise

membership
identity

'''

# TODO: unary

# a = -5

# TODO: arithmetic 
'''
+,- , / ,*

// -> floor divison (integer quotient)
% -> modulus operator (remainder)
** -> raise to the power of
'''
from ast import operator


n1 = 5
n2 = 2

# print("add is : ", n1 + n2)
# print("sub is : ", n1 - n2)
# print("multiplication is : ", n1 * n2)
# print("quotient is : ", n1 / n2)

# print("integer quotient is :", n1 // n2)
# print("remainder is :",n1%n2)

# print(5 ** 2)


# TODO: Assignment ('=')
a = 5

# a = a + 2
# a += 2

# a = a * 4
# a *= 4

# print(a)

# TODO: relational operators
'''
These return True/ False
> : greater than
< : less than
>= : greater than equal to

either LHS value is greater/less than or equal to RHS value

<= : less than equal to
== : equal to
!= : not equal to
'''

# print(5 > 3)

# print( 5 < 2 )

# print(5 >= 5)

# print(5 >= 2)

# print(4 <= 5)

# print(5 == 5)

# print(5 != 5)

# TODO: Logical operators
'''
and => logical and
when any one input is False output will be False

or => logical or
when any one input will be True output will be True

not => logical not
It changes the current
Falsy values -> False, 0 , None , ''
'''

# print(5 > 3 and 4 > 6)
# print(5 > 3 or 4 > 6)


# print(not 0)

# TODO: bitwise operators

'''
& -> logical and
| -> logical or
^ -> logical xor
>> -> right shift (It decreases the bits)
<< -> left shift  (It increases the bits)
'''

# print(bin(5))
# print(bin(11))

# print(5 & 11)
# print(5 | 10)

# print( 5 ^ 11)

# 

# print(10 >> 1)

# print(10 << 1)

# TODO: membership operator (in)

nums = [12, 13, 14, 15]
# print(13 in nums)
# print (16 in nums)

# name = "John"
# print('j' in name)

# print ('J' not in name)

# TODO: identity operator (is)

# a = 2
# print("id of a : ", id(a))

# b =2
# print("id of b : ",id(b))

# print ( a is b)

# l1 = [1, 2, 3]
# print("l1: ",id(l1))

# l2 = [1, 2, 3]
# print("l2: ",id(l2))

# print(l1 is l2)

# l3 = l1
# print("l3 is : ",id(l3))

# print(l1 is l3)