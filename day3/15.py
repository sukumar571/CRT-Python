from functools import reduce
def fun1(a,b):
    return a*b
n=int(input("enter a value: "))
r2=reduce(fun1,range(1,n+1))
print(r2)
