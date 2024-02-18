import math

# Input the degree value
degree = float(input("Введите значение в градусах: "))

# Convert degree to radian
radian = math.radians(degree)

# Print the result
print(f"Значение в радианах: {radian:.6f}")

'''Программа принимает значение в градусах с помощью input.
Используется функция math.radians для преобразования значения из градусов в радианы.
Результат выводится с использованием форматированной строки, показывая значение в радианах, округленное до 6 знаков после запятой.'''