e=set()
s={1,2,3,4,5,5,4,3,2,1,"Harry"}
print(s)

s.add("ssp")
s.remove(2) #removes duplicate calues as well

print(s,type(s))


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")  #If the item to remove does not exist, remove() will raise an error.
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  #Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print(x)
print(thisset)