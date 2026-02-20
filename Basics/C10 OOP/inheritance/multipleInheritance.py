class Employee:
    company:"ITC"
    name="Default name"
    def show(self):
        print(f"The name of the employer is {self.name} and the company  is {self.company}")

class Coder:
    language="Python"
    def printlanguage(self):
        print(f"{self.language}")

class Programmer(Employee,Coder):
    company="INS"
    def showlanguage(self):
        print(f"{self.language} {self.company}")

a=Employee()
b=Programmer()

b.show()
b.printlanguage()
b.showlanguage()


