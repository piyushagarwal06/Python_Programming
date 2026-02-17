class Employee:
    language = "Python"
    salary = 120000

    # Instance method (uses self)
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method (does NOT use self)
    @staticmethod
    def greet():
        print("Good morning")


# Object creation
h = Employee()

# Calling instance method
h.getInfo()

# Calling static method
h.greet()

# Static method can also be called using class name
Employee.greet()
