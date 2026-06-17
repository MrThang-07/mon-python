# (1) Phân tích
# 1. Tại sao point_value_vnd là Class Attribute?
# Lý do: Tỷ giá quy đổi điểm (1 điểm = 1,000 VNĐ) là một quy định chung áp dụng đồng loạt cho toàn hệ thống, không phải là tài sản riêng của bất kỳ khách hàng nào.

# Rắc rối nếu khai báo trong __init__ (dạng Instance Attribute): Nếu bạn dùng self.point_value_vnd = 1000, mỗi chiếc thẻ được tạo ra sẽ tự giữ riêng một bản sao của con số 1000 này trong bộ nhớ của nó. Khi Ban giám đốc muốn đổi tỷ giá lên thành 2,000 VNĐ ở Chức năng 5, bạn sẽ phải dùng vòng lặp for để đi tìm từng chiếc thẻ trong database rồi sửa thủ công cho từng người. Nếu hệ thống có 1 triệu khách hàng, việc này sẽ làm treo máy chủ ngay lập tức, chưa kể phát sinh lỗi lệch tỷ giá giữa thẻ cũ và thẻ mới tạo.

# 2. Tại sao is_valid_card_id nên dùng @staticmethod?
# Lý do: Hàm này làm nhiệm vụ kiểm tra xem chuỗi chữ do thu ngân nhập vào ("RC01", "RC100") có đúng định dạng quy định hay không. Logic kiểm tra này hoàn toàn độc lập, nó diễn ra trước khi một chiếc thẻ chính thức được sinh ra.

# Có cần tạo object trước không? Hoàn toàn KHÔNG. Nếu bắt tạo object thẻ trước rồi mới check, chúng ta sẽ rơi vào tình huống "tiến thoái lưỡng nan": lỡ tạo ra một chiếc thẻ có mã lỗi trong bộ nhớ rồi thì hệ thống sẽ bị nhiễm dữ liệu rác. Dùng @staticmethod giúp ta gọi trực tiếp thông qua tên Class MemberCard.is_valid_card_id(card_id) để làm bộ lọc ngay từ cửa vào cửa hàng.

# 3. Tính Đóng gói thông qua Name Mangling (__points, __tier) giải quyết bài toán gì?
# Giải quyết bài toán gian lận dữ liệu điểm số và hạng thẻ: Trong kinh doanh, điểm thưởng có giá trị quy đổi ra tiền mặt. Nếu để public, nhân viên thu ngân gian lận có thể cấu kết với khách hàng để gõ bừa lệnh card.points = 999999 hoặc tự sửa card.tier = "VIP" để trục lợi voucher.

# Khi dùng dấu gạch dưới kép __, Python sẽ khóa chặt quyền truy cập trực tiếp từ bên ngoài. Điểm số và hạng thẻ lúc này chỉ có thể thay đổi thông qua các "quy trình nghiệp vụ" chính thống được kiểm soát nghiêm ngặt là earn_points (khi có hóa đơn mua hàng thật) và redeem_points (khi khách đồng ý trừ điểm).
# (2) Viết code 
class MemberCard:
    # Class Attribute - Tỷ giá quy đổi dùng chung cho toàn hệ thống
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()  # Chuẩn hóa tên viết hoa các chữ cái đầu
        self.__points = 0         # Bảo mật nghiêm ngặt bằng Name Mangling
        self.__tier = "Standard"  # Hạng thẻ mặc định ban đầu

    # --- GETTERS (@property) ---
    @property
    def points(self):
        """Hàm đọc điểm an toàn từ bên ngoài, không có setter đi kèm."""
        return self.__points

    @property
    def tier(self):
        """Hàm đọc hạng thẻ an toàn từ bên ngoài, không có setter đi kèm."""
        return self.__tier

    # --- STATIC METHOD (@staticmethod) ---
    @staticmethod
    def is_valid_card_id(card_id):
        """
        Bẫy lỗi định dạng thẻ:
        - Phải có độ dài đúng bằng 4 ký tự.
        - Phải bắt đầu bằng chữ 'RC' (Viết hoa nghiêm ngặt).
        - 2 ký tự cuối bắt buộc phải là số.
        """
        if len(card_id) != 4:
            return False
        if not card_id.startswith("RC"):
            return False
        if not card_id[2:].isdigit():
            return False
        return True

    # --- CLASS METHOD (@classmethod) ---
    @classmethod
    def update_point_value(cls, new_value):
        """Cập nhật tỷ giá mới đồng loạt cho toàn bộ Class."""
        cls.point_value_vnd = new_value

    # --- INSTANCE METHODS (Phương thức đối tượng) ---
    def earn_points(self, bill_amount):
        """Tích điểm dựa trên hóa đơn và tự động xét thăng hạng VIP."""
        points_earned = int(bill_amount / 10000)  # Lấy phần nguyên theo quy định
        self.__points += points_earned
        
        # Tự động thăng hạng lên VIP nếu đạt đủ điều kiện điểm tích lũy
        if self.__points >= 100:
            self.__tier = "VIP"
            
        return points_earned

    def redeem_points(self, points_to_use):
        """
        Tiêu điểm đổi ưu đãi giảm giá:
        - Trả về bộ dữ liệu (True, số tiền giảm) nếu thành công.
        - Trả về (False, 0) nếu dính bẫy tiêu quá số điểm đang có.
        """
        if points_to_use <= 0 or points_to_use > self.__points:
            return False, 0
        
        discount_amount = points_to_use * MemberCard.point_value_vnd
        self.__points -= points_to_use
        return True, discount_amount


