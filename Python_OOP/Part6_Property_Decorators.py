
class Employee:
    def __init__(self, first,last,pay):
        self.first = first                                                
        self.last = last
        self.pay = pay

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@email.company.com'.format(self.first, self.last)
    
    @fullName.setter
    def fullName(self, name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete Name !')
        self.first = None
        self.last = None
        
    
dev1 = Employee('Rohan','More',50000)
dev2 = Employee('Nikita','Patil',50000)

dev1.fullName = 'XXX YYY'

print(dev1.first)
print(dev1.last)
print(dev1.email)
print(dev1.fullName)

del dev1.fullName
