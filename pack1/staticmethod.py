
""" check the mentioned date is weekdays of not"""
import datetime

class EMPLOYEE:
    
    @staticmethod
    def is_week_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True
        


        
my_date=datetime.date(2020,6,13)
print(EMPLOYEE.is_week_day(my_date))
