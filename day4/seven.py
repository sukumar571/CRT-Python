class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("parent class constructor")
    def display1(self):
        print("object state.....")
        print(f"a={self.a}")
        print(f"b={self.b}")

class child(parent):
    def __init__(self,a,b,c,d):
        parent.__init__(self,a,b)
        self.c=c
        self.d=d
        print("parent class constructor")
    def display2(self):
        print("object state.....")
        print(f"c={self.c}")
        print(f"d={self.d}")
    def add(self):
        print("a+b=",self.a+self.b)
        print("c+d=",self.c+self.d)

c1=child(100,200,300,400)
c1.display1()

c1.display2()
c1.add()
    