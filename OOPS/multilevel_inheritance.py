'''
multilevel inheritance
p1

p2

C
'''

class A:
    def show(self):
        print("I am in class A")

class B ( A ):
    def show(self):
        super().show()
        print("I am in class B")

class C ( B ):
    def show(self):
        print("I am in class C")
        super().show()

obj = C ()
obj.show()