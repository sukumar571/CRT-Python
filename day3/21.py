a=0
b=0
c=0

try:
    a=int(input("enter a value: "))
    b=int(input("enter b value: "))
    c=a/b
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("zero is not a valid")
finally:
    print("finally block")
print(f"{a}/{b}={c}")