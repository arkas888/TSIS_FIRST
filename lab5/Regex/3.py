import re

# Read the content of the file
with open("row.txt", "r") as port:
    point = port.read()

# Define the pattern
rent = re.compile(r'[a-z]+_[a-z]+')

# Find all matches in the text
mart = rent.findall(point)

# Print the matches
print(mart)

'''import re: Импорт модуля регулярных выражений (re).

with open("row.txt", "r") as port:: Открытие файла "row.txt" в режиме чтения.

point = port.read(): Чтение содержимого файла и сохранение его в переменной text.

rent = re.compile(r'[a-z]+_[a-z]+'): Создание регулярного выражения с паттерном "[a-z]+_[a-z]+", где [a-z]+ соответствует одной или
более строчным буквам, за которыми следует символ подчеркивания, а затем снова [a-z]+ для еще одной последовательности строчных букв.

mart = rent.findall(point): Поиск всех соответствий паттерну в тексте и сохранение их в переменной matches.

print(mart) Вывод найденных соответствий.

Этот код найдет и выведет все последовательности строчных букв, объединенных символом подчеркивания, в тексте из файла "row.txt".'''