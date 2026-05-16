from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        return float
class Circle(Shape):
    def __init__(self, r=int):
        super().__init__()
        self.r=r
    def area(self):
        return math.pi*self.r*self.r
class Rectangle(Shape):
    def __init__(self, w=int, h=int):
            super().__init__()
            self.w, self.h=w, h
    def area(self):
            return self.w*self.h