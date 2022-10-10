'''
dictionary -> {key : value}
dict()
immutable, ordered , iterable
keys of a dictionary can only be the immutable datatypes
tuple, string, int
'''

# user = {}
# print(user)
# print(type(user))

user = {
    "fname" : "John",
    "lname" : "Doe",
    "age"   : 23,
    "country" : "US"
}

# print(user)
# print(user["fname"])
# print(user["course"])

# user["age"] = 25
# print(user)

# user.update([("age" , 25) , ("gen", "M")])
# user.update({"course" : ["python" , "django"]})
# print(user)

# print(user.keys())
# print(type(user.keys()))

# print(user.values())
# print(type(user.values()))

# print(user.items())
# print(type(user.items()))

# for k , v in user.items():
#     print(f"key is {k} and value is {v}")

# print(user.get("course"))
# print(user.get("course" , "-1" ))

# print(user)
# print(user.pop("age"))
# print(user)

# print(user)
# print(user.popitem())
# print(user)

#TODO WAP to find frequency of each chracter in string
# HAHA -> {'H' : 2 , 'A' : 2}

# st = "HAHA"
# st = "HAha"
# freq = {}

# for i in st:
#     if freq.get(i.lower()) == None:
#         freq[i.lower()] = 1
#     else:
#         freq[i.lower()] = freq[i.lower()] + 1
# print(freq)

para = "Hey we are learning python are we python"
# print(para.splitlines())
print(para.split())

