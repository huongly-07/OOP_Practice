import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x, self.__y = x, y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def read(self):
        try:
            line = input().split()
            if len(line) == 2:
                self.__x, self.__y = float(line[0]), float(line[1])
            else:
                self.__x = float(line[0])
                self.__y = float(input())
        except:
            pass
    
    def print(self):
        print(f"({self.__x:.0f}, {self.__y:.0f})")

    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def distance_to_other(self, other):
        return math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

class PointTest:
    def testCase(self):
        p1 = Point()
        p1.print()

        p2 = Point()
        p2.read()
        p2.print()
        
        p2.move(1, 1)
        p2.print()
      
        print(f"{p2.distance():.1f}")

if __name__ == '__main__':
    tester = PointTest()
    tester.testCase()