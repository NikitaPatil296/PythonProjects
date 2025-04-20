class Employee:

    raise_amount = 1.04     # Class variable

    def __init__(self, first,last,pay):
        self.first = first                                                
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount)


class Developer(Employee):
    def __init__(self, first, last, pay,language):
        super().__init__(first, last, pay)
        self.language = language

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullName())


dev1 = Developer('Rohan','More',50000,'German')
dev2 = Developer('Nikita','Patil',50000,'English')

manager1 = Manager('Akash','Patil',90000,[dev1])

# print(isinstance(dev1,Manager))
print(issubclass(Developer,Employee))

# print(help(Developer))