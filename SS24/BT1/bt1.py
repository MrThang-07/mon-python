(1) Phân tích
# 1. Việc gán trực tiếp order_table1.total_amount = 0 từ bên ngoài đang vi phạm tính chất cốt lõi nào?

# Việc này vi phạm nghiêm trọng Tính đóng gói (Encapsulation). Tính đóng gói yêu cầu trạng thái bên trong của một đối tượng phải được che giấu và chỉ được thay đổi thông qua các phương thức công khai (public methods) do chính class đó cung cấp, tránh việc can thiệp trái phép từ bên ngoài.

# 2. Để kích hoạt cơ chế Name Mangling trong Python, ta cần đổi tên thuộc tính total_amount thành gì?

# Ta cần thêm hai dấu gạch dưới (__) vào trước tên thuộc tính, đổi thành: __total_amount (gọi là private attribute).

# 3. Sau khi che giấu, nếu muốn xem tổng tiền (chỉ đọc, không sửa) từ bên ngoài, ta cần dùng Decorator nào?

# Ta cần sử dụng Decorator @property để biến một phương thức thành một thuộc tính chỉ đọc (Read-only property).

# 4. Tại dòng lệnh self.vat_rate = new_rate, Python thực chất đang làm hành động gì?

# Python không hề thay đổi biến Class vat_rate. Thay vào đó, nó tự động tạo ra một biến Instance mới cũng tên là vat_rate và gắn riêng cho đối tượng order_table1. Điều này làm lu mờ (shadowing) biến Class, dẫn đến việc chỉ có Bàn 1 bị đổi thuế, còn Bàn 2 (và các bàn khác tạo sau này) vẫn tham chiếu đến biến Class gốc là 10%.

# 5. Để cập nhật thuế cho toàn bộ hệ thống, ta phải dùng Decorator nào và thay tham số self bằng gì?

# Ta phải sử dụng Decorator @classmethod và thay thế tham số self bằng cls (viết tắt của Class). Lúc này, phương thức sẽ tác động trực tiếp lên Class Attribute thay vì từng Instance riêng lẻ.
# (2) Sửa code 
# Hệ thống quản lý hóa đơn Rikkei Coffee - Đã bảo mật & đồng bộ
class CoffeeOrder:
    # Thuộc tính của lớp (Class Attribute) - Áp dụng chung cho toàn hệ thống
    __vat_rate = 0.10  # Để private để tránh chỉnh sửa tùy tiện từ bên ngoài

    def __init__(self, table_number):
        self.table_number = table_number
        # Giải quyết lỗ hổng 1: Sử dụng private attribute (__), kích hoạt Name Mangling
        self.__total_amount = 0  

    # Getter: Cho phép xem tổng tiền một cách an toàn (Chỉ đọc)
    @property
    def total_amount(self):
        return self.__total_amount

    # Getter cho VAT rate (để kịch bản test có thể truy cập)
    @property
    def vat_rate(self):
        return CoffeeOrder.__vat_rate

    # Phương thức thêm tiền món ăn vào hóa đơn
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price
        else:
            print("Giá món ăn không hợp lệ!")

    # Tính tổng tiền khách phải trả (đã cộng VAT)
    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder.__vat_rate)

    # Giải quyết lỗ hổng 2: Chuyển thành Class Method để đồng bộ toàn hệ thống
    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1: # Thêm validation cơ bản cho an toàn
            cls.__vat_rate = new_rate
        else:
            print("Tỷ lệ thuế không hợp lệ!")


# --- KỊCH BẢN KIỂM CHỨNG HỆ THỐNG ---

# Khách vào quán, hệ thống mở hóa đơn cho 2 bàn
order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

# Khách gọi món
order_table1.add_item(50000) # Bàn 1 gọi Cà phê sữa (50k)
order_table2.add_item(30000) # Bàn 2 gọi Trà đào (30k)

print("--- THỬ NGHIỆM TẤN CÔNG & CẬP NHẬT THUẾ ---")

# 1. Nhân viên gian lận cố tình gán đè tổng tiền của Bàn 1 về 0 từ bên ngoài
try:
    # Lệnh này sẽ ném ra lỗi AttributeError vì property 'total_amount' không có setter
    order_table1.total_amount = 0
except AttributeError as e:
    print(f"[BẢO MẬT] Ngăn chặn thành công! Lỗi: {e}")

# Cố tình can thiệp bằng biến private __total_amount (cú pháp cũ) cũng sẽ thất bại
order_table1.__total_amount = 0 # Hành động này thực chất tạo ra một biến phụ độc lập, không làm thay đổi biến gốc bên trong class

# 2. Quản lý chi nhánh cập nhật thuế VAT xuống 8% (0.08) thông qua Class Method
CoffeeOrder.update_vat_rate(0.08)

print("\n--- KẾT QUẢ ĐẦU RA CONSOLE ---")
print(f"Tổng tiền gốc Bàn 1: {order_table1.total_amount} VNĐ (Không bị sửa về 0)")
print(f"Tổng tiền Bàn 1 (sau VAT 8%): {order_table1.calculate_final_bill()} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate * 100}%")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate * 100}%")