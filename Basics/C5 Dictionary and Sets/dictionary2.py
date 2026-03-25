thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #The popitem() method removes the last inserted item
print(thisdict)


for x, y in thisdict.items():
  print(x, y)

for x in thisdict.keys():
  print(x)

for x in thisdict.values():
  print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)