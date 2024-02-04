def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Example of using the function:
fahrenheit_temp = float(input("Enter Fahrenheit temperature: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Fahrenheit is equivalent to {celsius_result:.2f} Celsius.")


'''Ниже представлена функция на Python, которая принимает температуру в градусах Фаренгейта в качестве входных данных, 
вычисляет эквивалентную температуру в градусах Цельсия с использованием заданной формулы, а затем выводит результат:

1. Определена функция fahrenheit_to_celsius с параметром fahrenheit, представляющим температуру в градусах Фаренгейта.
2. Внутри функции вычисляется эквивалентная температура в градусах Цельсия по формуле: C = (5 / 9) * (F – 32).
3. Результат в градусах Цельсия возвращается из функции.

Пример использования функции:
fahrenheit_temp = float(input("Введите температуру в градусах Фаренгейта: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} градусов Фаренгейта эквивалентны {celsius_result:.2f} градусам Цельсия.")
Эта функция принимает температуру в градусах Фаренгейта, 
применяет формулу для конвертации в градусы Цельсия и выводит результат на экран.

'''