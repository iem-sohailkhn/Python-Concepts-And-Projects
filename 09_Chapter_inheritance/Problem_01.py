class TwoDVector:
    def __init__(self,i,j):
        self.j=j
        self.i=i
    def show(self):
        print(f"The Vector of 2D is {self.i}i + {self.j}j")
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"The Vector of 3D is {self.i}i + {self.j}j + {self.k}k")
a=TwoDVector(2,3)
a.show()
b=ThreeDVector(4,5,6)
b.show()
