class EMPLOYEE:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)
        
    def fullmane(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #return self.pay = int(self.pay * self.raise_amount)
        return int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

