from functools import reduce
def fun1(a,b):
    return a+b
r1=range(1,11)
r2=reduce(fun1,r1)
print(r2)
