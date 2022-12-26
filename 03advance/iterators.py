'''
iterators are the objects that can be iterated upon

iterators -> any object that you can traverse is an iterator. An object will return data,
             one element at a time
It implements two special methods __iter__() and __next__(), known as iterator protocol

iterable -> An object is called iterable if we can get an iterator from it eg, list, tuples,string

iteration -> Repeating the process

we can iterate any object that can returm an iterator
'''

my_list = [1,2,3,4,5,6]

# for i in my_list:
#     print(i)

my_iter = iter(my_list)
# print(my_iter)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# while True:
#     try:
#         ele = next(my_iter)
#         print(ele)
#     except StopIteration:
#         break