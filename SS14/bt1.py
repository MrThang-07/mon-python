# (1) PHÂN TÍCH LỖI
#     1. Sai thứ tự tham số
#     Thực trạng: Khi gọi hàm calculate_final_price(100000, 15000, 0.1), giá trị 15000 bị gán nhầm cho tỷ lệ giảm giá (discount),
#     còn 0.1 bị gán nhầm cho phí ship (shipping_fee).
#     2. Nhầm lẫn giữa print() và return
#     Thực trạng: Hàm cũ kết thúc bằng lệnh print() để hiển thị kết quả ra màn hình mà không có từ khóa return để trả dữ liệu về.
# (2) ĐỀ XUẤT GIẢI PHÁP & THIẾT KẾ THUẬT TOÁN
#     1. Giải pháp khắc phục
#     Định hình lại hàm: Thay thế hoàn toàn lệnh print() ở cuối hàm bằng từ khóa return total 
#     để đóng gói dữ liệu và đẩy kết quả tính toán ra ngoài cho các biến khác sử dụng.
# (3) Viết code 

def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total
order_total = calculate_final_price(100000, 0.1, 15000)
final_payment = order_total + 5000
print("Khách hàng cần thanh toán:", final_payment)