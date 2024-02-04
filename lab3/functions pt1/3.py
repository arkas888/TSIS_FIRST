def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        total_legs = (num_chickens * 2) + (num_rabbits * 4)

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None

# Example of using the function:
num_heads = 35
num_legs = 94

solution = solve(num_heads, num_legs)

if solution:
    chickens, rabbits = solution
    print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
else:
    print("No solution found.")


'''Ниже представлена программа на Python с функцией, которая решает классическую головоломку о подсчете количества кур и кроликов на ферме, 
исходя из заданного числа голов и ног:

1. Определена функция solve с параметрами numheads (количество голов) и numlegs (количество ног).
2. В цикле перебираются все возможные варианты количества кур (num_chickens), и для каждого вычисляется количество кроликов (num_rabbits).
3. Проверяется, соответствует ли общее количество ног заданному numlegs.
4. Если найдено соответствие, возвращается кортеж с количеством кур и кроликов, иначе возвращается None.

Пример использования функции:
num_heads = 35
num_legs = 94

solution = solve(num_heads, num_legs)

if solution:
    chickens, rabbits = solution
    print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")
else:
    print("Решение не найдено.")
    Эта программа решает головоломку о распределении голов и ног между курами и кроликами на ферме.
    Функция возвращает количество кур и кроликов, 
    если существует соответствующее распределение, иначе возвращает None.'''