class Polynomial:
    def __init__(self, coeffs: list):
        # coeffs[0] là hệ số bậc cao nhất
        self.coeffs = list(coeffs)
        
        # Tiền xử lý: Loại bỏ các hệ số 0 vô nghĩa ở đầu (ví dụ: [0, 0, 2, 1] -> [2, 1])
        while len(self.coeffs) > 1 and self.coeffs[0] == 0:
            self.coeffs.pop(0)

    def __str__(self):
        # Nếu toàn bộ hệ số bằng 0 (hoặc list rỗng)
        if not self.coeffs or all(c == 0 for c in self.coeffs):
            return '0'

        terms = []
        degree = len(self.coeffs) - 1
        
        for i, c in enumerate(self.coeffs):
            if c == 0:
                continue
            
            cur_deg = degree - i
            
            # 1. Xử lý dấu
            if not terms:  # Số hạng đầu tiên
                sign = "-" if c < 0 else ""
            else:          # Các số hạng tiếp theo
                sign = " - " if c < 0 else " + "
            
            # 2. Xử lý hệ số (ẩn số 1 và -1 khi đi kèm với biến x)
            val = abs(c)
            if val == 1 and cur_deg != 0:
                val_str = ""
            else:
                val_str = str(val)
            
            # 3. Xử lý bậc của x
            if cur_deg == 0:
                var_str = ""
            elif cur_deg == 1:
                var_str = "x"
            else:
                var_str = f"x^{cur_deg}"
                
            terms.append(f"{sign}{val_str}{var_str}")
            
        return "".join(terms)

    def __call__(self, x):
        """Đánh giá giá trị đa thức tại x bằng Horner's method"""
        result = 0
        for c in self.coeffs:
            result = result * x + c
        return result

    def __add__(self, other):
        """Cộng hai đa thức"""
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        # Tìm chiều dài tối đa để căn chỉnh
        max_len = max(len(self.coeffs), len(other.coeffs))
        
        # Thêm các số 0 vào đầu (bên trái) list ngắn hơn để cân bằng số lượng hệ số
        c1 = [0] * (max_len - len(self.coeffs)) + self.coeffs
        c2 = [0] * (max_len - len(other.coeffs)) + other.coeffs
        
        # Cộng từng hệ số tương ứng
        new_coeffs = [a + b for a, b in zip(c1, c2)]
        
        return Polynomial(new_coeffs)