a=input("Enter a word: ").lower()
s=['a', 'e', 'i', 'o', 'u',]
c=0
d=0
k=len(a)
for i in range(k):
    if(a[i] == " "):
        d+=1
        
    elif(a[i] in s):
        c+=1
        print(i, a[i])
print("vowels : ",c)   
print("all characters : ",len(a)-d)