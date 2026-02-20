class Employee:
    def __init__(self, name):
        self.name = name

class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

p = Programmer("Harry", "Python")
print(p.name)
print(p.language)
