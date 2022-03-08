import unittest

from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide
from calculator import powerOf
from calculator import square



class TestCalculator(unittest.TestCase):
    
    def test_calculator_add(self):
        result=add(1,2)
        self.assertEqual(result,3)
        
    def test_calculator_add(self):
        result=add(32131,-2231)
        self.assertEqual(result,29900)
        
    def test_calculator_subtract(self):
        result=subtract(2,1)
        self.assertEqual(result,1)
        
    def test_calculator_subtract(self):
            result=subtract(32131,2231)
            self.assertEqual(result,29900)
    
    def test_calculator_add(self):
        result=multiply(5,6)
        self.assertEqual(result,30)
    
    def test_calculator_add(self):
        result=divide(81,9)
        self.assertEqual(result,9)
    
    def test_calculator_powerOff(self):
        result=powerOf(2,10)
        self.assertEqual(result,1024)
    
    def test_calculator_add(self):
        result=square(144)
        self.assertEqual(result,12)
    
   
        
        
        
if __main__ =='__main__':
   unittest.main()

    
    

