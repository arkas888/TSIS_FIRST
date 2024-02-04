def spy_game(nums):
    # Initialize variables to track the sequence
    sequence = [0, 0, 7]
    index = 0
    
    # Iterate through the list
    for num in nums:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    
    return False

# Examples of using the function:
result1 = spy_game([1, 2, 4, 0, 0, 7, 5])
print(result1)  # Output: True

result2 = spy_game([1, 0, 2, 4, 0, 5, 7])
print(result2)  # Output: True

result3 = spy_game([1, 7, 2, 0, 4, 5, 0])
print(result3)  # Output: False


'''Ниже представлена функция на Python под названием spy_game, которая принимает список целых чисел и возвращает `True`, 
если в нем есть последовательность 0, 0, 7:

1. Определена функция spy_game с параметром nums, представляющим список целых чисел.
2. Создан список sequence, представляющий требуемую последовательность [0, 0, 7].
3. Используется переменная index для отслеживания текущего элемента в последовательности.
4. В цикле for перебираются элементы списка nums.
5. Если текущий элемент равен ожидаемому элементу в последовательности, index увеличивается.
6. Если index достигает длины sequence, возвращается `True`, так как полная последовательность обнаружена.
7. Если цикл завершился без нахождения полной последовательности, возвращается `False`.

Примеры использования функции:
result1 = spy_game([1, 2, 4, 0, 0, 7, 5])
print(result1)  # Вывод: True

result2 = spy_game([1, 0, 2, 4, 0, 5, 7])
print(result2)  # Вывод: True

result3 = spy_game([1, 7, 2, 0, 4, 5, 0])
print(result3)  # Вывод: False
Эта функция проверяет наличие последовательности 0, 0, 7 в заданном порядке в списке целых чисел и возвращает True,
если такая последовательность обнаружена, и False в противном случае.'''