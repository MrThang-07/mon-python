class InventoryItem:
    def __init__(self,id,name,category,quantity,unit_price,storage_fee):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.storage_fee = storage_fee
        self.total_inventory_value = 0.0
        self.inventory_type = ""
        self.update_value_type()
    def calculate_inventory_value(self):
        self.total_inventory_value = (self.quantity * self.unit_price) + self.storage_fee
    def classify_inventory(self):
        if self.total_inventory_value < 5000000:
            self.inventory_type = "Thấp"
        elif self.total_inventory_value < 20000000:
            self.inventory_type = "Trung bình"
        elif self.total_inventory_value < 50000000:
            self.inventory_type = "Cao"
        else:
            self.inventory_type = "Rất cao"
    def update_value_type(self):
        self.calculate_inventory_value()
        self.classify_inventory()

class InventoryManager:
    def __init__(self):
        self.items = []
    def validate_quantity(self,prompt,min_input,max_input):
        while True:
            try:
                result = int(input(prompt).strip())
                if min_input <= result <= max_input:
                    return result
                else:
                    print(f"Vui lòng nhập từ {min_input} - {max_input}")
            except ValueError:
                print("Lỗi kiểu dữ liệu , phải là số nguyên !")
    def validate_price_fee(self,prompt):
        while True:
            try:
                result = int(input(prompt).strip())
                if result < 0:
                    print("Vui lònh nhập số lớn hơn hoặc bằng 0 !")
                    continue
                else:
                    return result
            except ValueError:
                print("Lỗi kiểu dữ liệu , phải là số nguyên !")
    def show_all(self):
        if not self.items:
            print("Danh sách hàng hóa đang rỗng!")
            return
        print(f"{'Mã hàng hóa':<15}| {'Tên hàng hóa':<15}| {'Danh mục':<15}| {'Số lượng tồn kho':<25}| {'Đơn giá nhập':<15}| {'Chi phí lưu kho':<20}| {'Tổng giá trị tồn kho':<25}| {'Phân loại tồn kho':<25}|")
        for i in self.items:
            print("-"*160)
            print(f"{i.id:<15}| {i.name:<15}| {i.category:<15}| {i.quantity:<25}| {i.unit_price:<15}| {i.storage_fee:<20}| {i.total_inventory_value:<25}| {i.inventory_type:<25}|")
    def add_item(self):
        input_id = input("Nhập mã hàng hóa : ").strip().upper()
        if not input_id:
            print("Mã bị rỗng !")
            return
        for i in self.items:
            if input_id == i.id:
                print("Mã đã bị trùng!")
        input_name = input("Nhập tên hàng hóa : ").strip().title()
        if not input_name:
            print("Tên bị rỗng !")
            return
        input_category = input("Nhập danh mục hàng hóa : ").strip().upper()
        if not input_category:
            print("Danh mục bị rỗng !")
            return
        quantity = self.validate_quantity("Nhập số lượng tồn kho :",0,1000000)
        unit_price = self.validate_price_fee("Nhập đơn giá : ")
        storage_fee = self.validate_price_fee("Nhập chi phí kho  : ")
        new_item = InventoryItem(input_id,input_name,input_category,quantity,unit_price,storage_fee)
        self.items.append(new_item)
        print("Đã thêm mới thành công!")
    def update_item(self):
        input_id = input("Nhập mã hàng hóa cần cập nhật : ").strip().upper()
        for i in self.items:
            if input_id == i.id:
                i.quantity = self.validate_quantity("Nhập số lượng tồn kho :",0,1000000)
                i.unit_price = self.validate_price_fee("Nhập đơn giá : ")
                i.storage_fee = self.validate_price_fee("Nhập chi phí kho  : ")
                i.update_value_type()
                print("Đã cập nhật thành công!")
                return
        print("Không tìm thấy hàng hóa cần cập nhật !")
    def delete_item(self):
        input_id = input("Nhập mã hàng hóa cần xóa : ").strip().upper()
        for i in self.items:
            if input_id == i.id:
                choice = input("Bạn có chắc muốn xóa hàng hóa này không (Y/N) :").strip().upper()
                if choice == "Y":
                    self.items.remove(i)
                    print("Đã xóa thành công")
                    return
                elif choice == "N":
                    print("Đã hủy thao tác")
                    return
                else:
                    print("Lựa chọn không hợp lệ!")
                    return
        print("Không tìm thấy hàng hóa cần xóa !")
    def search_item(self):
        search_list = []
        input_choice = input("Nhập 1(tìm kiếm theo tên) hoặc nhập 2(tìm kiếm theo danh mục) : ").strip()
        if input_choice == "1":
            search_name = input("Nhập tên hàng hóa cần tìm kiếm : ").strip().upper()
            for i in self.items:
                if search_name in i.name.upper():
                    search_list.append(i)
            if not search_list:
                print("Hiện không thấy hàng hóa nào!")
                return
            else:
                print(f"{'Mã hàng hóa':<15}| {'Tên hàng hóa':<15}| {'Danh mục':<15}| {'Số lượng tồn kho':<25}| {'Đơn giá nhập':<15}| {'Chi phí lưu kho':<20}| {'Tổng giá trị tồn kho':<25}| {'Phân loại tồn kho':<25}|")
                for i in search_list:
                    print("-"*160)
                    print(f"{i.id:<15}| {i.name:<15}| {i.category:<15}| {i.quantity:<25}| {i.unit_price:<15}| {i.storage_fee:<20}| {i.total_inventory_value:<25}| {i.inventory_type:<25}|")

        elif input_choice == "2":
            search_category = input("Nhập tên hàng hóa cần tìm kiếm : ").strip().upper()
            for i in self.items:
                if search_category in i.category.upper():
                    search_list.append(i)
            if not search_list:
                print("Hiện không thấy hàng hóa nào!")
                return
            else:
                print(f"{'Mã hàng hóa':<15}| {'Tên hàng hóa':<15}| {'Danh mục':<15}| {'Số lượng tồn kho':<25}| {'Đơn giá nhập':<15}| {'Chi phí lưu kho':<20}| {'Tổng giá trị tồn kho':<25}| {'Phân loại tồn kho':<25}|")
                for i in search_list:
                    print("-"*160)
                    print(f"{i.id:<15}| {i.name:<15}| {i.category:<15}| {i.quantity:<25}| {i.unit_price:<15}| {i.storage_fee:<20}| {i.total_inventory_value:<25}| {i.inventory_type:<25}|")
        else:
            print("Vui lòng chọn 1 hoặc 2!")
            return
    
def main():
    manager = InventoryManager()
    while True:
        print("""==================MENU===================
    1. Hiển thị danh sách hàng hóa
    2. Thêm hàng hóa mới
    3. Cập nhật hàng hóa
    4. Xóa hàng hóa
    5. Tìm kiếm hàng hóa
    6. Thoát
    ======================================""")
        choice = input("Nhập lựa chọn của bạn : ").strip()
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_item()
            case "3":
                manager.update_item()
            case "4":
                manager.delete_item()
            case "5":
                manager.search_item()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                return
            case _:
                print("Vui lòng nhập từ 1 - 6 !")
            
if __name__ == "__main__":
    main()

        