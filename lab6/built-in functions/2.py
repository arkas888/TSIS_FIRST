def count_upper_lower(input_string):
    # Используем встроенные функции isupper() и islower() для проверки каждого символа
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    
    return upper_count, lower_count

def main():
    # Вводим строку от пользователя
    user_input = input("Введите строку: ")

    # Вызываем функцию для подсчета заглавных и строчных букв
    upper, lower = count_upper_lower(user_input)

    # Выводим результат
    print(f"Количество заглавных букв: {upper}")
    print(f"Количество строчных букв: {lower}")

if __name__ == "__main__":
    main()
    
'''Создаем функцию count_upper_lower(input_string), которая принимает строку и использует встроенные 
методы isupper() и islower() для проверки каждого символа.

С использованием генераторов списков и функции sum(), считаем количество заглавных и строчных букв.

В функции main() запрашиваем у пользователя ввод строки.

Вызываем функцию count_upper_lower(user_input) для подсчета заглавных и строчных букв.

Выводим результат.

Таким образом, программа использует встроенные методы isupper() и islower() для проверки каждого символа в строке и 
подсчитывает количество заглавных и строчных букв с использованием генераторов списков и функции sum().'''