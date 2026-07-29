# ==========================================
# 1. CLASS PRODUCT (ĐỐI TƯỢNG SẢN PHẨM)
# ==========================================
class Product:
    def __init__(self, p_id, name, price, quantity, discount):
        self.id = p_id
        self.name = name
        self.price = float(price)
        self.quantity_sold = int(quantity)
        self.discount = float(discount)
        
        # Thuộc tính tự động tính toán (Đóng gói)
        self.total_revenue = 0
        self.revenue_type = ""
        
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        rev = (self.price * self.quantity_sold) - self.discount
        self.total_revenue = rev if rev > 0 else 0

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"

# ==========================================
# 2. CLASS PRODUCT MANAGER (QUẢN LÝ DANH SÁCH)
# ==========================================
class ProductManager:
    def __init__(self):
        self.products = []

    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm đang rỗng!")
            return
        print("\n--- DANH SÁCH SẢN PHẨM ---")
        for p in self.products:
            print(f"Mã: {p.id} | Tên: {p.name} | Giá: {p.price} | SL: {p.quantity_sold} | Giảm: {p.discount} | DT: {p.total_revenue} | Loại: {p.revenue_type}")

    def add_product(self):
        print("\n--- THÊM SẢN PHẨM MỚI ---")
        p_id = input("Nhập mã SP: ").strip()
        if not p_id:
            print("Lỗi: Mã sản phẩm không được để trống!")
            return
        
        for p in self.products:
            if p.id == p_id:
                print("Lỗi: Mã sản phẩm bị trùng!")
                return
                
        name = input("Nhập tên SP: ").strip()
        if not name:
            print("Lỗi: Tên sản phẩm không được để trống!")
            return
        
        try:
            price = float(input("Nhập giá bán: "))
            if price < 0:
                print("Lỗi: Giá bán phải lớn hơn hoặc bằng 0!")
                return
                
            qty = int(input("Nhập số lượng đã bán (0 - 10000): "))
            if qty < 0 or qty > 10000:
                print("Lỗi: Số lượng bán phải từ 0 đến 10,000!")
                return
                
            disc = float(input("Nhập giảm giá: "))
            if disc < 0:
                print("Lỗi: Giảm giá phải lớn hơn hoặc bằng 0!")
                return
                
            self.products.append(Product(p_id, name, price, qty, disc))
            print("Thêm sản phẩm thành công!")
            
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng số cho Giá, Số lượng và Giảm giá!")

    def update_product(self):
        p_id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
        for p in self.products:
            if p.id == p_id:
                try:
                    price = float(input("Nhập giá mới: "))
                    if price < 0:
                        print("Lỗi: Giá bán phải >= 0!")
                        return
                        
                    qty = int(input("Nhập SL mới (0 - 10000): "))
                    if qty < 0 or qty > 10000:
                        print("Lỗi: Số lượng phải từ 0 đến 10,000!")
                        return
                        
                    disc = float(input("Nhập giảm giá mới: "))
                    if disc < 0:
                        print("Lỗi: Giảm giá phải >= 0!")
                        return
                        
                    p.price = price
                    p.quantity_sold = qty
                    p.discount = disc
                    
                    p.calculate_revenue()
                    p.classify_revenue()
                    print("Cập nhật sản phẩm thành công!")
                    return
                except ValueError:
                    print("Lỗi: Nhập sai kiểu dữ liệu số!")
                    return
                    
        print("Không tìm thấy sản phẩm cần cập nhật!")

    def delete_product(self):
        p_id = input("Nhập mã sản phẩm cần xóa: ").strip()
        for p in self.products:
            if p.id == p_id:
                confirm = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ").strip()
                if confirm.lower() == 'y':
                    self.products.remove(p)
                    print("Xóa sản phẩm thành công!")
                elif confirm.lower() == 'n':
                    print("Đã hủy thao tác xóa!")
                else:
                    print("Lựa chọn không hợp lệ, hủy thao tác xóa!")
                return
        print("Không tìm thấy sản phẩm cần xóa!")

    def search_product(self):
        kw = input("Nhập từ khóa tìm kiếm tên SP: ").strip().lower()
        found = False
        print("\n--- KẾT QUẢ TÌM KIẾM ---")
        for p in self.products:
            if kw in p.name.lower():
                print(f"Mã: {p.id} | Tên: {p.name} | Giá: {p.price} | DT: {p.total_revenue} | Loại: {p.revenue_type}")
                found = True
        if not found:
            print("Không tìm thấy sản phẩm phù hợp!")

    def statistics(self):
        stats = {"Thấp": 0, "Trung bình": 0, "Khá": 0, "Cao": 0}
        for p in self.products:
            if p.revenue_type in stats:
                stats[p.revenue_type] += 1
        print("\n--- THỐNG KÊ SỐ LƯỢNG THEO NHÓM DOANH THU ---")
        for k, v in stats.items():
            print(f"Doanh thu {k}: {v} sản phẩm")

# ==========================================
# 3. HÀM MAIN (GIAO DIỆN ĐIỀU HƯỚNG)
# ==========================================
def main():
    manager = ProductManager()
    
    # Ghi cứng dữ liệu mẫu để test nhanh
    manager.products = [
        Product("SP001", "Laptop Dell", 15000000, 3, 2000000),
        Product("SP002", "Chuột Logitech", 350000, 20, 500000),
        Product("SP004", "Màn hình Samsung", 4500000, 5, 0)
    ]

    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Thống kê doanh thu")
        print("7. Thoát")
        print("======================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
        match choice:
            case '1':
                manager.show_all()
            case '2':
                manager.add_product()
            case '3':
                manager.update_product()
            case '4':
                manager.delete_product()
            case '5':
                manager.search_product()
            case '6':
                manager.statistics()
            case '7':
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()