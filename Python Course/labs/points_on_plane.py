import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):
        distance1 = self.__vertice1.distance_from_point(self.__vertice2)
        distance2 = self.__vertice2.distance_from_point(self.__vertice3)
        distance3 = self.__vertice3.distance_from_point(self.__vertice1)
        return distance1 + distance2 + distance3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
