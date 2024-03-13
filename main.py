def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return num1 / num2
    else:
        raise ValueError("Неверная операция!")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operator = input("Введите операцию (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print(f"Результат: {result}")
except ValueError as ve:
    print(f"Ошибка: {ve}")
except ZeroDivisionError as zde:
    print(f"Ошибка: {zde}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
