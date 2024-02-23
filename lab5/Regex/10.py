import re

def camel_to_snake(input_camel_case):
    # Используем регулярное выражение для преобразования Camel Case в Snake Case
    snake_case_result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_camel_case).lower()
    return snake_case_result

# Чтение содержимого файла
with open("row.txt", "r") as file:
    camel_case_text = file.read()

# Пример использования:
snake_case_result = camel_to_snake(camel_case_text)

# Вывод результата
print("Исходная Camel Case строка:", camel_case_text)
print("Преобразованная Snake Case строка:", snake_case_result)

'''import re: Импорт модуля регулярных выражений (re).

def camel_to_snake(input_camel_case):: Определение функции, которая принимает 
строку в формате Camel Case и возвращает строку в формате Snake Case.

snake_case_result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_camel_case).lower(): 
Использование регулярного выражения для преобразования Camel Case в Snake Case.
Здесь мы ищем места, где строчная буква или цифра перед заглавной буквой и вставляем подчеркивание между ними. 
Затем результат приводится к нижнему регистру.

return snake_case_result: Возвращение результата из функции.

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

camel_case_text = file.read(): Чтение содержимого файла и сохранение его в переменной camel_case_text.

snake_case_result = camel_to_snake(camel_case_text): Вызов функции с использованием другого имени переменной.

print("Исходная Camel Case строка:", camel_case_text): Вывод исходной строки Camel Case.

print("Преобразованная Snake Case строка:", snake_case_result): Вывод результата в формате Snake Case.'''