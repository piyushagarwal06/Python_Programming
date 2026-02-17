class Employee:
    language="python"
    salary=120000

    def __init__(self):#dunder method which is automatically called
        print("I am an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")
    
harry=Employee()
harry.name="Harry"
print(harry.name , harry.salary)

rohan=Employee()#__init__  Runs automatically when an object is created.