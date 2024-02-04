def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Example of using the function:
input_numbers = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)


'''Ниже представлена функция на Python под названием filter_prime, 
которая принимает список чисел в качестве аргумента и возвращает только простые числа из списка:

1. Определена вспомогательная функция is_prime, которая проверяет, является ли число простым. 
Если число меньше 2, оно не является простым. Далее проводится проверка делителей в диапазоне от 2 до квадратного корня из числа.

2. Определена функция filter_prime с параметром numbers, представляющим список чисел.
3. Внутри функции применяется функция filter с использованием is_prime для фильтрации простых чисел из списка.
4. Результат в виде списка простых чисел возвращается из функции.

Пример использования функции:
input_numbers = input("Введите числа, разделенные пробелами: ")
numbers_list = list(map(int, input_numbers.split()))

prime_numbers = filter_prime(numbers_list)
print("Простые числа:", prime_numbers)
Эта функция принимает список чисел, применяет фильтрацию с использованием вспомогательной 
функции is_prime и возвращает только простые числа из списка.'''