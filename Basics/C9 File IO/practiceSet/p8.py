# Write a program to make a copy of a text file “this. txt”
with open("Chapter9/practiceSet/p8this.txt") as f:
    content=f.read()

with open("Chapter9/practiceSet/p8thiscopy.txt", "w") as f:
    f.write(content)