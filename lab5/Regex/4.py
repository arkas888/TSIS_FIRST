import re

# Read the content of the file
with open("row.txt", "r") as f:
    x = f.read()

# Define the pattern
matter = re.compile(r'[A-Z][a-z]+')

# Find all matches in the text
t = matter.findall(x)

# Print the matches
print(t)

'''import re: Импорт модуля регулярных выражений (re).

with open("row.txt", "r") as f:: Открытие файла "row.txt" в режиме чтения.

x = f.read(): Чтение содержимого файла и сохранение его в переменной x.

matter = re.compile(r'[A-Z][a-z]+'): Создание регулярного выражения с matter "[A-Z][a-z]+",
где [A-Z] соответствует одной заглавной букве, а [a-z]+ - одной или более строчным буквам.

t = matter.findall(x): Поиск всех соответствий паттерну в тексте и сохранение их в переменной matches.

print("Matches:", t): Вывод найденных соответствий.

Этот код найдет и выведет все последовательности, начинающиеся с одной заглавной буквы,
за которой следуют строчные буквы, в тексте из файла "row.txt".'''