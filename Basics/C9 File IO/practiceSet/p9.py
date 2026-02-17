# Write a program to find out whether a file is identical & matches the content of another file.

with open("Chapter9/practiceSet/p8thiscopy.txt") as f:
    content1=f.read()

with open("Chapter9/practiceSet/p8this.txt") as f:
    content2=f.read()

if(content1==content2 ):
    print("Files are identical")

else:
    print("Files are Not identical")