ch=input("enter a character: ")[0].lower()
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print(ch,"is a vowel")
elif(ch>='0' and ch<='9'):
    print(ch,"is a digit")
else:
    print(ch,"is a consonant")

if('abc'>'ABC'):
    print("abc is greater than ABC")