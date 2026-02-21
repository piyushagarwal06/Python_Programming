class Employee:
    @property
    def name(self):
        return self.ename

e = Employee()
e.ename = "Harry"
print(e.name)
