import re

# Read the content of the file
with open("row.txt", "r") as file:
    snake_case_string = file.read()

# Define the pattern for finding underscores followed by a letter
tort = re.compile(r'_([a-z])')

# Function to convert match to uppercase
def to_upper(match):
    return match.group(1).upper()

# Use sub() with a function to convert snake_case to camelCase
camel_case_string = tort.sub(to_upper, snake_case_string)

# Print the converted string
print("Camel Case String:")
print(camel_case_string)

'''import re: Импорт модуля регулярных выражений (re).

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

snake_case_string = file.read(): Чтение содержимого файла и сохранение его в переменной snake_case_string.

tort = re.compile(r'_([a-z])'): Создание регулярного выражения для поиска символа подчеркивания, за которым следует строчная буква.

def to_upper(match): return match.group(1).upper(): Функция to_upper, которая принимает совпадение (match) и 
возвращает букву в верхнем регистре.

camel_case_string = tort.sub(to_upper, snake_case_string): Использование функции sub() 
для замены символов подчеркивания на соответствующие буквы в верхнем регистре.

print("Camel Case String:") и print(camel_case_string): Вывод преобразованной строки в стиле "camelCase".

Этот код преобразует строку в стиле "snake_case" в строку в стиле "camelCase".'''