# (1) Phân tích lỗi
    #  transaction.strip() không đổi chuỗi gốc: Vì chuỗi trong Python là bất biến (immutable). Hàm chỉ trả về chuỗi mới, không gán lại (transaction = ...) thì chuỗi gốc giữ nguyên.

    # Ký tự phân tách thực tế: Dấu gạch đứng |.

    # transaction.split("-") bị sai: Vì dấu - nằm trong mã khóa học (PYTHON-01), không phải dấu phân tách các trường dữ liệu.

    # Dữ liệu trong parts bị lệch: Chuỗi bị chia đôi thành 2 phần (chỉ có index 0 và 1). Gọi đến parts[2] và parts[3] sẽ gây lỗi IndexError (sập chương trình).

    # Cần .strip() lại sau khi split(): Để xóa sạch các khoảng trắng thừa dính ở hai đầu từng phần tử (ví dụ: biến " PYTHON-01 " thành "PYTHON-01").

    # Cần ép amount sang số: Vì amount ban đầu là chữ (string). Phải chuyển sang số nguyên (int) thì Python mới hiểu để áp dụng định dạng dấu phẩy hàng nghìn (:,).
#  (2) Sửa code 
transaction = "   nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print(f"Số tiền: {amount:,} VND")
print("Trạng thái:", status)