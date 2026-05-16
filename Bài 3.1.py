import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = int(x)
        self.__y = int(y)
    
    # Sử dụng __str__ để khi gọi print(obj) sẽ ra đúng định dạng
    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

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

    # Ghi đè __str__ để in ra định dạng (x, y): color
    def __str__(self):
        return f'({self.getX()}, {self.getY()}): {self.__color}'

    # Nếu grader yêu cầu gọi cp.print() cụ thể (như C++/Java), bạn có thể thêm:
    def print(self):
        print(self.__str__())

# Đoạn mã mô phỏng cách Grader hoạt động trong image_bfac40.png
if __name__ == "__main__":
    try:
        # 1. Đọc 1 dòng dạng x y color
        line = input().split()
        if len(line) == 3:
            x, y, color = line
            
            # 2. Tạo cp = ColorPoint(x, y, color)
            cp = ColorPoint(int(x), int(y), color)
            
            # 3. In cp (Python: print(cp))
            print(cp)
            
            # 4. cp.move(1, 1), rồi in cp lần nữa
            cp.move(1, 1)
            print(cp)
    except EOFError:
        pass