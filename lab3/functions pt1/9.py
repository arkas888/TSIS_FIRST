import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative."
    
    volume = (4/3) * math.pi * radius**3
    return volume

# Example of using the function:
radius_value = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius_value)
print(f"The volume of the sphere with radius {radius_value} is: {result:.2f}")


'''Ниже представлена функция на Python под названием sphere_volume, которая вычисляет объем сферы по заданному радиусу:

1. Импортирован модуль math для использования числа π (pi).
2. Определена функция sphere_volume с параметром radius, представляющим радиус сферы.
3. Добавлена проверка, что радиус не может быть отрицательным.
4. Вычислен объем сферы по формуле: объем = (4/3) * π * r^3.
5. Результат в виде объема сферы возвращается из функции.

Пример использования функции:
radius_value = float(input("Введите радиус сферы: "))
result = sphere_volume(radius_value)
print(f"Объем сферы с радиусом {radius_value} равен: {result:.2f}")
Эта функция принимает радиус сферы в качестве аргумента, вычисляет объем сферы по заданной формуле и возвращает результат.
В приведенном примере пользователю предлагается ввести радиус, и затем выводится объем со сферой с этим радиусом.'''