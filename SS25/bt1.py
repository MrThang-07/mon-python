# (1)
# 1. Thành phần cấu trúc Class BankAccount
# Thuộc tính Lớp (Class Attributes): bank_name và transaction_fee. Đây là các thông tin chung áp dụng đồng bộ cho toàn bộ hệ thống Vietcombank.

# Thuộc tính Đối tượng (Instance Attributes): account_number (mã công khai) và thuộc tính ẩn danh bảo mật cao __balance (áp dụng kỹ thuật Name Mangling để chống can thiệp số dư bừa bãi).

# Cơ chế Đóng gói (Encapsulation):

# Dùng @property cho balance để biến nó thành một thuộc tính chỉ cho phép ĐỌC dữ liệu số dư, hoàn toàn không định nghĩa hàm setter để chặn đứng mọi hành vi sửa đổi tiền trực tiếp từ ngoài rìa.

# Dùng bộ đôi @property và @account_name.setter để chuẩn hóa dữ liệu tên (xóa khoảng trắng thừa, viết hoa toàn bộ) và lọc lỗi chuỗi rỗng trước khi nạp dữ liệu vào vùng nhớ của đối tượng.

# 2. Phân loại và lý do sử dụng các Phương thức đặc biệt
# Tại sao validate_account_number dùng @staticmethod?

# Hàm này nhận vào một chuỗi độc lập và kiểm tra xem nó có đúng 10 chữ số hay không. Logic kiểm tra này hoàn toàn không sờ vào dữ liệu riêng của một chiếc thẻ nào (self), cũng không cần thay đổi cấu hình chung của Class (cls). Do đó, nó được thiết kế làm một hàm tiện ích tĩnh để có thể gọi kiểm tra ngay từ ngoài cửa trước khi tiến hành khởi tạo đối tượng tài khoản.

# Tại sao update_transaction_fee dùng @classmethod?

# Phí giao dịch là tài sản dùng chung của toàn hệ thống (Class Attribute). Khi có quyết định thay đổi phí, ta cần tác động trực tiếp vào bộ não tổng của Class thông qua tham số cls để toàn bộ các tài khoản hiện tại và tương lai đều được áp dụng mức phí mới đồng loạt, thay vì đi sửa từng tài khoản đơn lẻ.
# (2) Viết code 
class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__balance = 0  
        self._account_name = ""
        
        cleaned_name = account_name.strip().upper()
        if cleaned_name:
            self._account_name = cleaned_name

    # =========================================================================
    # DECORATORS - CÁC BỘ ĐIỀU HƯỚNG VÀ ĐÓNG GÓI OOP
    # =========================================================================

    @property
    def balance(self):
        # @property: Biến một phương thức thành thuộc tính chỉ cho phép ĐỌC (Getter).
        # Giúp bảo mật số dư tài khoản, chặn đứng việc sửa đổi dữ liệu từ bên ngoài.
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, name):
        # @<attribute>.setter: Thiết lập màng lọc dữ liệu khi có hành vi GHI hoặc sửa đổi.
        # Tự động loại bỏ khoảng trắng dư thừa và đưa chuỗi về dạng IN HOA chuẩn chỉnh.
        cleaned_name = name.strip().upper()
        if not cleaned_name:
            print("Tên tài khoản không được để trống")
        else:
            self._account_name = cleaned_name

    @staticmethod
    def validate_account_number(account_number):
        # @staticmethod: Định nghĩa phương thức tĩnh độc lập (Utility Method).
        # Không liên kết với self hay cls, dùng để check định dạng chuỗi đầu vào.
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        # @classmethod: Định nghĩa phương thức lớp, nhận tham số 'cls' đại diện cho Class.
        # Dùng để thay đổi các thuộc tính cấu hình dùng chung của toàn hệ thống ngân hàng.
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là {cls.transaction_fee:,} VND")
        else:
            cls.transaction_fee = new_fee
            print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND")

    # =========================================================================
    # INSTANCE METHODS - CÁC PHƯƠNG THỨC NGHIỆP VỤ ĐỐI TƯỢNG
    # =========================================================================

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        
        total_deduction = amount + BankAccount.transaction_fee
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False
            
        self.__balance -= total_deduction
        return True

    def display_info(self):
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


# =========================================================================
# LUỒNG ĐIỀU PHỐI CHƯƠNG TRÌNH CHÍNH (MAIN INTERFACE)
# =========================================================================

def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")
            while True:
                account_number = input("Nhập số tài khoản 10 chữ số: ").strip()
                # Gọi Static Method kiểm tra trực tiếp qua tên lớp BankAccount
                if BankAccount.validate_account_number(account_number):
                    break
                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")
            
            account_name = input("Nhập tên chủ tài khoản: ").strip()
            if not account_name:
                print("Tên tài khoản không được để trống")
                continue
                
            current_account = BankAccount(account_number, account_name)
            print("Mở tài khoản thành công!")
            print(f"Số tài khoản: {current_account.account_number}")
            print(f"Tên chủ tài khoản: {current_account.account_name}")
            
        elif choice in ["2", "3", "4"]:
            # Bẫy dữ liệu: Chặn người dùng thao tác khi chưa tạo tài khoản đối tượng
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                continue
                
            if choice == "2":
                print("\n--- THÔNG TIN TÀI KHOẢN ---")
                current_account.display_info()
                
            elif choice == "3":
                print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                type_choice = input("Chọn loại giao dịch (1-2): ").strip()
                
                if type_choice not in ["1", "2"]:
                    print("Lựa chọn loại giao dịch không hợp lệ.")
                    continue
                    
                try:
                    amount = int(input("Nhập số tiền giao dịch: ").strip())
                except ValueError:
                    print("Vui lòng nhập một con số nguyên hợp lệ!")
                    continue
                    
                if type_choice == "1":
                    if current_account.deposit(amount):
                        print(f"Nạp tiền thành công: +{amount:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")
                elif type_choice == "2":
                    if current_account.withdraw(amount):
                        print(f"Rút tiền thành công: -{amount:,} VND")
                        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
                    print(f"Số dư mới: {current_account.balance:,} VND")
                    
            elif choice == "4":
                print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                new_name = input("Nhập tên mới: ").strip()
                if not new_name:
                    print("Tên tài khoản không được để trống")
                else:
                    # Gán giá trị thông qua hàm setter để kích hoạt bộ chuẩn hóa tự động
                    current_account.account_name = new_name
                    print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")
                    
        elif choice == "5":
            print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            try:
                new_fee = int(input("Nhập phí giao dịch mới: ").strip())
            except ValueError:
                print("Vui lòng nhập một con số nguyên hợp lệ!")
                continue
            # Gọi Class Method trực tiếp từ tên lớp để cập nhật đồng loạt cấu hình hệ thống
            BankAccount.update_transaction_fee(new_fee)
            
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break
        else:
            print("Chức năng không hợp lệ! Vui lòng nhập số từ 1 đến 6.")

if __name__ == "__main__":
    main()