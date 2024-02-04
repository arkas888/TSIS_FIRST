def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.split()).lower()
    reversed_word = cleaned_word[::-1]
    return cleaned_word == reversed_word

# Example of using the function:
input_word = input("Enter a word or phrase: ")
result = is_palindrome(input_word)

if result:
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")


'''Ниже представлена функция на Python под названием is_palindrome, которая проверяет, является ли слово или фраза палиндромом:

1. Определена функция is_palindrome с параметром word, представляющим слово или фразу.
2. Удаляются пробелы и преобразуется к нижнему регистру для регистронезависимого сравнения.
3. Создаются две строки: cleaned_word (очищенное слово) и reversed_word (слово в обратном порядке).
4. Возвращается результат сравнения cleaned_word и reversed_word.

Пример использования функции:
input_word = input("Введите слово или фразу: ")
result = is_palindrome(input_word)

if result:
    print(f"{input_word} является палиндромом.")
else:
    print(f"{input_word} не является палиндромом.")
Эта функция проверяет, является ли введенное слово или фраза палиндромом, убирая пробелы и регистр для более точного сравнения. 
Если введенное слово или фраза читается одинаково как с начала, так и с конца, то они считаются палиндромами.'''