from employeeModule import EMPLOYEE as e
import unittest

class test_employeeModule(unittest.TestCase):
    
    
    def test_EMPLOYEE(self):
        emp1=e('ashit','mandal',70000)
        print(emp1.email())
        #self.assertEquals(emp1.email,'ashitmandal@email.com')
        
    
    
    
    
   # self.assertEqual(emp1.email,'ashitmandal@email.com')