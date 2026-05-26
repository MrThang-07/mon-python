# (1) Phân Tích Lỗi
    # Bản chất lỗi: Khối lệnh if working_days == 0: hiện tại chỉ thực hiện đúng một nhiệm vụ là in ra dòng chữ cảnh báo. Do không có cấu trúc rẽ nhánh (else) hoặc lệnh điều hướng vòng lặp, chương trình mặc định chạy tuần tự từ trên xuống dưới.

    # Dò luồng thực thi (khi nhập ngày công = 0):

    # Chương trình nhận working_days = 0.

    # Thỏa mãn điều kiện if, in ra thông báo: "CẢNH BÁO...".

    # (Lỗi bắt đầu từ đây) Hệ thống không dừng lại mà tiếp tục chạy xuống dòng tính toán: bonus_amount = 0 * 200000 = 0.

    # Hệ thống tiếp tục chạy lệnh print và gửi email chúc mừng nhận 0 VNĐ.
    # Code đang thiếu else -> nên thêm else vào code để code đúng hơn không bị sai logic .

# (2) Sửa Lỗi
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")


for employee_number in range(1, 4):
    print(f"--- Đang xử lý nhân viên số {employee_number} ---")
  
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
   
    if working_days == 0:
      
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("----------------------------------------\n")
    #  Thêm else 
    else:
     
        bonus_amount = working_days * 200000
        print(f"-> Đã gửi Email: Chúc mừng nhận được {bonus_amount} VNĐ tiền thưởng!")
        print("----------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")