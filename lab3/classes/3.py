'''Определен класс Rectangle, который наследует от класса Shape из задачи 2. Экземпляр класса может быть создан с помощью длины и ширины. 
Класс Rectangle имеет метод, который вычисляет площадь.

1. Класс Rectangle:
   - Метод __init__ принимает длину и ширину в качестве аргументов и использует конструктор базового класса с помощью super().
   - Метод area переопределен для вычисления площади прямоугольника на основе переданных значений длины и ширины.

Пример использования класса:
rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())'''

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0 
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example of using the class:
rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area())


# Example of using the class:
rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area())