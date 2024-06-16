def fun1(i):
    return i%2 ==0
r1=range(1,11)
m=map(fun1,r1) # map functions only 1 time usable
f1=filter(fun1,r1) # filter functions
print("map.........")
for ele in m:
    print(ele,end=",")

print("\nfilter.........")

for ele in f1:
    print(ele,end=",")