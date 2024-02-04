def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)

'''Ниже представлен простой программный код на Python, который использует функцию filter 
и lambda-функцию для фильтрации простых чисел из заданного списка:

1. Определенная функция is_prime проверяет, является ли число простым. Если число меньше 2, 
оно не является простым. Далее проводится проверка делителей в диапазоне от 2 до квадратного корня из числа.

2. Задан список чисел numbers.

3. С использованием функции filter и lambda-функции фильтруются простые числа из списка.

4. Результат выводится на экран, показывая оригинальный список и список простых чисел.

Пример использования функции filter с lambda-функцией для фильтрации простых чисел:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Использование filter с lambda-функцией для фильтрации простых чисел
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Оригинальный список:", numbers)
print("Простые числа:", prime_numbers)'''