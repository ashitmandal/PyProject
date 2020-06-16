class EMPLOYEE:
    raise_amount=1.04
    
    def __init__(self,name,age,salary):
        self.namae=name
        self.age=age
        self.salary=salary
        
    def __repo__(self):
        return '{} {}.s{}'.format(self.name,self.age,self.salary)
        
        
        
e1=EMPLOYEE('ashit',28,35000)
e2=EMPLOYEE('aman',29,55000)
e3=EMPLOYEE('ram',30,55000)

employee=[e1,e2,e3]

#sort the employees by name wise

    def e_sort(emp):
        return self.name

s.employee=sorted(employee,key=e_sort)

print(s.employee)