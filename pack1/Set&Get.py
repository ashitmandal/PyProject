"""
Use the getter ,setter method
"""
class EMPLOYEE:
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        #self.email=first+"."+last+"gmail.com"
    """get the valus->>>>Getter method"""
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    """"Set the fullname"""
    @fullname.setter
    def fullname(self, name):
        first, last=name.split(' ')
        self.first=first
        self.last=last
        
    """delete the full anme"""    
    @fullname.deleter
    def fullname(self):
        print('deleted name')
        self.first=None
        self.last=None


"""create the object"""
emp_1=EMPLOYEE('ashit','mandal',80000)
emp_1.fullname= 'neha kumari'
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname


"""lets take a example we are saperating the full name by Space.So for that we need class object and thoughthat we are passing the value to method"""

