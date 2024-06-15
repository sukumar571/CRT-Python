l1=[10,10,20,30,40,30.47,3+4j,"suku"]
print("l1=",l1)
print("id of l1=",id(l1))

l1.append(10000) #append method
print("l1=",l1)
print("id of l1=",id(l1))

l2=l1.count(10) #count method
print(l2)

l1.copy() #copy method
print(l1)

l1.extend([1,2,3,4,5,6]) #extend method
print(l1)

l1.insert(6,22) #insert method
print(l1)

l1[6]=2500 #replace method
print(l1)

l1.pop() #remove from last method
print(l1)

l1.pop(1) #remove from index method
print(l1)

l1.remove(10000) #remove element method
print(l1)

l1.reverse() #reverse method
print(l1)

l1.clear() #clear
print(l1)

l1.sort() #sort method produces error because the data types are different
print(l1)