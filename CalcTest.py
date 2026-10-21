import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_power_negative_exponent(self):
        calc = Calculator()
        result = calc.power(2, -2)
        self.assertEqual(result, 0.25)
        self.assertIsInstance(result, float)

    def test_power_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(calc.power(0, 0), 1)

    def test_modulo_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.modulo(7, 0)

    def test_power_positive_integers(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)

    def test_modulo_positive_integers(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(7, 3), 1)

    def test_add(self):
        calc = Calculator() # arrange: initialize object
        result = calc.add(2, 3) # act: execute function
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5 # assert

    def test_subtract(self):
        calc = Calculator() # arrange: initialize object
        result = calc.subtract(2, 3) # act: execute function
        self.assertEqual(result, -1)  # Expect 2 - 3 = -1 # assert
    
    def test_multiply(self):
        calc = Calculator() # arrange: initialize object
        result = calc.multiply(2, 3) # act: execute function
        self.assertEqual(result, 6)  # Expect 2 * 3 = 6 # assert
    
    def test_divide_by_zero(self):
        calc = Calculator()

        with self.assertRaisesRegex(ValueError, "^Cannot divide by zero$"):
            calc.divide(5, 0)

    def test_add_floats(self):
        calc = Calculator()
        self.assertEqual(calc.add(0.1, 0.2), 0.3)

    def test_multiply_invalid_input(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.multiply("5", 3)
    
    def test_add_invalid_input(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.add("5", 3)
    
    def test_subtract_invalid_input(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.subtract("5", 3)
    
    def test_divide_invalid_input(self):
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.divide("5", 3)
    
    def test_divide_integer_return_type(self):
        calc = Calculator()
        res = calc.divide(10, 2)
        self.assertIsInstance(res, int)
    
    def test_subtract_overflow(self):
        calc = Calculator()
        with self.assertRaises(OverflowError):
            calc.subtract(-1e308, 1e308)

if __name__ == "__main__":
    unittest.main()
