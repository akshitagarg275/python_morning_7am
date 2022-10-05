'''
jump statements 
break -> to stop the loop
continue -> to skip the iteration
pass
'''

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if i ==3:
#         continue
#     print(i)

# for i in range(5):
#     if i ==3:
#         pass
#     print(i)


'''
else part of the loop 
will not get executed if the 
loop is explicitly terminated
'''

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("I am else block")


# TODO: WAP to find whether the given no is prime or not
# 13 -> 1, 13 prime
# 9 -> 1 , 3, 9 Not a prime
num = int(input("enter the num: "))

for i in range(2 , num):
    if num % i == 0:
        print("It is not a prime no")
        break
else:
    print("It is a prime no")

