name = "Bharat"
print(name.endswith("rry"))
print(name.startswith("ha"))
print(len(name))   #len function only works for strings,list tuples, dictionaries,sets and not for int/float.
print(name.capitalize()) #convert the first character to uppercase and the rest to lowercase.
print(name.find("har"))
print(name.replace("Bharat","Hindustan"))
print(name) #will print Bharat as strings are immutable.

print(name.lower())
print(name.upper())
print(name)


s = "   **Hello World!**   "
print("Original:", repr(s))  # show spaces clearly

# Remove spaces from both ends
print("strip():", repr(s.strip()))

# Remove spaces only from the left
print("lstrip():", repr(s.lstrip()))

# Remove spaces only from the right
print("rstrip():", repr(s.rstrip()))

# Remove specific characters from both ends
print("strip('* '):", repr(s.strip("* ")))


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']