result = []

def divider(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("a и b должны быть числами")
    if a < b:
        raise ValueError("a должно быть больше или равно b")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, "some_key": 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Исключение: {e}")

print(result)
