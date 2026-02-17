# Write a program to mine a log file and find out whether it contains ‘python’.

with open("Chapter9/practiceSet/p6file.txt") as f:
    content = f.read()

if("Python" in content):
    print("Yes python is present")

else:
    print("No python is not present")