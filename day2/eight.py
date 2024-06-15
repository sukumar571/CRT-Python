#unpacking example
def fun(a, b=0,c=0):
    return a + b + c

print(fun(10))
print(fun(10, 20, 30))
x=fun(*[10, 20, 40])
print(x)