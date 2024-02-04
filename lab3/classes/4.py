'''Определен класс Point с требуемыми методами:

1. Метод __init__ является конструктором класса и инициализирует объект класса с заданными координатами x и y.

2. Метод show выводит координаты точки.

3. Метод move изменяет координаты точки на новые значения, переданные в качестве аргументов.

4. Метод dist вычисляет расстояние между текущей точкой и другой точкой, переданной в качестве аргумента, 
используя формулу расстояния между двумя точками в декартовой системе координат.

Пример использования класса:
point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Расстояние между двумя точками: {distance}")

point1.move(1, 1)
point1.show()'''


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# Example of using the class:
point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between the two points: {distance}")

point1.move(1, 1)
point1.show()