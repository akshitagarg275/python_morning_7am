'''
DRY -> Donot Repeat Yourself
Loops -> these help in exceuting certain code for certain no of times

for loop
while loop

initalisation
condition
re-initialization (updation)
'''

# print("Hello")
# print("Hello")
# print("Hello")

# i = 1

# while i <= 5:
#     print("Hello: ", i)
#     i = i +1

# TODO: WAP to print nums from 5 to 1

# i = 5

# while i >= 1:
#     print(i)
#     i = i - 1


# TODO: WAP to print even nums till 10

# i = 0

# while i <= 10:
#     print(i)
#     i = i + 2

# i = 0
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i = i + 1 


'''
for loop -> it is used on iterables (list, tuple, set, dictionary)



'''

# nums = [23, 34, 56, 67]

# for n in nums:
#     print(n)

# name = "John Doe"

# for i in name:
#     print(i, end = "")

# for i in range(5):
#     print(i)


# TODO: WAP to count no digits in a number entered


num = int(input("enter a num: "))
# 12 -> 2
# 456 -> 3
count = 0
while num > 0 :
    rem = num % 10
    count =count + 1
    num = num // 10

print("No of digits: ",count)

# TODO: 234 = 2+ 3+ 4 =9

# num = int(input("enter a num: "))

# sum = 0
# while num > 0 :
#     rem = num % 10
#     sum =sum + rem
#     num = num // 10

# print("sum of digits: ",sum)


# TODO: WAP tp reverse a num
# 234 -> 432

# num = int(input("enter a num: "))

# reverseNum = 0
# while num > 0 :
#     rem = num % 10
#     reverseNum = (reverseNum * 10) + rem
#     print("rev: ", reverseNum)
#     num = num // 10

# else: 
#     print("reverse is: ", reverseNum)

# TODO: WAP to find whether given num is pallindrome or not
# 234 = 432
# 121 = 121
