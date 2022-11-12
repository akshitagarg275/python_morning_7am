'''
len() = __len__

> = __gt__
'''

class Num:

    def __init__(self, num):
        self.num = num

    def __gt__(self, other):
        return self.num > other.num

    def __add__(self,other):
        return self.num + other.num
    
    def __str__(self):
        return "It is an object of Num class"

n1 = Num(2)
n2 = Num(6)

print( n1 > n2)
print(n1 + n2)
print(n1)
