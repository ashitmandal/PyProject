"""
here 2 staecial methos"repr" and "str"
repr-is for debug purpose
str is for basic OP-string OP it wil show
repr and str means->how we wantoutr output should be prinr

"""

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
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{}-{}'.format(self.last,self.email)     
    def __add__(self,Ather):
        return self.pay+Ather.pay
    
emp_1=EMPLOYEE('ashit','kumar',70000)
emp_2=EMPLOYEE('maa','kumari',80000)

"""
print(repr(emp_2))
print(str(emp_2))
"""

#or in other way
#print(emp_1.__repr__())
#print(emp_2.__str__())

#int specia method
print(int.__add__(1,2))

print(emp_1+emp_2)
    
    
        