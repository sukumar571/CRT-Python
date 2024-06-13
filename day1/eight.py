a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

if a > b and a > c:
    print("a is greater")
elif(a==b and a>c):
    print("a,b are greater than c")
elif(a==c and a>b):
    print("a,c are greater than b")
elif b > a and b > c:
    print("b is greater")
elif (b==c and b>a):
    print("b,c are greater than a")
elif c > a and c > b:
    print("c is greater")
elif(a==b and a>c):
    print("a,b are greater than c")
else:
    print("all are equal")
