"""
Use the getter ,setter method
"""
class EMPLOYEE:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        #self.email=first+"."+last+"gmail.com"
    #get the valus
    @property  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first,self.last)
    
    
    #set the value 

emp_1=EMPLOYEE('ashit','mandal',70000)
"""
emp_1 is name change so only direct variable ,if any operation we have done ,so it will not change
so for that reason we use the get function (in python we called @property.
So in this wasy Ex:email method,we can call the function as an argument )
"""
emp_1.first='binod'

#Use the settor to set the data
emp_1.fullname('sulakha mandal')


print(emp_1.first)
print(emp_1.fullname())
#Calling the function as an variable ,due to GetProperties mothod
print(emp_1.email)

