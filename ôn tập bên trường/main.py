from manager import ProductManager
from product import Product

def main():
    manager = ProductManager()
    
    # Ghi cứng dữ liệu (Hardcode)
    manager.products = [
        Product("SP001", "Laptop Dell", 15000000, 3, 2000000),
        Product("SP002", "Chuột Logitech", 350000, 20, 500000),
        Product("SP004", "Màn hình Samsung", 4500000, 5, 0)
    ]

    while True:
        print("\n=== MENU ===")
        print("1.Hiện | 2.Thêm | 3.Sửa | 4.Xóa | 5.Tìm | 6.Thống kê | 7.Thoát")
        choice = input("Chọn: ")
        
        # Dùng match case cực gọn thay cho if-elif
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
                print("Cảm ơn đã sử dụng!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()