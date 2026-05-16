class Temperature:
    def __init__(self,celsius=0.0):
        self._c=0.0
        self.celsius= celsius
        # Gọi setter để kiểm tra dữ liệu ngay khi khởi tạo
    @property #Property xong vẫn gọi hàm
    def celsius(self):
        return self._c
    @celsius.setter
    def celsius(self, value=float):
        if value<-273.15:
            raise ValueError
        self._c=value
    @property
    def fahrenheit(self):
        return float(self._c*9/5+32)
    
    @fahrenheit.setter
    def fahrenheit(self, value=float):
        self.celsius=(value-32)*5/9
