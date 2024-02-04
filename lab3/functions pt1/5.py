from itertools import permutations

def print_permutations():
    input_string = input("Enter a string: ")
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    print("Permutations of the string:")
    for permuted_string in permuted_strings:
        print(permuted_string)

# Example of using the function:
print_permutations()


'''Ниже представлена функция на Python под названием print_permutations, 
которая принимает строку от пользователя и выводит все перестановки этой строки:

1. Импортирован модуль permutations из библиотеки itertools.

2. Определена функция print_permutations без параметров.
3. Внутри функции запрашивается у пользователя ввод строки с помощью функции input().
4. С использованием itertools.permutations создается список permuted_strings, содержащий все перестановки введенной строки.
5. Выводятся на экран все перестановки строки.

Пример использования функции:
print_permutations()
Эта функция принимает строку от пользователя, использует модуль itertools для создания списка всех перестановок этой строки,
и затем выводит их на экран.
'''