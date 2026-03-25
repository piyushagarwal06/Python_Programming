x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #true
print(x is y) #false
print(x == y) #true

print(x is not y) #The is not operator returns True if both variables do not point to the same object

