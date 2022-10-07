'''
strings -> ' ' , " " , ''' '''
str()
ordered , immutable , iterable
'''




import email


s = 'python'
# print(s)
# print(type(s))

# for i in s:
#     print(i, end = "")

# print(len(s))

# print(s[0])
# print(s[-1])

# s[0] = 'P'

# TODO: slicing

s = 'python is pl'
# print(s[: :])
# print(s[: : -1])
# print(s[2:4])
# print(s[-3:])

# print(s.startswith('Py'))
# print(s.endswith('Py'))

# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())

# s = 'python is pl'
# print(s.find("pyh"))
# print(s.find("h",5))

# print(s.index("Pyh"))

# print(s.count('p'))

s = "python"
# print(s.isalpha())

# print(s.isalnum())

# contact = "77768"
# print(contact.isdigit())

# p = "   "
# print(p.isspace())

# print('for'.isidentifier())

#TODO: escape sequence

'''
\b - backspace
\n - new line
\t - tab
\' - '
\\ - \
'''

# path = r"C:\tmp\new_folder"
# print(path)

# TODO: strip
# password = "    xjbscjbc      "
# print(password.lstrip())
# print(password.rstrip())
# print(password.strip())


# TODO: format

n1= 2
n2 = 3
ans = n1 + n2
# 2 + 3 = 5

# print(str(n1) + ' + ' + str(n2) + ' = ' + str(ans))

# print("{} + {} = {}".format(n1,n2,ans))
# print("{1} + {0} = {2}".format(n1,n2,ans))

# print(f"{n1} + {n2} = {ans}")

# TODO: replace
s = "we are learning"
# print(s.replace('a' , '@'))
# print(s.replace('a' , '@' , 1))


# TODO: split
# print(s.split())
# print(s.split('e',2))


# TODO: join

fname = 'jon'
lname = "doe"
uname = ".".join([fname,lname])
print(uname)

domain ="abc.com"
email = '@'.join([uname,domain])
print(email)