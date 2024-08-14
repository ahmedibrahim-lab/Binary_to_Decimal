import unittest

from b2d import binary_to_decimal

class TestB2D(unittest.TestCase):
    
    # Test cases for correct results
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('10'), 2)
        self.assertEqual(binary_to_decimal('11'), 3)
        self.assertEqual(binary_to_decimal('101'), 5)
        self.assertEqual(binary_to_decimal('1101'), 13)
        self.assertEqual(binary_to_decimal('11111111'), 255)
        self.assertEqual(binary_to_decimal('100000000'), 256)

    # Test cases for invalid inputs
    def test_invalid_input(self):
        
        with self.assertRaises(ValueError):
            binary_to_decimal('2') 
        with self.assertRaises(ValueError):
            binary_to_decimal('abc')    
        with self.assertRaises(ValueError):
            binary_to_decimal('10a1')    
        with self.assertRaises(ValueError):
            binary_to_decimal('')
        
if __name__ == '__main__':
    unittest.main()