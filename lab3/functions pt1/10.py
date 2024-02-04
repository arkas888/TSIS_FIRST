def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example of using the function:
original_list = [1, 2, 3, 1, 2, 4, 5]
result = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", result)


'''Ниже представлена функция на Python под названием unique_elements, 
которая принимает список и возвращает новый список с уникальными элементами, без использования множества (set):

1. Определена функция unique_elements с параметром input_list, представляющим исходный список.
2. Создан пустой список unique_list, предназначенный для хранения уникальных элементов.
3. В цикле for перебираются элементы из исходного списка.
4. Для каждого элемента проверяется, отсутствует ли он уже в unique_list, и если да, то добавляется в unique_list.
5. Результат в виде нового списка с уникальными элементами возвращается из функции.

Пример использования функции:
original_list = [1, 2, 3, 1, 2, 4, 5]
result = unique_elements(original_list)
print("Исходный список:", original_list)
print("Список с уникальными элементами:", result)
Эта функция принимает список, проходится по его элементам, и для каждого элемента проверяет, 
был ли он уже добавлен в новый список unique_list. Если элемент не был добавлен,
он добавляется, и таким образом формируется новый список с уникальными элементами.'''