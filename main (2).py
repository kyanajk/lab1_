#Ким Яна. 090301-ПОВа-о23
import math
def calculate_formula(x, y, z):
    fourth_root = (y + (x - 1) ** (1 / 3)) ** (1 / 4)

    absolute_value = abs(x - y)

    sin_squared = math.sin(z) ** 2
    tan_value = math.tan(z)

    denominator = absolute_value * (sin_squared + tan_value)

    if denominator != 0:
        result = fourth_root / denominator
    else:
        result = None
    return result
# Пример использования функции
x = 9
y = 3
z = math.pi / 4
result = calculate_formula(x, y, z)
print(result)