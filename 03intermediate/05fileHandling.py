'''
File Handling
text file - html , .txt, .doc ,.py
binary file - mp3,mp4,pdf,png

file = open(file_name , mode)

modes for text file
r - read mode (file should already exist)
w - write mode
a - append mode

modes for binary file
rb - read mode
wb -  write mode
'''

# file = open("./02scope.py", "r")
# print(file)
# data = file.read()
# print(data)

# print(file.readline())
# print(file.readline())

# print(file.readlines())

# print(file.read(10))
# file.seek(10)
# print(file.read(20))
# file.close()

# TODO: write mode(it overrides the previous content)
# file = open("./ex.txt" , 'w')
# # file.write("Hello")
# file.writelines(["jncjsnvj\n", "csjcnsdjkvn\n"])
# file.close()

# TODO: append mode (to add the content at the end)
# file = open("./ex.txt" , "a")
# file.write(" writing using append mode")
# file.close()

# Smarter way
# with open("./copy.txt", "w") as f1 , open("./02scope.py", "r") as f2:
#     for data in f2:
#         f1.write(data)

# print("files got automatically closed")

# TODO: Binary mode
# with open("./pic.png" , 'rb') as f1:
    # print(f1.read())
with open("./pic.png" , 'rb') as f1 , open("./copy.png" ,"wb") as f2:
    for data in f1:
        f2.write(data)