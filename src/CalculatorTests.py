import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
calculator = Calculator() 

class MyTestCase(unittest.TestCase):


    def test_add_calculator(self):
        test_input = CsvReader('/src/Addition.csv').data
        for row in test_input:
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_sub_calculator(self):
        test_input = CsvReader('/src/Subtraction.csv').data
        for row in test_input:
            self.assertEqual(calculator.sub(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_mul_calculator(self):
        test_input = CsvReader('/src/Multiplication.csv').data
        for row in test_input:
            self.assertEqual(calculator.mul(row['Value 1'], row['Value 2']),int(row['Result']))


    def test_div_calculator(self):
        test_input = CsvReader('/src/Division.csv').data
        for row in test_input:
            self.assertEqual(calculator.div(row['Value 1'], row['Value 2']),float(row['Result']))


    def test_sq_calculator(self):
        test_input = CsvReader('/src/Square.csv').data
        for row in test_input:
            self.assertEqual(calculator.sq(row['Value 1']),int(row['Result']))


    def test_sqroot_calculator(self):
        test_input = CsvReader('/src/Square Root.csv').data
        for row in test_input:
            result = round(calculator.sqroot(int(row['Value 1'])), 8)
            self.assertEqual(result, round(float(row['Result']), 8))




if __name__ == '__main__':
    unittest.main()