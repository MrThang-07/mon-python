# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#  1. Tính toàn vẹn dữ liệu và Phạm vi biến (Scope)
# Tại sao biến lưu tổng doanh thu (flight_revenue) và số ghế trống (available_seats) phải là biến toàn cục (Global)?

# Trong hệ thống đặt vé, hai thông số này đại diện cho trạng thái sống còn của chuyến bay theo thời gian thực.

# Nếu khai báo chúng là biến cục bộ (Local) bên trong các hàm book_seats() hay refund_seats(), giá trị của chúng sẽ bị xóa sạch ngay sau khi hàm kết thúc lượt chạy. Do đó, chúng bắt buộc phải là biến toàn cục nằm ở bộ nhớ tổng để tất cả các chức năng (Đặt vé, Hủy vé, Thống kê) cùng nhìn thấy, cùng sử dụng và cập nhật đồng bộ.
# (2) Viết code

BASE_PRICE = 2000.0
MAX_SEATS = 50
available_seats = 50
flight_revenue = 0.0

def calculate_ticket_price(seats_count, ticket_class):
    """
    Tính toán chi tiết giá vé dựa trên số lượng và phân hạng ghế của hành khách.
    
    Tham số đầu vào:
        seats_count (int): Số lượng vé máy bay khách muốn mua.
        ticket_class (int): Hạng vé lựa chọn (1: Economy, 2: Business).
    Giá trị trả về:
        float: Tổng chi phí thanh toán cuối cùng đã bao gồm 5% phí dịch vụ.
    """
    if ticket_class == 1:
        ticket_price = BASE_PRICE
        class_name = "Economy"
    else:
        ticket_price = BASE_PRICE * 1.5
        class_name = "Business"
        
    subtotal = seats_count * ticket_price
    service_fee = subtotal * 0.05
    final_price = subtotal + service_fee
    
    print("\n-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {seats_count} | Hạng: {class_name}")
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"Tổng thanh toán: ${final_price:.1f}")
    
    return final_price

def execute_booking(seats_count, total_cost):
    """Thực hiện trừ ghế trống và cộng dồn doanh thu toàn cục khi đặt vé thành công."""
    global available_seats, flight_revenue
    
    if seats_count > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return False
        
    available_seats = available_seats - seats_count
    flight_revenue = flight_revenue + total_cost
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
    return True

def process_refund(seats_count):
    """Xử lý nghiệp vụ hoàn trả vé, tính toán số tiền hoàn dựa trên chính sách hãng."""
    global available_seats, flight_revenue
    
    # Bẫy lỗi hủy khống vé (Ghost Refund)
    if available_seats + seats_count > MAX_SEATS:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0.0
        
    # Chính sách: Hoàn 80% giá vé cơ bản, không hoàn phí dịch vụ
    refund_amount = seats_count * (BASE_PRICE * 0.8)
    
    available_seats = available_seats + seats_count
    flight_revenue = flight_revenue - refund_amount
    
    return refund_amount

def print_flight_status():
    """
    In báo cáo chi tiết về tình trạng lấp đầy và doanh thu của chuyến bay VN2026.
    
    Tham số đầu vào: Không có.
    Giá trị trả về: Không có (None).
    """
    booked_seats = MAX_SEATS - available_seats
    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_SEATS}")
    print(f"Ghế đã đặt     : {booked_seats}")
    print(f"Ghế trống      : {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:.1f}")
    print("-" * 36)

def main():
    while True:
        print("""
============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================""")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        match choice:
            case "1":
                print("\n--- ĐẶT VÉ MÁY BAY ---")
                seats_str = input("Nhập số lượng vé: ").strip()
                
                if not seats_str.isdigit():
                    print("[Lỗi]: Số lượng vé phải là một số nguyên dương!")
                    continue
                    
                seats_count = int(seats_str)
                if seats_count <= 0:
                    print("[Lỗi]: Số lượng vé nhập vào phải lớn hơn 0.")
                    continue
                
                if seats_count > available_seats:
                    print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
                    continue
                    
                class_str = input("Chọn hạng vé (1: Economy, 2: Business): ").strip()
                if class_str != "1" and class_str != "2":
                    print("[Lỗi]: Hạng vé không hợp lệ! Vui lòng chỉ chọn 1 hoặc 2.")
                    continue
                    
                ticket_class = int(class_str)
                
                total_cost = calculate_ticket_price(seats_count, ticket_class)
                
                execute_booking(seats_count, total_cost)
                
            case "2":
                print("\n--- HỦY VÉ & HOÀN TIỀN ---")
                refund_str = input("Nhập số lượng vé muốn hủy: ").strip()
                
                if not refund_str.isdigit():
                    print("[Lỗi]: Số lượng vé hủy phải là một số nguyên dương!")
                    continue
                    
                refund_count = int(refund_str)
                if refund_count <= 0:
                    print("[Lỗi]: Số lượng vé nhập vào phải lớn hơn 0.")
                    continue
               
                amount_returned = process_refund(refund_count)
            
                if amount_returned > 0.0:
                    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${amount_returned:.1f} (80% giá cơ bản).")
                    print(f"Ghế trống hiện tại: {available_seats}")
                    
            case "3":
                print_flight_status()
                
            case "4":
                print("Hệ thống SkyBooking tạm đóng. Cảm ơn phiên làm việc của bạn!")
                break
                
            case _:
                print("[Lỗi]: Lựa chọn không hợp lệ, vui lòng chọn số từ 1 đến 4.")
                
        input("\nNhấn Enter để quay lại bảng Menu chính...")
main()