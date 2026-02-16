f=open("Chapter9/file.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close