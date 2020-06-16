import unittest
from pack1 import calc as c


class testCalc(unittest.TestCase):
    
    
    def test_add(self):
        #result=c.add(10,5)
        #self.assertEqual(result, 15)
        self.assertEquals(c.add(10,5),15)
        self.assertEquals(c.add(-1,1),0)
        self.assertEquals(c.add(10,2),12)
        
    def test_sub(self): 
        self.assertEquals(c.sub(6,3),3)
        
    def test_mul(self):
        self.assertEquals(c.mul(6,3),18)
        
        
    def test_div(self):
        self.assertEquals(c.div(6,2),3)        
        self.assertEquals(c.div(5,2),2.5)
        #self.assertEquals(c.div(6,0),6)
        
        self.assertRaises(ValueError,c.div,10,2)
        #result=
   
        
if __name__=='__main__':
    unittest.main()
