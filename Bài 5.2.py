class Vector2D:
    def __init__(self, x=int, y=int):
        self.x=x
        self.y=y
    def __str__(self):
        return (f'({self.x}, {self.y})')
    def __add__(self,other):
        dx=self.x+other.x
        dy=self.y+other.y
        return Vector2D(dx,dy)
    def __sub__(self,other):
        return Vector2D(self.x-other.x, self.y-other.y)
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    def __eq__(self,other):
        if not isinstance(other,Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y