# str1='the quick brown fox jumps over the lazy dog'
str1 = 'the quick brown fox jumps over'
a="abcdefghijklmnopqrstuvwxyz"
flag=True
for i in a:
    if i not in str1.lower():
        flag=False
        break
if flag==True:
    print("is a pangram")
else:
    print("is not a pangram")