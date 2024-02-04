'''Определен класс Shape и его подкласс Square. В классе Square есть функция init, которая принимает длину в качестве аргумента. 
Оба класса имеют функцию area, которая может выводить площадь фигуры, при этом для класса Shape площадь по умолчанию равна 0.

1. Класс Shape:
   - Метод __init__ представляет конструктор класса, но в данном случае он просто передает управление конструктору базового класса.
   - Метод area возвращает 0, представляя площадь общей фигуры (по умолчанию).

2. Класс Square:
   - Метод __init__ принимает длину в качестве аргумента и использует конструктор базового класса с помощью super().
   - Метод area переопределен для вычисления площади квадрата.

Пример использования классов:
shape = Shape()
print("Площадь общей фигуры:", shape.area())

square = Square(5)
print("Площадь квадрата:", square.area())'''

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

# Example of using the classes:
shape = Shape()
print("Area of the generic shape:", shape.area())

square = Square(5)
print("Area of the square:", square.area())
