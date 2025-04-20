class Employee:

    raise_amount = 1.04     # class variable
    no_of_emps = 0          # class variable

    def __init__(self, first, last,pay):
        self.first = first                                                 # Instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_emps += 1

    def fullName(self):
        return '{} {}'.format(emp1.first, emp1.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount)


emp1 = Employee('Rohan','More',50000)
emp2 = Employee('Nikita','Patil',50000)

print(Employee.no_of_emps)

# emp1.raise_amount = 2
# print(emp1.__dict__)              # Namespace of emp1
# print(Employee.__dict__)