# ======================================================
# LUỒNG ĐIỀU PHỐI CHƯƠNG TRÌNH CHÍNH (MAIN APPLICATION)
# ======================================================

# Cơ sở dữ liệu danh sách thẻ giả lập ban đầu để dễ test kịch bản đề bài
cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]

# Nạp sẵn dữ liệu điểm mẫu cho giống kịch bản kiểm thử của đề bài
cards_database[0].earn_points(1500000)  # RC01 có 150 điểm -> Hạng VIP
cards_database[1].earn_points(200000)   # RC02 có 20 điểm -> Hạng Standard

def find_card(card_id):
    """Hàm phụ trợ tìm kiếm thẻ trong database theo mã card_id."""
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None

def main():
    while True:
        print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
        print("1. Xem danh sách thẻ thành viên")
        print("2. Đăng ký thẻ mới")
        print("3. Khách mua hàng (Tích điểm)")
        print("4. Khách dùng điểm (Đổi ưu đãi)")
        print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            if not cards_database:
                print("Hệ thống hiện chưa có thẻ thành viên nào.")
            else:
                for idx, card in enumerate(cards_database, 1):
                    # Gọi trực tiếp qua thuộc tính property sạch sẽ, không dùng dấu ngoặc ()
                    print(f"{idx}. Mã: {card.card_id} | Tên: {card.name:<18} | Điểm: {card.points:<4} | Hạng: {card.tier}")
                    
        elif choice == "2":
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip()
            
            # Kiểm tra bẫy định dạng mã thẻ trước bằng Static Method
            if not MemberCard.is_valid_card_id(card_id):
                print("\nLỗi định dạng! Mã thẻ phải bắt đầu bằng 'RC' và kèm 2 chữ số (Ví dụ: RC01).")
                continue
                
            # Kiểm tra trùng lặp mã thẻ trong hệ thống
            if find_card(card_id) is not None:
                print("\nMã thẻ đã tồn tại trong hệ thống!")
                print("Vui lòng kiểm tra lại.")
                continue
                
            name = input("Nhập tên khách hàng: ").strip()
            if not name:
                print("Tên khách hàng không được để trống!")
                continue
                
            # Khởi tạo đối tượng mới an toàn và thêm vào danh sách
            new_card = MemberCard(card_id, name)
            cards_database.append(new_card)
            
            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}")
            print(f"Tên khách hàng: {new_card.name}")
            print(f"Điểm ban đầu: {new_card.points}")
            print(f"Hạng thẻ: {new_card.tier}")
            
        elif choice == "3":
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã thẻ: ").strip()
            card = find_card(card_id)
            
            if card is None:
                print("Không tìm thấy mã thẻ này trong hệ thống!")
                continue
                
            try:
                bill_amount = int(input("Nhập tổng tiền hóa đơn: ").strip())
                if bill_amount < 0:
                    print("Số tiền hóa đơn không thể là số âm!")
                    continue
            except ValueError:
                print("Vui lòng nhập số tiền hợp lệ!")
                continue
                
            old_tier = card.tier
            points_earned = card.earn_points(bill_amount)
            
            print(f"\nKhách hàng: {card.name}")
            print(f"Hóa đơn: {bill_amount:,} VNĐ")
            print(f"Số điểm được tích: {points_earned}")
            print(f"Tổng điểm hiện tại: {card.points}")
            
            # Kiểm tra xem khách có được thăng hạng VIP ngay trong giao dịch này không
            if old_tier == "Standard" and card.tier == "VIP":
                print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")
            print(f"Hạng thẻ hiện tại: {card.tier}")
            
        elif choice == "4":
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            print(f"Tỷ giá hiện tại là: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            card_id = input("Nhập mã thẻ: ").strip()
            card = find_card(card_id)
            
            if card is None:
                print("Không tìm thấy mã thẻ này trong hệ thống!")
                continue
                
            try:
                points_to_use = int(input("Nhập số điểm muốn sử dụng: ").strip())
            except ValueError:
                print("Vui lòng nhập số điểm là số nguyên!")
                continue
                
            # Gọi phương thức nghiệp vụ tiêu điểm
            success, discount = card.redeem_points(points_to_use)
            
            if success:
                print(f"\nĐã trừ {points_to_use} điểm.")
                print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
                print(f"Số điểm còn lại: {card.points}")
                print(f"Hạng thẻ hiện tại: {card.tier}")
            else:
                print("\nKhông thể đổi điểm!")
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có hoặc không hợp lệ.")
                print(f"Điểm hiện tại của khách: {card.points}")
                print(f"Số điểm sau giao dịch: {card.points}")
                
        elif choice == "5":
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            
            try:
                new_value = int(input("Nhập tỷ giá mới cho 1 điểm: ").strip())
                if new_value <= 0:
                    print(" Tỷ giá quy đổi điểm phải lớn hơn 0!")
                    continue
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")
                continue
                
            # Gọi Class Method để cập nhật đồng loạt giá trị của toàn Class
            MemberCard.update_point_value(new_value)
            print("\nCập nhật tỷ giá thành công!")
            print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break
        else:
            print("❌ Chức năng không hợp lệ! Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()