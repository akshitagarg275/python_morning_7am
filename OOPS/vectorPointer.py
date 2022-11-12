'''
2D Vector: 5i^ + 6J^
3D Vector: 5i^ + 6J^ + 9k^
'''

class Vec2D:

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^")

class Vec3D(Vec2D):

    def __init__(self, i, j , k):
        super().__init__(i, j )
        self.kcap = k
    
    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")

obj2 = Vec2D(5 , 6)
obj2.show()

obj3 = Vec3D(5, 6, 7)
obj3.show()