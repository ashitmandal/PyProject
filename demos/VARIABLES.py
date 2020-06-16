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
    
emp_1=EMPLOYEE('ashit','mandal',50000)
emp_1=EMPLOYEE('Binod','mandal',60000)

print(EMPLOYEE.raise_amount)
print(emp_1.raise_amount)

print(EMPLOYEE.__dict__)
