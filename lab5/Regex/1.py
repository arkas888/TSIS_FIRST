import re

# Read the content of the file
with open("row.txt", "r") as v:
    white = v.read()

# Define the pattern
n = re.compile(r'a*b*')

# Find all matches in the text
c = n.findall(white)

# Print the matches
print(c)

"""import re: Импорт модуля регулярных выражений (re), который предоставляет функциональность для работы с регулярными выражениями в Python.

with open("row.txt", "r") as v:: Открытие файла "row.txt" в режиме чтения и использование конструкции with, 
чтобы автоматически закрыть файл после чтения.

white = v.read(): Чтение содержимого файла и сохранение его в переменной text.

n = re.compile(r'a*b*'): Создание регулярного выражения с паттерном "ab",
где 'a' - это символ 'a', а 'b*' - это ноль или более символов 'b'.

c = n.findall(white): Поиск всех соответствий паттерну в тексте и сохранение их в переменной c.

print(c): Вывод найденных соответствий.

Этот программный код найдет все подстроки, содержащие 'a', за которыми 
следует ноль или более символов 'b', в тексте из файла "row.txt"."""