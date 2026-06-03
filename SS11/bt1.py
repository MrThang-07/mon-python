# (1) PHÂN TÍCH LỖI 
# Dựa trên mã nguồn hiện tại (Legacy Code), các câu hỏi phân tích lỗi được trả lời cụ thể như sau:

# Tuple product_info ban đầu có bao nhiêu phần tử?

# Có 4 phần tử: "SP001", "Áo polo nam", "Size L", và 299000.

# Phần tử "SP001" đang nằm ở index nào? Vì sao dòng product_code = product_info[1] lấy sai mã sản phẩm?

# "SP001" là phần tử đầu tiên nên nằm ở index 0.

# Dòng code trên lấy sai vì lập trình viên sử dụng index 1 (vị trí thứ 2), dẫn đến kết quả nhận được bị sai thành "Áo polo nam".

# Phần tử "Áo polo nam" đang nằm ở index nào? Vì sao dòng product_name = product_info[2] lấy sai tên sản phẩm?

# "Áo polo nam" nằm ở index 1.

# Dòng code trên lấy sai vì sử dụng index 2, dẫn đến kết quả bị sai thành "Size L".

# Vì sao dòng product_length = product_info.length() gây lỗi? Muốn đếm số phần tử trong tuple, cần dùng hàm nào?

# Dòng này gây lỗi AttributeError vì đối tượng tuple trong Python không có phương thức (method) tên là .length().

# Muốn đếm số phần tử trong tuple, chúng ta phải sử dụng hàm toàn cục len(tuple_name).

# Vì sao dòng product_info[3] = 279000 không hợp lệ? Tuple có cho phép sửa trực tiếp phần tử không?

# Dòng này không hợp lệ vì tuple là kiểu dữ liệu có đặc tính immutable (bất biến).

# Tuple không bao giờ cho phép sửa đổi, thêm hoặc xóa trực tiếp bất kỳ phần tử nào sau khi đã khởi tạo. Việc cố tình gán đè giá trị sẽ gây ra lỗi TypeError.

# Muốn cập nhật giá bán từ 299000 thành 279000, cần xử lý như thế nào?

# Chúng ta phải tạo ra một tuple hoàn toàn mới bằng cách trích xuất (slice) các phần tử cũ không thay đổi và cộng hợp với giá trị mới, hoặc gán lại toàn bộ giá trị mới vào biến product_info.
# (2) . Viết Code :
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_code = product_info[0]

product_name = product_info[1]

product_length = len(product_info)

product_info = (product_info[0], product_info[1], product_info[2], 279000)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)