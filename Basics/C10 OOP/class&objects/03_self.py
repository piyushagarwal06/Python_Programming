class Employee:
    language="Python"
    salary=120000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    def greet(self):
        print("Good morning")

h=Employee()
h.getInfo()
h.greet()
# Here:
# h is an object of Employee
# When you call h.getInfo(), Python automatically passes h as the first argument
# That first argument is called self
# So internally, Python does this 👇
# Employee.getInfo(h)