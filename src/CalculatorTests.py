import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
calculator = Calculator()

class MyTestCase(unittest.TestCase):



    def test_add(self):
        self.assertEqual(calculator.add(2,2),4)

    def test_add_calculator(self):
        test_input = CsvReader('/src/Addition.csv').data
        for row in test_input:
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))



if __name__ == '__main__':
    unittest.main()