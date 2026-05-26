# (1) Phân Tích & Đề Xuất Giải Pháp
    # 1. Phân tích Input/Output

        # Input: Nhận một số nguyên từ người dùng (biến so_luong).

        # Output: * Nếu nhập <= 0 (Bẫy số âm, số 0): In lỗi, bắt nhập lại.

        # Nếu nhập > 0: In thông báo thành công, kết thúc chương trình.

    # 2. Bảng so sánh 2 giải pháp vòng lặp
        # Tiêu chí :

        #     Dùng while True + break :
        #     - Tiêu chíDùng while True + breakDùng while so_luong <= 0Cách hoạt độngLặp vô hạn. 
        #     Dùng lệnh break để chủ động đập vỡ vòng lặp khi dữ liệu đúng.
        #     - Ưu điểm	Code gọn gàng, không cần tạo biến mồi. 
        #     Dùng while so_luong <= 0 : 
        #         - Lặp có điều kiện. Phải "mồi" trước biến so_luong = 0 để vòng lặp khởi động.
        #         - Câu lệnh sát với tư duy tự nhiên: "Chừng nào còn sai thì còn lặp".
    # 3. Chốt lựa chọn
                # Chọn Cách 2 (while so_luong <= 0). Tuy phải thêm một dòng "mồi" biến ở đầu, nhưng logic của nó rất rõ ràng.
                # Đọc ngay dòng while là thấy được điều kiện chặn lỗi của chương trình mà không cần tìm kiếm lệnh break ở bên trong.

# (2) Triển Khai Code
print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

so_luong = 0

while so_luong <= 0:
    
    
    so_luong = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
  
    if so_luong <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")

print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {so_luong} nhân sự mới!")
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")