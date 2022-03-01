import unittest

from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide
from calculator import powerOf
from calculator import square





class TestCalculator(unittest.TestCase):
    
    def test_calculator_add(self):
        self.assertEqual(add(1,2),3)
        
    def test_calculator_subtract(self):
        self.assertEqual(subtract(2,1),1)
    
    def test_calculator_add(self):
        self.assertEqual(multiply(5,6),36)
    
    def test_calculator_add(self):
        self.assertEqual(divide(81,9),9)
    
    def test_calculator_powerOff(self):
        self.assertEqual(powerOf(2,10),1024)
    
    def test_calculator_add(self):
        self.assertEqual(square(144),12)
        
        
        
if __main__ =='__main__':
    unittest.main()

    
    

