import re

# Read the content of the file
with open("row.txt", "r") as file:
    text = file.read()

# Define the pattern
pattern = re.compile(r'[ ,.]')

# Replace matches with a colon
modified_text = pattern.sub(':', text)

# Print the modified text
print("Modified Text:")
print(modified_text)

'''import re: Импорт модуля регулярных выражений (re).

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

text = file.read(): Чтение содержимого файла и сохранение его в переменной text.

pattern = re.compile(r'[ ,.]'): Создание регулярного выражения с паттерном "[ ,.]", где [ ,.] 
соответствует любому пробелу, запятой или точке.

modified_text = pattern.sub(':', text): Замена всех совпадений паттерна в тексте на двоеточие.

print("Modified Text:") и print(modified_text): Вывод измененного текста.

Этот код заменит все вхождения пробела, запятой или точки на двоеточие в тексте из файла "row.txt".'''