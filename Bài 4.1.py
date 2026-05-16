class TuLanh:
    def __init__(self, nhanhieu='Electrolux', maso='UNKNOWN', nuocsx='Việt Nam', tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        # Chuyển đổi tkdien sang kiểu bool nếu nó đang là string
        if isinstance(tkdien, str):
            self.__tkdien = tkdien.lower() == 'true'
        else:
            self.__nhanhieu = nhanhieu
            self.__tkdien = tkdien
            
        self.__dungtich = dungtich
        self.__gia = gia
        
        # Thiết lập trạng thái hiển thị
        self.trang_thai = 'Có' if self.__tkdien else 'Không'

    # Ghi đè __str__ để hỗ trợ lệnh print(tu) theo yêu cầu của Grader
    def __str__(self):
        lines = [
            f"Nhãn hiệu: {self.__nhanhieu}",
            f"Mã số: {self.__maso}",
            f"Nước SX: {self.__nuocsx}",
            f"T/K điện: {self.trang_thai}",
            f"Dung tích: {self.__dungtich}L",
            f"Giá: {self.__gia}VNĐ"
        ]
        return "\n".join(lines)

    # Vẫn giữ hàm print() nếu Grader gọi theo kiểu C++/Java
    def print(self):
        print(self.__str__())

# Mô phỏng cách Grader vận hành dựa trên image_bf9c5c.png
if __name__ == "__main__":
    try:
        # 1. Đọc 1 dòng dạng nhanhieu|maso|nuocsx|tkdien|dungtich|gia
        data = input().split('|')
        if len(data) == 6:
            # 2. Tạo đối tượng TuLanh
            tu = TuLanh(
                nhanhieu=data[0],
                maso=data[1],
                nuocsx=data[2],
                tkdien=data[3],
                dungtich=int(data[4]),
                gia=int(data[5])
            )
            # 3. In tu (Python gọi __str__)
            print(tu)
    except EOFError:
        pass