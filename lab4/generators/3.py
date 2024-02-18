def generate_numbers_divisible_by_3_and_4(n):
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number

# Пример использования функции с генератором
n = int(input("Введите значение n: "))
divisible_numbers_generator = generate_numbers_divisible_by_3_and_4(n)

# Вывод результатов
print(f"Числа, делящиеся на 3 и 4 в диапазоне от 0 до {n}:")
for num in divisible_numbers_generator:
    print(num)
    
'''Функция generate_numbers_divisible_by_3_and_4 создана с использованием ключевого слова yield для генерации чисел,
которые делятся на 3 и 4 в пределах от 0 до n.
Пользователь вводит значение n с консоли.
Создается объект генератора divisible_numbers_generator, который генерирует числа, соответствующие условиям деления на 3 и 4.
Результаты генератора выводятся на экран в виде чисел, делящихся на 3 и 4, в пределах от 0 до n.'''