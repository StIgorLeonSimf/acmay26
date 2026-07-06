import math

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calk_square(self):
        pass

    def display(self):
        print(self.name)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height

    def calk_square(self):
        return self.width * self.height

    def display(self):
        super().display()
        print(f'Ширина: {self.width}\nВысота: {self.height}\n'
              f'Площадь: {self.calk_square()}')


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Круг')
        self.radius = radius

    def calk_square(self):
        return (self.radius ** 2 * math.pi)

    def display(self):
        super().display()
        print(f'Радиус: {self.radius}\nПлощадь: {self.calk_square():.2f} ')



if __name__ == '__main__':
    rect = Rectangle(2, 3)
    rect.display()
    c = Circle(3)
    c.display()