'''
iter() --> __iter__()
next() --> __next__()

For building custom iterator we need to implement  __iter__() and __next__() methods
__iter__() methods returns the iterator object itself
__next__() metho retutn teh next item in the sequence. On reaching the last element it must
raise StopIteration

'''

class Number:
    def __init__(self, number=0):
        self.num = number
    
    def __iter__(self):
        self.ele = 0

        return self

    def __next__(self):
        if self.ele < self.num:
            res=self.ele
            self.ele = self.ele + 1
            return res
        else:
            raise StopIteration

n = Number(5)

my_iter = n.__iter__()
# print(my_iter)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())