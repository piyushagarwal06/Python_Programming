#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘anywhere’.
f=open("Chapter9/practiceSet/p1poems.txt")
content=f.read()
if("anywhere" in content):
    print("The word is present")
else:
    print("The word is not present")

f.close()