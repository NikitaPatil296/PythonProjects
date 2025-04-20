
'''
Dunder methods : 

__repr__
The __repr__ method is used to provide an official string representation of an object,
mainly for debugging, which ideally should be unambiguous and could recreate the object.

__str__
The __str__ method provides a user-friendly string representation of an object, 
used when printing or displaying it directly, often meant to be more readable than __repr__.

__init__
The __init__ method is the constructor in Python, used to initialize an object's attributes when it is created. 
It sets up the initial state of the object by taking arguments during instantiation.

'''

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

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{}-{}".format(self.fullName(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())
    
dev1 = Employee('Rohan','More',50000)
dev2 = Employee('Nikita','Patil',50000)

# print(repr(dev1))
# print(str(dev1))



# Operator overloading  : Dunder menthods for Numerical value

# print(1+3)
# print(int.__add__(1,3))

# print('a'+'b')
# print(str.__add__('a','b'))


# print(dev1 + dev2)

print(len(dev1.fullName()))
