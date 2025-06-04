import unittest
from main import RPNCalculator


class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        """Инициализация калькулятора перед каждым тестом."""
        self.calc = RPNCalculator()

    def test_basic_arithmetic(self):
        """Тест базовых арифметических операций."""
        expression = "3 + 5 * 2"
        rpn = self.calc.to_rpn(expression)
        result = self.calc.calculate(expression)
        self.assertEqual(rpn, ['3', '5', '2', '*', '+'])
        self.assertEqual(result, 13.0)

    def test_parentheses(self):
        """Тест выражений со скобками."""
        expression = "( 3 + 5 ) * 2"
        rpn = self.calc.to_rpn(expression)
        result = self.calc.calculate(expression)
        self.assertEqual(rpn, ['3', '5', '+', '2', '*'])
        self.assertEqual(result, 16.0)

    def test_division_and_subtraction(self):
        """Тест деления и вычитания."""
        expression = "10 - 4 / 2"
        rpn = self.calc.to_rpn(expression)
        result = self.calc.calculate(expression)
        self.assertEqual(rpn, ['10', '4', '2', '/', '-'])
        self.assertEqual(result, 8.0)

    def test_invalid_expression(self):
        """Тест обработки некорректного выражения."""
        expression = "3 + * 5"
        with self.assertRaises(ValueError):
            self.calc.calculate(expression)

    def test_unmatched_parentheses(self):
        """Тест обработки несбалансированных скобок."""
        expression = "( 3 + 5  * 2"
        with self.assertRaises(ValueError):
            self.calc.to_rpn(expression)


if __name__ == '__main__':
    unittest.main()
