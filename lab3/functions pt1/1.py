def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Example of using the function:
grams_value = 250
ounces_result = grams_to_ounces(grams_value)
print(f"{grams_value} grams is approximately {ounces_result:.2f} ounces.")

'''Ниже представлена функция на Python, которая конвертирует граммы в унции, используя коэффициент конверсии:

1. Определенна функция grams_to_ounces с параметром grams, представляющим количество граммов.
2. Внутри функции вычисляется количество унций по формуле: ounces = 28.3495231 * grams.
3. Результат в унциях возвращается из функции.

Пример использования функции:
grams_value = 250
ounces_result = grams_to_ounces(grams_value)
print(f"{grams_value} граммов примерно равно {ounces_result:.2f} унций.")
Эта функция принимает количество граммов в качестве аргумента, вычисляет соответствующее количество унций и возвращает результат. 
В приведенном примере функция применяется для конвертации 250 граммов в унции, и результат выводится на экран.
'''