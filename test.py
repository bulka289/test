def main(input: str) -> str:


    try:
        # Разделяем строку на числа и операцию
        parts = input.split()
        if len(parts) != 3:
            raise ValueError("Неверный формат ввода")

        a = int(parts[0])
        b = int(parts[2])

        # Выполняем операцию
        operation = parts[1]
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            # Проверка на деление на ноль
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            result = a // b
        else:
            raise ValueError("Неверная операция")

        # Проверяем, что числа находятся в диапазоне от 1 до 10
        # (после выполнения операции)
        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10")

        return str(result)

    except ValueError as e:
        print(f"Ошибка: {e}")
        raise
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
        raise



if __name__ == "__main__":
    input_str = input("Введите арифметическое выражение: ")
    try:
        result = main(input_str)
        print(f"Результат: {result}")
    except Exception as e:
        pass