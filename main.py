import operator


class RPNCalculator:
    """Класс для преобразования инфиксного выражения в RPN и вычисления результата."""

    def __init__(self):
        self.operators = {
            '+': (1, operator.add),
            '-': (1, operator.sub),
            '*': (2, operator.mul),
            '/': (2, operator.truediv)
        }

    def is_number(self, token: str) -> bool:
        """Проверяет, является ли токен числом."""
        try:
            float(token)
            return True
        except ValueError:
            return False

    def to_rpn(self, expression: str) -> list:
        """Преобразует инфиксное выражение в обратную польскую запись (RPN)."""
        stack = []
        output = []
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

        for token in tokens:
            if self.is_number(token):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop()  # Удаляем '('
            elif token in self.operators:
                while (stack and stack[-1] != '(' and
                       stack[-1] in self.operators and
                       self.operators[stack[-1]][0] >= self.operators[token][0]):
                    output.append(stack.pop())
                stack.append(token)
            else:
                raise ValueError(f"Недопустимый токен: {token}")

        while stack:
            if stack[-1] == '(':
                raise ValueError("Неправильное расположение скобок")
            output.append(stack.pop())

        return output

    def evaluate_rpn(self, rpn: list) -> float:
        """Вычисляет значение выражения в RPN."""
        stack = []

        for token in rpn:
            if self.is_number(token):
                stack.append(float(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для операции")
                b = stack.pop()
                a = stack.pop()
                result = self.operators[token][1](a, b)
                stack.append(result)
            else:
                raise ValueError(f"Недопустимый токен в RPN: {token}")

        if len(stack) != 1:
            raise ValueError("Некорректное выражение: лишние операнды")
        return stack[0]

    def calculate(self, expression: str) -> float:
        """Основной метод: преобразует выражение в RPN и вычисляет его."""
        try:
            rpn = self.to_rpn(expression)
            result = self.evaluate_rpn(rpn)
            return result
        except Exception as e:
            raise ValueError(f"Ошибка в выражении: {str(e)}")


def main():
    """Точка входа программы."""
    calc = RPNCalculator()
    while True:
        try:
            expression = input("Введите выражение (или 'выход' для завершения): ")
            if expression.lower() == 'выход':
                break
            result = calc.calculate(expression)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
