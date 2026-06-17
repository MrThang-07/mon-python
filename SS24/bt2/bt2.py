# (1) Phân tích

# Hậu quả nếu để thuộc tính points tự do (public):

# Làm mất tính toàn vẹn dữ liệu (Data Integrity): Hệ thống không có màng lọc kiểm duyệt nên bất kỳ ai cũng có thể can thiệp trực tiếp từ bên ngoài để sửa điểm thành số âm hoặc chuỗi chữ.
# Gây sập hệ thống (Crash): Nếu points bị gán nhầm thành một chuỗi (ví dụ: "một trăm"), thì khi chạy hàm add_points thực hiện phép toán +=, Python sẽ ném ra lỗi TypeError và làm ứng dụng dừng hoạt động ngay lập tức.
# Decorator dùng để tạo "bộ lọc" dữ liệu:

# Chúng ta cần sử dụng cặp Decorator @property (để tạo hàm đọc dữ liệu) và @<tên_biến>.setter (để tạo bộ lọc kiểm tra tính hợp lệ của dữ liệu trước khi cho phép gán giá trị mới).
# Tại sao truyền tham số self vào is_eligible_for_voucher là tồi?Tham số self đại diện cho một đối tượng (chiếc thẻ) cụ thể. Trong khi đó, logic kiểm tra hóa đơn $200k$ chỉ phụ thuộc vào số tiền của hóa đơn (bill_amount), hoàn toàn không sử dụng bất kỳ thông tin nào của thẻ (như tên khách hay số điểm).Việc ép dùng self bắt buộc hệ thống phải tạo ra một object thẻ thành viên "ảo" thì mới gọi được hàm này, gây lãng phí bộ nhớ và không thực tế đối với khách vãng lai chưa có thẻ.
# Decorator tạo hàm tiện ích độc lập và sự khác biệt với @classmethod:

# Để gọi hàm trực tiếp từ Class mà không cần tạo object, ta dùng Decorator @staticmethod.

# Sự khác biệt:

# @staticmethod: Không nhận bất kỳ tham số mặc định nào (self hay cls). Nó hoạt động giống hệt một hàm bình thường nhưng được gom nhóm vào trong Class để quản lý cho gọn.

# @classmethod: Bắt buộc phải nhận tham số đầu tiên là cls (đại diện cho chính cái Class đó). Thường dùng khi muốn truy cập vào các biến dùng chung của toàn Class hoặc làm hàm khởi tạo thay thế (Factory Method).
# (2) Viết code 
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        # Khởi tạo điểm ẩn danh thông qua Name Mangling
        self.__points = 0
        
        # Sử dụng luôn setter để kiểm duyệt dữ liệu ngay khi khởi tạo chiếc thẻ
        self.points = points

    # Hàm Getter: Cho phép đọc điểm từ bên ngoài thông qua tên thuộc tính sạch
    @property
    def points(self):
        return self.__points

    # Hàm Setter: Màng lọc kiểm duyệt dữ liệu đầu vào nghiêm ngặt
    @points.setter
    def points(self, value):
        if not isinstance(value, int) or value < 0:
            print("Dữ liệu điểm không hợp lệ!")
        else:
            self.__points = value

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng thêm phải là số nguyên lớn hơn 0!")

    # Chuyển thành Static Method: Hàm tiện ích độc lập dùng chung cho toàn hệ thống
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


# --- KỊCH BẢN KIỂM THỬ HỆ THỐNG MỚI ---

# Khởi tạo thẻ ban đầu với 100 điểm
card1 = MemberCard("Le Van C", 100)

print("--- THỬ NGHIỆM 1: Thu ngân cố tình gán điểm sai quy định ---")
card1.points = -50  # Hệ thống sẽ chặn lại và in ra thông báo lỗi

print("\n--- THỬ NGHIỆM 2: Kiểm tra voucher trực tiếp từ tên Class ---")
# Gọi hàm check voucher trực tiếp từ Class MemberCard (Không cần qua object card1)
result = MemberCard.is_eligible_for_voucher(250000)

print("\n--- KẾT QUẢ HIỂN THỊ CUỐI CÙNG ---")
# Điểm vẫn giữ nguyên là 100 chứ không bị đổi thành -50
print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")