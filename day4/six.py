class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("parent class constructor")
    def display(self):
        print("object state.....")
        print(f"a={self.a}")
        print(f"b={self.b}")

class child(parent):
    def add(self):
        return self.a + self.b

c1=child(100,200)
c1.display()
print(c1.add())

    