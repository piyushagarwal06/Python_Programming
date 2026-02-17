class Employee:
    name="Hari"
    language="py"
    salary=1200000

h=Employee()
print(h.name,h.salary)

rohan=Employee()
rohan.name="Rohan Roro Robinson"
print(f"{rohan.salary} {rohan.language} {rohan.name}")

#Here name is object attribute and salary and language are class attributes as they directly belong to the class