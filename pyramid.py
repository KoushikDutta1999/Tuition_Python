# Python Program using Constructor to print Full Pyramid, Full Inverted Pyramid and Diamond Pattern

class pattern:
    def __init__(self,n):
        self.n = n
        
    def full_py(self):
        print("Full Pyramid")
        k = self.n-2
        for i in range(1,self.n+1):
            for j in range(0,k+2):
                print("",end=" ")
            for j in range(1, i+1):
                print("*",end=" ")
            print(" ")
            k-=1
#------------------------------------------
    def invert(self):
        print("Full inverted Pyramid")
        k = 1
        for i in range(self.n,0,-1):
            for j in range(0,k):
                print("",end=" ")
            for j in range(1, i+1):
                print("*",end=" ")
            print()
            k+=1
#------------------------------------------
    def diamond(self):
        print("Diamond Patter")
        k = self.n-2
        for i in range(1,self.n+1):
            for j in range(0,k+2):
                print("",end=" ")
            for j in range(1, i+1):
                print("*",end=" ")
            print(" ")
            k-=1
        k = 1
        for i in range(self.n,0,-1):
            for j in range(0,k):
                print("",end=" ")
            for j in range(1, i+1):
                print("*",end=" ")
            print()
            k+=1
obj=pattern(5)
obj.full_py()
obj.invert()
obj.diamond()