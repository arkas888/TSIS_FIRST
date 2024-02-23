import re

# Read the content of the file
with open("row.txt", "r") as file:
    text = file.read()

# Define the pattern
p = re.compile(r'a.*b')

# Find all matches in the text
matches = p.findall(text)

# Print the matches
print("Matches:", matches)

'''import re: Импорт модуля регулярных выражений (re).

with open("row.txt", "r") as file:: Открытие файла "row.txt" в режиме чтения.

text = file.read(): Чтение содержимого файла и сохранение его в переменной text.

p = re.compile(r'a.*b'): Создание регулярного выражения с паттерном "a.b", 
где 'a' - это символ 'a', '.' - это любой символ (кроме новой строки) 0 или более раз, и 'b' - это символ 'b'.

matches = p.findall(text): Поиск всех соответствий паттерну в тексте и сохранение их в переменной matches.

print("Matches:", matches): Вывод найденных соответствий.

Этот код найдет и выведет все строки в тексте из файла "row.txt", в которых есть символ 'a', 
за которым следует любой символ, и заканчивается символом 'b'.'''