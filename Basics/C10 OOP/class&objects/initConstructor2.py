class Employee:
    language="python"
    salary=120000

    def __init__(self,name ,salary,language):#dunder method which is automatically called
        self.name="hj"
        self.salary=10000
        self.language="js"
        print(f"I am an object. Name: {self.name}")
        print("I am an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")
    
harry=Employee("Dhurandar" , 120000000000 ,"js")
harry.name="Harry"
print(harry.name , harry.salary)

rohan=Employee("Dhurandar" , 120000000000 ,"js")#__init__  Runs automatically when an object is created.