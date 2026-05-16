import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = int(x)
        self.__y = int(y)
        
    def read(self):
        data = input().split()
        if len(data) >= 2:
            self.__x = int(data[0])
            self.__y = int(data[1])

    def print(self):
        print(f'({self.__x}, {self.__y})')

    def move(self, dx, dy):
        self.__x = dx + self.__x
        self.__y = dy + self.__y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def distance(self):
        kq = math.sqrt(self.__x**2 + self.__y**2)
        return f'{kq:.1f}'

    def distance_point(self, other):
        dx = other.getX() - self.__x
        dy = other.getY() - self.__y
        kq2 = math.sqrt(dx**2 + dy**2)
        return f'{kq2:.1f}'


class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.getColor()
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.__color = str(color)
        else:
            super().__init__(0, 1)
            self.__color = 'xanh'

    def getColor(self):
        return self.__color

    def read(self):
        data = input().split()
        if len(data) >= 3:
            self.setXY(int(data[0]), int(data[1]))
            self.__color = str(data[2])

    def print(self):
        print(f'({self.getX()}, {self.getY()}): {self.__color}')

    def setColor(self, color):
        self.__color = str(color)
        
class ColorPointTest:
    def testCase(self):
        c1 = ColorPoint()
        c1.print()
        c2 = ColorPoint()
        c2.read()
        c2.print()
        c3 = ColorPoint(c2)
        c2.move(5, 5)
        c2.print()
        c3.print()