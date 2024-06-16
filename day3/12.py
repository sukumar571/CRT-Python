def fun1(ele):
    return ele**3
r1=range(1,11)
m=map(fun1,r1) # map functions only 1 time usable

for ele in m:
    print(ele)