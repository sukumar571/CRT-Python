class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"Name={self.name}")
        print(f"RollNo={self.rollno}")
        print(f"Marks={self.marks}")
        print("-----------------------")
e1=student("Basha",596,0)
e2=student("Sukumar",571,100)
e3=student("Nanrutha",588,50)
e1.display()
e2.display()
e3.display()