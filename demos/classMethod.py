class EMPLOYEE:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"gmail.com"       
        
        
    def fullmane(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #return self.pay = int(self.pay * self.raise_amount)
        return int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
        
        
    @classmethod
    def _arrange_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    #get teh employee from diff format 
        
emp_str_1='ram-kumar-20000'
emp_str_2='komal-kaur-50000'
emp_str_3='neka-kumari-50000'

"""
this is one way to initiate variale
first,last,pay=emp_str_1.split('-')
new_emp_1=EMPLOYEE(first,last,pay)
"""

new_emp_1=EMPLOYEE._arrange_string(emp_str_1)

print(new_emp_1.email)



#print(help(EMPLOYEE))


"""    
emp_1=EMPLOYEE('ashit','mandal',70000)
emp_1=EMPLOYEE('Binod','mandal',60000)


emp_1.set_raise_amount(2.0)
print(EMPLOYEE.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)
    
""" 
print(EMPLOYEE.__dict__)
    
    
    
        