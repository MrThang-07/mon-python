

# PHẦN 1: PHÂN TÍCH GIẢI PHÁP 
# 1. Cơ chế đóng gói và Name Mangling (__password, __plan)
# Trong Python, khi ta đặt dấu gạch dưới kép __ vào trước tên một thuộc tính đối tượng, cơ chế Name Mangling sẽ lập tức kích hoạt. Python sẽ âm thầm đổi tên thuộc tính đó trong bộ nhớ thành dạng _ClassName__attribute_name (Ví dụ: _NetflixAccount__password).

# Điều này giúp ngăn chặn hoàn toàn các đoạn code bên ngoài lỡ tay gán đè dữ liệu theo kiểu account.password = "123" hoặc hack gói cước account.plan = "Premium". Việc thay đổi hay đọc dữ liệu bắt buộc phải đi qua các "cửa khẩu" do ta thiết kế sẵn là hàm Getter/Setter và phương thức nghiệp vụ.

# 2. Sự ảnh hưởng của Class Method đến các Instance hiện có
# Class Method nhận tham số đầu tiên là cls (đại diện cho bản thân cái Class NetflixAccount tổng), chứ không phải self (đối tượng cá nhân).

# Khi ta gọi Class Method để thay đổi một Class Attribute như max_profiles, giá trị này được cập nhật ngay tại vùng nhớ gốc dùng chung của Class. Vì tất cả các tài khoản (Instance) hiện có trên hệ thống đều đang tham chiếu chung về vùng nhớ gốc này để kiểm tra giới hạn, nên một khi Class Method ra lệnh thay đổi, tất cả các tài khoản đang chạy hay vừa mới tạo đều lập tức bị áp dụng chính sách mới ngay trong tích tắc mà không cần phải duyệt vòng lặp để cập nhật từng tài khoản đơn lẻ.
# Phần 2 : Viết code 
class NetflixAccount:
    # Class Attributes - Thuộc tính dùng chung cho toàn hệ thống toàn cầu
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email, password):
        self.email = email
        self.profiles = []
        
        # Sử dụng Name Mangling (__) để bảo mật tuyệt đối bên trong bộ nhớ
        self.__plan = "Basic"
        self.__password = ""
        
        # Kích hoạt setter kiểm duyệt mật khẩu ngay khi khởi tạo
        self.password = password

    # =========================================================================
    # GETTERS & SETTERS (PROPERTIES)
    # =========================================================================

    @property
    def password(self):
        """
        @property (Getter): Biến phương thức thành một thuộc tính chỉ đọc.
        Mục đích: Che giấu mật khẩu thật, luôn trả về chuỗi ẩn danh '********'.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        @<attribute>.setter: Tạo màng lọc dữ liệu khi có hành vi ghi/sửa đổi.
        Mục đích: Chặn mật khẩu yếu, ném ra lỗi ValueError nếu ngắn hơn 6 ký tự.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short (Must be >= 6 characters)")
        self.__password = new_password

    @property
    def plan(self):
        """
        @property (Getter): Tạo thuộc tính chỉ cho phép ĐỌC (Read-only).
        Mục đích: Vì không định nghĩa setter nên bên ngoài không thể hack sửa gói cước.
        """
        return self.__plan

    # =========================================================================
    # CLASS & STATIC METHODS
    # =========================================================================

    @staticmethod
    def validate_email(email):
        """
        @staticmethod: Phương thức tĩnh độc lập, không sờ vào self hay cls.
        Mục đích: Làm hàm tiện ích kiểm tra cú pháp email hợp lệ (có '@' và '.').
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        @classmethod: Phương thức cấp lớp, nhận tham số 'cls' để quản lý cấu hình chung.
        Mục đích: Cập nhật giới hạn số lượng profile đồng loạt áp dụng toàn cầu.
        """
        if new_limit <= 0:
            print("Giới hạn profile phải lớn hơn 0!")
        else:
            cls.max_profiles = new_limit
            print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}")

    # =========================================================================
    # INSTANCE METHODS
    # =========================================================================

    def add_profile(self, profile_name):
        """Phương thức đối tượng: Kiểm tra giới hạn của Class trước khi thêm người xem."""
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(f"Không thể thêm! Đã đạt giới hạn số lượng Profile ({NetflixAccount.max_profiles}) trên tài khoản này.")
            return False
        
        self.profiles.append(profile_name.title())
        print(f" Đã thêm người xem: {profile_name.title()} thành công.")
        return True

    def upgrade_plan(self, new_plan):
        """Phương thức đối tượng: Con đường chính thống duy nhất để cập nhật gói cước ẩn."""
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan not in valid_plans:
            print(f"Gói cước không hợp lệ! Chỉ chấp nhận: {', '.join(valid_plans)}")
            return False
        
        self.__plan = new_plan
        print(f" Nâng cấp thành công! Gói cước hiện tại của bạn là: {self.__plan}")
        return True

    def display_info(self):
        """Phương thức đối tượng: Kết xuất báo cáo thông tin tài khoản ra màn hình CLI."""
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email tài khoản: {self.email}")
        print(f"Mật khẩu: {self.password}")  # Gọi qua property getter để lấy dạng ẩn danh
        print(f"Gói dịch vụ: {self.plan}")     # Gọi qua property getter
        print(f"Danh sách Profile ({len(self.profiles)}/{NetflixAccount.max_profiles}):")
        if not self.profiles:
            print("   (Trống - Chưa có người xem nào)")
        else:
            for idx, profile in enumerate(self.profiles, 1):
                print(f"   {idx}. {profile}")


# =========================================================================
# LUỒNG ĐIỀU PHỐI CHƯƠNG TRÌNH CHÍNH (MAIN APPLICATION INTERFACE)
# =========================================================================

def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        print("===================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
            email = input("Nhập email đăng ký: ").strip()
            
            # Bẫy lỗi 1: Gọi Static Method kiểm tra định dạng email
            if not NetflixAccount.validate_email(email):
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                continue
                
            password = input("Nhập mật khẩu (tối thiểu 6 ký tự): ").strip()
            
            try:
                # Bẫy lỗi 2: Khởi tạo đối tượng để kích hoạt kiểm tra độ dài mật khẩu ở setter
                current_account = NetflixAccount(email, password)
                print(" Đăng ký tài khoản Netflix thành công!")
            except ValueError as error_message:
                print(f"Lỗi bảo mật mật khẩu: {error_message}")
                current_account = None # Đảm bảo reset trạng thái nếu lỗi
                
        elif choice in ["2", "3", "4"]:
            # Bẫy lỗi 4: Chặn thao tác khi hệ thống chưa được đăng ký đối tượng
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                continue
                
            if choice == "2":
                print("\n--- THÔNG TIN TÀI KHOẢN ---")
                current_account.display_info()
                
            elif choice == "3":
                print("\n--- THÊM NGƯỜI XEM (ADD PROFILE) ---")
                profile_name = input("Nhập tên người xem mới: ").strip()
                if not profile_name:
                    print(" Tên người xem không được để trống!")
                else:
                    current_account.add_profile(profile_name)
                    
            elif choice == "4":
                print("\n--- NÂNGCẤP GÓI CƯỚC ---")
                print("Các gói dịch vụ hiện có: Basic | Standard | Premium")
                new_plan = input("Nhập tên gói cước muốn đổi: ").strip().title()
                current_account.upgrade_plan(new_plan)
                
        elif choice == "5":
            print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX (ADMIN ONLY) ---")
            print(f"Giới hạn Profile toàn cầu hiện tại: {NetflixAccount.max_profiles}")
            try:
                new_limit = int(input("Nhập số lượng Profile tối đa mới: ").strip())
                # Gọi Class Method trực tiếp qua tên Class tổng để cập nhật cấu hình
                NetflixAccount.update_max_profiles(new_limit)
            except ValueError:
                print(" Vui lòng nhập vào một số nguyên hợp lệ!")
                
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng Netflix Account Manager!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 6.")

if __name__ == "__main__":
    main()