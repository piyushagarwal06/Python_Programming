# A file contains a word “justice" multiple times. You need to write a program which replace this word with ##### by updating the same file.

word="justice"

with open("Chapter9/practiceSet/p4file.txt" , "r") as f:
    content=f.read()

contentNew = content.replace(word,"####")

with open("Chapter9/practiceSet/p4file.txt" , "w") as f:
    f.write(contentNew)