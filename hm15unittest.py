import unittest


class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b != 0:
            return a/b


class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)

  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)

  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)


