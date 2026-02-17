# Write a program to find out the line number where python is present from ques 6.

with open("Chapter9/practiceSet/p6file.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "Python" in line:
        print(f"Yes Python is present Line No: {lineno}")
        # break
    lineno += 1
else:
    print("No Python is not present")
