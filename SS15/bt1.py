# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#  1. Phân định phạm vi biến (Global vs Local)
# Biến toàn cục (Global Variables):

# inventory_stock (Kiểu int): Lưu giữ số lượng sản phẩm hiện tại còn lại trong kho bãi của TechStore.

# total_revenue (Kiểu float): Lưu giữ tổng lũy kế doanh thu thực tế thu được từ các hóa đơn bán hàng thành công.

# Biến cục bộ (Local Variables):

# Các tham số như amount, quantity, price chỉ tồn tại bên trong phạm vi hoạt động của hàm nhận chúng để xử lý tính toán.

# discount, vat, subtotal, final_total trong hàm calculate_final_price() là biến cục bộ, chỉ được sinh ra khi hàm vận hành và tự giải phóng bộ nhớ sau khi hàm hoàn tất lệnh return.
# ̣(2) Viết code 
# Khởi tạo các biến toàn cục lưu trữ trạng thái hệ thống ban đầu
inventory_stock = 100
total_revenue = 0.0

def print_report():
    """
    Hiển thị báo cáo tổng quan về tình hình kinh doanh của TechStore.
    
    Tham số đầu vào: Không có.
    Giá trị trả về: Không có (None).
    """
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu  : ${total_revenue:.1f}")

def add_stock(amount):
    """
    Cập nhật tăng số lượng hàng hóa lưu kho thực tế của cửa hàng.
    
    Tham số đầu vào:
        amount (int): Số lượng sản phẩm muốn nhập thêm vào kho.
    Giá trị trả về: Không có (None).
    """
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False
    return True

def calculate_final_price(quantity, price):
    subtotal = quantity * price
    discount = 0.0
    
    if subtotal >= 1000.0:
        discount = subtotal * 0.1
        
    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat
    
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price:.1f}")
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Giảm giá (10%): ${discount:.1f}")
    print(f"Thuế VAT (8%): ${vat:.1f}")
    print(f"Tổng thanh toán: ${final_total:.1f}")
    
    return final_total

def main():
    global inventory_stock, total_revenue
    
    while True:
        print("""
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================""")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        match choice:
            case "1":
                print("\n--- NHẬP HÀNG ---")
                try:
                    amount_input = int(input("Nhập số lượng sản phẩm muốn thêm: ").strip())
                    if amount_input <= 0:
                        print("[Lỗi]: Dữ liệu nhập vào phải lớn hơn 0.")
                        continue
                    add_stock(amount_input)
                except ValueError:
                    print("[Lỗi]: Vui lòng nhập vào một số nguyên hợp lệ!")
                    
            case "2":
                print("\n--- BÁN HÀNG ---")
                try:
                    qty_input = int(input("Nhập số lượng mua: ").strip())
                    if qty_input <= 0:
                        print("[Lỗi]: Dữ liệu nhập vào phải lớn hơn 0.")
                        continue
                        
                    
                    if not process_sale(qty_input):
                        continue
                        
                    price_input = float(input("Nhập đơn giá ($): ").strip())
                    if price_input <= 0:
                        print("[Lỗi]: Dữ liệu nhập vào phải lớn hơn 0.")
                        continue
                        
                   
                    final_payment = calculate_final_price(qty_input, price_input)
                    
                    
                    inventory_stock -= qty_input
                    total_revenue += final_payment
                    print("Đã bán thành công!")
                    
                except ValueError:
                    print("[Lỗi]: Nhập sai định dạng kiểu dữ liệu số!")
                    
            case "3":
                print_report()
                
            case "4":
                print("Cảm ơn bạn đã sử dụng hệ thống TechStore System. Tạm biệt!")
                break
                
            case _:
                print("[Lỗi]: Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4.")
                
        input("\nNhấn Enter để tiếp tục quay lại bảng Menu...")

main()