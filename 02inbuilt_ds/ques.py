# 1) Write a python function to find the digital root of a number.
# (To find digital root, you need to add the digits of a number till you get a single digit 
# number. That is say you have 56789. In the first iteration you add 5, 6, 7, 8 and 9. 
# The result is 35. In the second iteration you add 3 and 5. You get 8. So 8 is the 
# answer.)

def digitalroot(num):
    flag=True
    while(flag):
        r=0
        n=num
        print(n)
        sum = 0
        while(n > 0):
            r=n%10
            sum += r
            n//=10
            print(n)
        # num=r
        if(sum%10==0):
            print("1")
            flag=False
            print(sum)
            break
num=int(input("Enter a number: "))
digitalroot(num)

