import math

class Point:
    def __init__ (self,x=0,y=0):
        self.__x = x
        self.__y = y
    
    def read(self):
        data = input().split()
        self.__x = int(data[0])
        self.__y = int(data[1])

    def print(self):
        pass
    
    def move(self,dx,dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    
    def getY(self):   
        return self.__y
    def distance(self,other):
        d = math.sqrt((self.__x - other.getX())**2 + (self.__y - other.getY())**2)
        return d