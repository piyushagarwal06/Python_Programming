marks={
    "Harry" : 100,
    "Shubham" : 59,
    "Rohan" : 23
}
print(marks,type(marks))
print(marks["Harry"])

print(marks.items())
print(marks.values())
print(marks.keys())
print(marks.get("Harry"))
print(marks.get("harry"))
marks.update({"harry":99, "Siya":101})
print(marks)