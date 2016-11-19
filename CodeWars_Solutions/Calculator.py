# Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

# Example:

# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
# "2/2+3*4-6"

import unittest

class Calculator(object):
  def evaluate(self, string):
    return (round(eval(string),4))

def Calculate(arg1):
    new_calc = Calculator()
    return (new_calc.evaluate(arg1))

# Calculate('2 / 2 + 3 * 4 - 6')

class MyTest(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(Calculate('2 / 2 + 3 * 4 - 6'),7)
    def test2(self):
        self.assertEqual(Calculate('1.1*2.2*3.3'),7.986)

if __name__ == '__main__':
    unittest.main()