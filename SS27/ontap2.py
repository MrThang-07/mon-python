class Product:
    def __init__(self,id,name,import_price,quantity,storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = 0.0
        self.stock_status = ""
        self.update_value_status()
    def calculate_total_value(self):
       self.total_value = (self.import_price * self.quantity) +  self.storage_fee
    def classify_stock_status(self):
        if self.total_value < 9000000:
            self.stock_status = "Thấp (An toàn)"
        elif self.total_value < 15000000:
            self.stock_status = "Trung bình"
        elif self.total_value < 30000000:
            self.stock_status = "Cao (Cần chú ý)"
        else:
            self.stock_status = "Rất cao (Rủi ro ứ đọng vốn)"
    def update_value_status(self):
        self.calculate_total_value()
        self.classify_stock_status()
class ProductManager:
    def __init__(self):
        self.products = []
    def validate_number(self,prompt,min_input,max_input):
        while True:
            try:
                input_in = int(input(prompt.strip()))
                if input_in < min_input:
                    print("Vui lòng nhập lớn hơn 0!")
                    continue
                if min_input <= input_in <= max_input:
                    return input_in
                else:
                    print("Vui lòng nhập từ 0 - 1000:")
                    continue
            except ValueError:
                print("nhập sai kiểu dữ liệu !")
    def show_all(self):
        if not self.products:
            print("Danh sách bị rỗng .")
        else:
            print(f"{'Mã SP':<10}| {'Tên sản phẩm':<20}| {'Giá nhập':<15}| {'Số lượng':<15}| {'Chi phí kho':<20}| {' Tổng giá trị':<20}| {'Trạng thái tồn':<20}|")
            for item in self.products:
                print("-"*38)
                print(f"{item.id:<10}| {item.name:<20}| {item.import_price:<15}| {item.quantity:<15}| {item.storage_fee:<20}| {item.total_value:<20}| {item.stock_status:<20}|")
    def add_product(self):
        input_id = input("Nhập mã sp thêm mới : ").strip().upper()
        if not input_id:
            print("Mã sp bị rỗng !")
            return
        for item in self.products:
            if input_id == item.id:
                print("Mã sp bị trùng!")
                return
        input_name = input("Nhập tên sản phẩm : ").strip().title()
        if not input_name:
            print("Tên sp bị rỗng !")
            return
        input_import_price = self.validate_number("Nhập giá tiền sản phẩm : ",1,10000000000)
        input_quantity = self.validate_number("Nhập số lượng sản phẩm :",0,1000)
        input_storage_fee = self.validate_number("Nhập chi phí lưu kho phát sinh:",1,10000000)
        new_sp = Product(input_id,input_name,input_import_price,input_quantity,input_storage_fee)
        self.products.append(new_sp)
        print("Đã thêm thành công .")
    def update_product(self):
        input_id = input("Nhập mã sp cần cập nhật : ").strip().upper()
        for item in self.products:
            if input_id == item.id:
                item.import_price = self.validate_number("Nhập giá tiền sản phẩm : ",1,10000000000)
                item.quantity = self.validate_number("Nhập số lượng sản phẩm :",0,1000)
                item.storage_fee = self.validate_number("Nhập chi phí lưu kho phát sinh:",1,10000000)
                item.update_value_status()
                print("Đã cập nhật thành công ")
                return
        print("Không tìm thấy mã sp cần cập nhật !")
    def delete_product(self):
        input_id = input("Nhập mã sp cần xóa : ").strip().upper()
        for item in self.products:
            if input_id == item.id:
                choice = input("Bạn có chắc muốn xóa sản phẩm này khỏi hệ thống không? (Y/N): ").strip().upper()
                if choice == "Y":
                    self.products.remove(item)
                    print("Đã xóa thành công")
                    return
                return
        print("Không tìm thấy mã sp cần xóa !")
    def search_product(self):
        share_list = []
        input_name = input("Nhập tên sp cần tìm kiếm : ").strip().upper()
        for item in self.products:
            if input_name in item.name.upper():
                share_list.append(item)
        if not share_list:
            print("Không tìm thấy tên sp cần tìm kiếm !")
            return
        else:
            for item in share_list:
                print("-"*38)
                print(f"{item.id:<10}| {item.name:<20}| {item.import_price:<15}| {item.quantity:<15}| {item.storage_fee:<20}| {item.total_value:<20}| {item.stock_status:<20}|")

def main():
    manager = ProductManager()
    while True:
        print("""================ MENU ================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
=====================================

""")
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match (choice):
            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "4":
                manager.delete_product()
            case "5":
                manager.search_product()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                return
            case _:
                print("Vui lòng nhập lựa chọn từ 1 - 6 !")
        
if __name__ == "__main__":
    main()
