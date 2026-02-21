# Property decorators (getter & setter) help in encapsulation.
# Property decorators allow methods to be accessed like attributes while enabling controlled access using getter and setter methods.
class Employee:
    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.ename = value

e = Employee()
e.name = "Harry"
print(e.name)