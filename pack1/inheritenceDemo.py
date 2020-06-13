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
  
class DEVELOPER(EMPLOYEE):
    raise_amount=5
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
      
        self.prog_lang=prog_lang
        
class MANAGER(EMPLOYEE):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first, last, pay)
        
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("->>>",emp.fullmane())
            
                   
dev_1=DEVELOPER('Ashit','Mandal',100000,'python')
dev_2=DEVELOPER('Deepak','Mandal',50000,'java')


mgr_1=MANAGER('binod','mandal',60000)

#mgr_1.print_emp()

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_1)

#mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

"""

print(isinstance(mgr_1,EMPLOYEE))


print(issubclass(MANAGER,DEVELOPER))
print(mgr_1.fullmane())
"""