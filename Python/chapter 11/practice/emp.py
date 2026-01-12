class Employee:
    salary=10000
    increment=20
    @property
    def afterincrement(self):
        return (self.salary*self.increment)/100+self.salary
    @afterincrement.setter
    def afterincrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100
emp=Employee()
emp.salary=1000
print(emp.afterincrement)
emp.afterincrement=1200
print(emp.increment)
 