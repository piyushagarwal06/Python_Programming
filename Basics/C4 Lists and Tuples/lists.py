a=["142",142,142.1,False]
print(a)
a[0]="Grapes" #lists are mutable
print(a)

a.append("Bharat")
print(a)

l1=[1,34,62,2,55,134]
print(l1.sort()) #output = None as list.sort() sorts the list in place and returns None.

print(sorted(l1))#output=sorted list

l1.insert(2,3333333)
print(l1)  #output=[1, 2, 3333333, 34, 55, 62, 134]
print(l1.insert(2,4543254)) # output=None

print(l1.pop(3))
print(l1)
