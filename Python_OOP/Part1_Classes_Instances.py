
class Employee:
    def __init__(self, first, last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(emp1.first, emp1.last)


emp1 = Employee('Rohan','More',50000)
emp2 = Employee('Nikita','Patil',50000)




