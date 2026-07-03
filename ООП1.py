# def summator(*v):
#     x = 0
#     y = 0
#     for k, vy in v:
#         x += k
#         y += vy
#     return x, y
#
#
# v1 = (10, 20)
# v2 = (10, 2)
# v = v1 + v2
# print(v)
# print(type(v))
# v = summator(v1, v2)
# print(v)
# class Vector(object):

import matplotlib.pyplot as plt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cnt = 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def display_add(self, other):
        res = self + other
        v1x = (0,self.x)
        v1y = (0,self.y)
        v2x = (0, other.x)
        v2y = (0,other.y)
        rx = [0, res.x]
        ry = [0, res.y]
        plt.plot(v1x, v1y, v2x, v2y, rx, ry, '-.',lw=4)
        plt.show()

    def __str__(self):
        return f'V({self.x}, {self.y})'


v1 = Vector(10, 20)
v2 = Vector(10, 2)
v3 = Vector(5, 5)
# print(v1.x, v1.y)
print(v1, v2)
v = v1 + v2 + v3
print(v)
v1.display_add(v2)