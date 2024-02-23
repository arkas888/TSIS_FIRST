import re

def split_at_uppercase(input_string):
    # Use regular expression to split at uppercase letters
    split_result = re.findall(r'[a-z]+|[A-Z][a-z]*', input_string)
    return split_result

# Чтение содержимого файла
with open("row.txt", "r") as file:
    text_from_file = file.read()

# Пример использования:
result = split_at_uppercase(text_from_file)

# Вывод результата
print("Исходная строка:", text_from_file)
print("Результат разделения на заглавные буквы:", result)

'''import re: Импорт модуля регулярных выражений (re).

def split_at_uppercase(input_string):: Определение функции, которая принимает строку и возвращает список подстрок, 
разделенных по заглавным буквам.

split_result = re.findall(r'[a-z]+|[A-Z][a-z]*', input_string): Использование регулярного выражения для разделения строки на подстроки.
Это выражение ищет либо одну или более строчных букв (маленьких), либо заглавную букву, за которой могут следовать строчные буквы.

return split_result: Возвращение результата из функции.

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

text_from_file = file.read(): Чтение содержимого файла и сохранение его в переменной text_from_file.

result = split_at_uppercase(text_from_file): Вызов функции с использованием другого имени переменной.

print("Исходная строка:", text_from_file): Вывод исходной строки.

print("Результат разделения на заглавные буквы:", result): Вывод результата разделения строки на заглавные буквы.

Этот код разделит строку на подстроки, начинающиеся с заглавных букв, и выведет результат.'''