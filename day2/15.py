d1={
    1:"sukumar",
    2:"basha",
    3:"kalyan",
    4:"vinay",
    5:"nagoor",
    6:"prudhvi"
}
print(d1.get(1)) #get method
l1=d1.keys() #keys method
l2=d1.values() #values method
print(l1)
print(l2)

d1.pop(1) #remove method
print(d1)

d1.popitem() #remove method
print(d1)

d1.update({6:"ramu"})  #update method
print(d1)

d1.update({2:"shiva"}) #update method
print(d1)

val=d1.setdefault(3,"kalyan") #set default
print(val)

value=d1.setdefault(1,"basha") #set default
print(value)
print(d1)


student_marks=dict.fromkeys(range(1,81)) 
student_marks.update({1:(60,70,80,90,95)})
print(student_marks)