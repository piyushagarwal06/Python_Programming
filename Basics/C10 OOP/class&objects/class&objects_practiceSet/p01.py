# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"
    def __init__(self,name, salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Harry",12000000,400001)
print(p.name,p.salary,p.company)

r=Programmer("Rohan",1230000,250001)
print(r.salary,r.company,r.name)


        