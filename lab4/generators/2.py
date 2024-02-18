def generate_even_numbers(N):
    for number in range(N + 1):
        if number % 2 == 0:
            yield number

# Ввод значения N с консоли
N = int(input("Введите значение N: "))

# Генерация чётных чисел от 0 до N
even_numbers_generator = generate_even_numbers(N)

# Преобразование результатов в строку с разделением запятой
even_numbers_str = ', '.join(map(str, even_numbers_generator))

# Вывод результата
print(f"Чётные числа от 0 до {N} в виде строки с разделением запятой: {even_numbers_str}")

'''Функция generate_even_numbers создана с использованием ключевого слова yield для генерации чётных чисел от 0 до N.
Пользователь вводит значение N с консоли.
Создается объект генератора even_numbers_generator, который генерирует чётные числа.
Результаты генератора преобразуются в строку с разделением запятой с использованием ', '.join(map(str, even_numbers_generator)).
Результат выводится на экран в виде строки с чётными числами от 0 до N, разделёнными запятой.'''
