# (1) Phân Tích Lỗi 
#     Bản chất lỗi: Lệnh khởi tạo total_budget = 0 bị đặt bên trong vòng lặp for.

#     Hậu quả: Mỗi khi chuyển sang nhân viên mới, vòng lặp lại chạy lệnh gán tổng tiền về 0.
#     Do đó, quá trình cộng dồn bị xóa sạch và biến này chỉ lưu được mức lương của người cuối cùng.

#     Cách khắc phục: Đưa dòng total_budget = 0 ra bên ngoài (phía trước vòng lặp) 
#     để biến chỉ bị reset một lần duy nhất lúc bắt đầu chạy chương trình.
# (2) Sửa Lỗi

print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")


total_budget = 0


for employee_number in range(1, 4):
    print(f"Đang xử lý nhân viên số {employee_number}")

    salary = int(input("  Nhập mức lương (VNĐ): "))
    
  
    total_budget = total_budget + salary 


print(f"=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ: {total_budget} VNĐ")