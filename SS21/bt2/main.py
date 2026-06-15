import logging
from pos_logic import view_menu, add_to_order, calculate_total, ItemNotFoundError, InvalidQuantityError

# Cấu hình logging chỉ hiện trên màn hình Console (Terminal)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    current_order = [] # Giỏ hàng ban đầu trống rỗng
    
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            view_menu()
            
        elif choice == "2":
            print("\n--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ").strip().upper() # Tự động xóa khoảng trắng và in hoa
            
            # Bẫy lỗi 1: Nhập chữ thay vì số
            try:
                quantity_input = input("Nhập số lượng: ").strip()
                quantity = int(quantity_input)
            except ValueError:
                print("Vui lòng nhập số lượng là một số nguyên!")
                logging.error("ValueError - Invalid quantity input")
                continue
                
            # Bẫy lỗi 2 và 3: Gọi hàm nghiệp vụ và bắt các Custom Exception
            try:
                drink_name = add_to_order(current_order, drink_code, quantity)
                print(f"Đã thêm {quantity} x {drink_name} vào giỏ hàng.")
            except ItemNotFoundError:
                print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
            except InvalidQuantityError:
                print("Số lượng phải lớn hơn 0!")
                
        elif choice == "3":
            if len(current_order) == 0:
                print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                continue
                
            print("\n--- GIỎ HÀNG HIỆN TẠI ---")
            print(f"{'Mã SP':<5} | {'Tên đồ uống':<18} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
            print("-" * 65)
            for item in current_order:
                subtotal = item["price"] * item["quantity"]
                print(f"{item['drink_code']:<5} | {item['name']:<18} | {item['price']:,} | {item['quantity']:<8} | {subtotal:,} VNĐ")
            print("-" * 65)
            
            total = calculate_total(current_order)
            print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
            
        elif choice == "4":
            if len(current_order) == 0:
                print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                continue
                
            total = calculate_total(current_order)
            print("\n--- THANH TOÁN ---")
            print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
            confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()
            
            if confirm == 'y':
                print("Thanh toán thành công.")
                logging.info("Checkout successful")
                print("Giỏ hàng đã được làm trống.")
                current_order.clear() # Xóa sạch giỏ hàng
            elif confirm == 'n':
                print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
            else:
                print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
                
        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn sai, vui lòng nhập số từ 1 đến 5!")

if __name__ == "__main__":
    main()