class Emp:
    company="Google" #static variable
    def __init__(self,eno,ename,sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal
    #instance method
    def dispaly(self):
        print("object.....state....")
        print(f"Eno={self.eno}")
        print(f"Eno={self.ename}")
        print(f"Eno={self.sal}")

e1=Emp(100,"sukumar",100000)
e2=Emp(101,"basha",200000)
print(Emp.company)
e1.dispaly()
e2.dispaly()