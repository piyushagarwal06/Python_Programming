class Person:
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    def work(self):
        print("I am working")

class Programmer(Employee):
    def code(self):
        print("I am coding")

p = Programmer()
p.takeBreath()
p.work()
p.code()
