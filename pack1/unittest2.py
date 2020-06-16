class EMPLOYEE:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"gmail.com"      


        @property
        def email(self):
            return '{} {}.gmail.com'.format(self.first,self.last)
        @property
        def email(self):
            return '{} {}.gmail.com'.format(self.first,self.last) 
        
e=EMPLOYEE(ashit,mandal,90000)
print(e.email())
