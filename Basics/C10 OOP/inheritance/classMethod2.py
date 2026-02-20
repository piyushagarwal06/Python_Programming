class Employee:
    company = "Google"

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e = Employee()
print(Employee.company)
e.changeCompany("Microsoft")
print(Employee.company)
