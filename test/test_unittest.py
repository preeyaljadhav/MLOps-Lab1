import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    #My added test cases for the functions I have added
    #SQUARE ROOT TEST CASES

    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertEqual(calculator.square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
        with self.assertRaises(ValueError):
            calculator.square_root("nine")

    #MEMORY BUTTONS TEST CASES

    def test_memory(self):
        calculator.memory_clear()
        self.assertEqual(calculator.memory_recall(), 0)
        calculator.memory_add(10)
        self.assertEqual(calculator.memory_recall(), 10)
        calculator.memory_add(5)
        self.assertEqual(calculator.memory_recall(), 15)
        calculator.memory_subtract(3)
        self.assertEqual(calculator.memory_recall(), 12)
        calculator.memory_clear()
        self.assertEqual(calculator.memory_recall(), 0)
        calculator.memory_add(calculator.fun1(2, 3))
        self.assertEqual(calculator.memory_recall(), 5)
        calculator.memory_clear()
        with self.assertRaises(ValueError):
            calculator.memory_add("ten")
        with self.assertRaises(ValueError):
            calculator.memory_subtract("ten")

    # UNIT CONVERSION TEST CASES

    def test_temperature_conversion(self):
        self.assertEqual(calculator.celsius_to_fahrenheit(100), 212)
        self.assertEqual(calculator.celsius_to_fahrenheit(0), 32)
        self.assertEqual(calculator.celsius_to_fahrenheit(-40), -40)
        self.assertEqual(calculator.fahrenheit_to_celsius(212), 100)
        self.assertEqual(calculator.fahrenheit_to_celsius(32), 0)
        self.assertEqual(calculator.fahrenheit_to_celsius(-40), -40)
        with self.assertRaises(ValueError):
            calculator.celsius_to_fahrenheit("hot")

    def test_distance_conversion(self):
        self.assertEqual(calculator.miles_to_km(1), 1.609344)
        self.assertEqual(calculator.km_to_miles(1.609344), 1)
        self.assertEqual(calculator.km_to_miles(0), 0)
        self.assertAlmostEqual(calculator.km_to_miles(10), 6.2137, places=4)
        with self.assertRaises(ValueError):
            calculator.km_to_miles(-5)
        with self.assertRaises(ValueError):
            calculator.miles_to_km("far")

    # NUMBER BASE CONVERSION TEST CASES

    def test_base_conversion(self):
        self.assertEqual(calculator.decimal_to_binary(10), "1010")
        self.assertEqual(calculator.decimal_to_binary(0), "0")
        self.assertEqual(calculator.decimal_to_binary(255), "11111111")
        self.assertEqual(calculator.decimal_to_hex(255), "FF")
        self.assertEqual(calculator.decimal_to_hex(16), "10")
        self.assertEqual(calculator.binary_to_decimal("1010"), 10)
        self.assertEqual(calculator.binary_to_decimal("11111111"), 255)
        self.assertEqual(calculator.binary_to_decimal(calculator.decimal_to_binary(42)), 42)
        with self.assertRaises(ValueError):
            calculator.decimal_to_binary(-5)
        with self.assertRaises(ValueError):
            calculator.decimal_to_binary(3.5)
        with self.assertRaises(ValueError):
            calculator.decimal_to_hex("ten")
        with self.assertRaises(ValueError):
            calculator.binary_to_decimal("102")




if __name__ == '__main__':
    unittest.main()