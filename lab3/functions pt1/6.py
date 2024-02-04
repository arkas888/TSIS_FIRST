def reverse_sentence():
    input_string = input("Enter a sentence: ")
    words = input_string.split()
    reversed_sentence = ' '.join(reversed(words))
    
    return reversed_sentence

# Example of using the function:
result = reverse_sentence()
print("Reversed sentence:", result)


'''Ниже представлена функция на Python под названием reverse_sentence, 
которая принимает строку от пользователя и возвращает предложение с перевернутыми словами:

1. Определена функция reverse_sentence без параметров.
2. Внутри функции запрашивается у пользователя ввод строки с помощью функции input().
3. С использованием метода split создается список words, содержащий отдельные слова из введенной строки.
4. С использованием функции ' '.join и reversed создается строка reversed_sentence, в которой слова перевернуты.
5. Результат в виде строки с перевернутыми словами возвращается из функции.

Пример использования функции:
result = reverse_sentence()
print("Перевернутое предложение:", result)
Эта функция принимает строку от пользователя, разделяет ее на отдельные слова,
переворачивает порядок слов и возвращает предложение с перевернутыми словами.'''