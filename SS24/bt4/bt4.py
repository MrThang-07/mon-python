# (1) Phân tích 

# 1. Thuộc tính Lớp (Class Attributes)
# service_charge: Biến dạng số thực (float), dùng chung cho toàn bộ các món trong thực đơn để quản lý tỷ lệ phụ phí dịch vụ toàn chuỗi (mặc định ban đầu là 0.0).

# 2. Thuộc tính Đối tượng (Instance Attributes)
# item_id: Chuỗi ký tự (str) - Mã món ăn/đồ uống (Public).

# item_name: Chuỗi ký tự (str) - Tên món ăn/đồ uống (Public).

# __base_price: Số nguyên (int) - Giá gốc ban đầu của món (Private - Bảo mật bằng Name Mangling).

# __is_available: Giá trị logic (bool) - Trạng thái còn hàng (True) hoặc hết hàng (False) (Private - Bảo mật bằng Name Mangling).

# 3. Phân loại các Phương thức (Methods Breakdown)
# Phương thức khởi tạo (__init__): Nhận vào item_id, item_name, và base_price. Tự động định danh trạng thái mặc định __is_available = True (Đang bán) khi món mới được khai sinh.

# Getters / Setters:

# @property và @base_price.setter cho thuộc tính __base_price: Màng lọc tại setter đảm bảo giá tiền nhập vào bắt buộc phải là số nguyên và lớn hơn 0. Nếu vi phạm sẽ từ chối cập nhật.

# @property cho thuộc tính __is_available: Giúp hệ thống đọc được trạng thái từ bên ngoài mà không cho phép dùng dấu bằng để gán đè bừa bãi.

# Instance Methods (Phương thức đối tượng):

# toggle_availability(self): Không nhận tham số ngoài. Thực hiện đảo trạng thái bán (True thành False hoặc ngược lại) và trả về trạng thái mới.

# calculate_selling_price(self): Không nhận tham số ngoài. Áp dụng công thức tính toán và trả về Giá niêm yết cuối cùng sau khi cộng phụ phí dịch vụ của lớp.

# Class Methods (Phương thức lớp):

# update_service_charge(cls, new_rate): Nhận tham số cls và giá trị phần trăm phụ phí mới để cập nhật đồng bộ cho toàn bộ hệ thống.

# Static Methods (Phương thức tĩnh):

# is_valid_item_id(item_code): Hàm tiện ích độc lập, nhận vào một chuỗi mã món để kiểm định chất lượng định dạng (2 chữ cái in hoa + 2 chữ số) trước khi cho phép tạo đối tượng.
# (2) Viết code 
class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__is_available = True         
        self.__base_price = 1000
        self.base_price = base_price

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
        else:
            self.__base_price = new_price

    @property
    def is_available(self):
        return self.__is_available

    @staticmethod
    def is_valid_item_id(item_code):
        if len(item_code) != 4:
            return False
        if not item_code[:2].isalpha() or not item_code[:2].isupper():
            return False
        if not item_code[2:].isdigit():
            return False
        return True

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    def toggle_availability(self):
        self.__is_available = not self.__is_available
        return "ĐANG BÁN" if self.__is_available else "HẾT HÀNG"

    def calculate_selling_price(self):
        final_price = self.__base_price + (self.__base_price * MenuItem.service_charge)
        return int(final_price)


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]

def find_item_by_id(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
        print("1. Xem thực đơn & Giá niêm yết")
        print("2. Thêm món mới vào menu")
        print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
        print("4. Điều chỉnh giá gốc của món")
        print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
            if not menu_db:
                print("Thực đơn hiện tại đang trống!")
            else:
                for idx, item in enumerate(menu_db, 1):
                    status_text = "Đang bán" if item.is_available else "Hết hàng"
                    selling_price = item.calculate_selling_price()
                    print(f"{idx}. Mã: {item.item_id} | Tên: {item.item_name:<15} | Trạng thái: {status_text:<9} | Giá niêm yết: {selling_price:,} VNĐ")
                    
        elif choice == "2":
            print("\n--- THÊM MÓN MỚI VÀO MENU ---")
            item_id = input("Nhập mã món: ").strip()
            
            if not MenuItem.is_valid_item_id(item_id):
                print("\nMã món không hợp lệ!")
                print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
                continue
                
            if find_item_by_id(item_id) is not None:
                print(f"\nLỗi: Mã món '{item_id}' đã tồn tại trong thực đơn!")
                continue
                
            item_name = input("Nhập tên món: ").strip()
            if not item_name:
                print("Lỗi: Tên món không được bỏ trống.")
                continue
                
            try:
                base_price = int(input("Nhập giá gốc: ").strip())
                if base_price <= 0:
                    print(" Lỗi: Giá gốc ban đầu của món phải lớn hơn 0.")
                    continue
            except ValueError:
                print(" Lỗi: Vui lòng nhập số nguyên hợp lệ cho giá tiền.")
                continue
                
            new_item = MenuItem(item_id, item_name, base_price)
            menu_db.append(new_item)
            print("\nThêm món mới thành công!")
            
        elif choice == "3":
            print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
            item_id = input("Nhập mã món cần cập nhật: ").strip()
            item = find_item_by_id(item_id)
            
            if item is None:
                print(" Không tìm thấy mã món này trong hệ thống!")
                continue
                
            new_status = item.toggle_availability()
            print(f">> Đã cập nhật {item.item_name} thành {new_status}!")
            
        elif choice == "4":
            print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
            item_id = input("Nhập mã món cần đổi giá: ").strip()
            item = find_item_by_id(item_id)
            
            if item is None:
                print("Không tìm thấy mã món này trong hệ thống!")
                continue
                
            try:
                new_price = int(input("Nhập giá tiền mới: ").strip())
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
                continue
                
            old_price = item.base_price
            item.base_price = new_price
            
            if item.base_price == new_price and new_price != old_price:
                print("Cập nhật giá gốc thành công!")
                
        elif choice == "5":
            print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
            current_percentage = int(MenuItem.service_charge * 100)
            print(f"Phụ phí hiện tại: {current_percentage}%")
            
            try:
                rate_input = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: ").strip())
                if rate_input < 0.0:
                    print("Mức phụ phí dịch vụ không được phép âm!")
                    continue
            except ValueError:
                print("Vui lòng nhập một số thập phân hợp lệ!")
                continue
                
            MenuItem.update_service_charge(rate_input)
            print("Cập nhật phụ phí dịch vụ thành công!")
            
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()