import unittest
from src.calculator import add, subtract, divide

class Test_Calculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,0),-1)
        self.assertEqual(add(1.5,1.5),3)
        
    def test_subtract(self):
        self.assertEqual(subtract(3,2),1)
        self.assertEqual(subtract(0,-1),1)
        self.assertEqual(subtract(0,0),0)
        
    def test_divide(self):
        self.assertEqual(divide(6,3),2)
        self.assertAlmostEqual(divide(13,5),2.6)
        with self.assertRaises(ValueError):
            divide(9,0)
            

if __name__ == '__main__':
    unittest.main()
        

