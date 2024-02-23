import re

def insert_spaces_between_caps(input_str):
    # Используем регулярное выражение для поиска слов, начинающихся с заглавных букв
    # и вставляем пробелы перед ними
    result_str = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_str)
    return result_str

# Чтение содержимого файла
with open("row.txt", "r") as file:
    text_content = file.read()

# Пример использования:
result_text = insert_spaces_between_caps(text_content)

# Вывод результата
print("Исходный текст:", text_content)
print("Текст с вставленными пробелами перед словами в Camel Case:", result_text)

'''import re: Импорт модуля регулярных выражений (re).

def insert_spaces_between_caps(input_str):: Определение функции, которая принимает строку и возвращает новую строку с 
вставленными пробелами перед словами, начинающимися с заглавных букв.

result_str = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_str): Использование регулярного выражения для поиска мест, 
где маленькая буква перед заглавной буквой, и вставки пробела между ними.

return result_str: Возвращение результата из функции.

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

text_content = file.read(): Чтение содержимого файла и сохранение его в переменной text_content.

result_text = insert_spaces_between_caps(text_content): Вызов функции с использованием другого имени переменной.

print("Исходный текст:", text_content): Вывод исходного текста.

print("Текст с вставленными пробелами перед словами в Camel Case:", result_text): 
Вывод результата с вставленными пробелами перед словами, начинающимися с заглавных букв.'''