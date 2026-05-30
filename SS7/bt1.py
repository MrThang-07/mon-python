# (1) Phân tích lỗi
    # Nguyên nhân cốt lõi khiến đoạn code legacy bị sai kết quả là do Tính bất biến (Immutable) của kiểu dữ liệu chuỗi (string) 
    # trong Python.

    # Vì sao student_name.strip() không đổi trực tiếp biến gốc?
    # Hàm .strip() chỉ tìm các khoảng trắng ở hai đầu, tạo ra một bản sao chuỗi mới đã sạch khoảng trắng và trả về kết quả. 
    # Nó hoàn toàn không tác động hay sửa đổi gì vào vùng nhớ của biến student_name gốc.

    # Vì sao student_name.title() không ra "Nguyen Van A"?
    # Vì lệnh student_name.title() được gọi độc lập và kết quả trả về của nó (chuỗi đã viết hoa chữ cái đầu) bị "rơi vào hư vô" 
    # do không có biến nào hứng lấy. Hơn nữa, nó đang chạy trên chuỗi gốc vẫn còn khoảng trắng thừa ("  nguYEn vAn a  ").

    # Vì sao student_code.upper() và email.lower() không có tác dụng?
    # Tương tự như trên, các phương thức này chỉ sinh ra chuỗi mới đã viết hoa/viết thường. 
    # Do lập trình viên không gán ngược lại cho biến student_code và email, nên hai biến này vẫn giữ nguyên giá trị lỗi ban đầu.

    # Giải pháp: Muốn các phương thức xử lý chuỗi có hiệu lực, ta bắt buộc phải gán lại kết quả trả về vào chính biến đó
    # (hoặc một biến mới). Ngoài ra, có thể sử dụng kỹ thuật gọi phương thức liên tiếp (method chaining) để code ngắn gọn hơn.

# (2) Sửa lỗi 


student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "


student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()


print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)