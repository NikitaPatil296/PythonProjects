class Employee:

    raise_amount = 1.04     # Class variable

    def __init__(self, first, last,pay):
        self.first = first                                                
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(emp1.first, emp1.last)
    
    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:       # weekday() : Monday = 0 , ....., Saturday=5,Sunday=6
            return False
        return True


emp1 = Employee('Rohan','More',50000)
emp2 = Employee('Nikita','Patil',50000)


import datetime
day = datetime.date(2025,4,20)
print(emp1.is_workday(day))



# Regular instance methods -
#                Bydefault pass instance (self) as first argument
# classmethod -  
#                Pass class as first argument(cls)
#                Alternatively used as constructor
# staticmethod - 
#                 Dont pass anything automatically. They dont pass instance or class.
#                 They behave like regular function except we include them in classes 
#                 because they have some logical connection with the class.