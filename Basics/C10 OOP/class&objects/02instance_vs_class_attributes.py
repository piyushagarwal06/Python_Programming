class Employee:
    name="Hari"
    language="py"
    salary=1200000

h=Employee()
h.language="java" #This is an instance attribute
# nstance attributes, take preference over class attributes during assignment & retrieval.
print(h.name,h.salary,h.language)