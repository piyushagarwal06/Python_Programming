thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  #removes the last item.
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist



thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)