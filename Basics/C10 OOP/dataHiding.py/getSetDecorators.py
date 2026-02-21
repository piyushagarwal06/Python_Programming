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