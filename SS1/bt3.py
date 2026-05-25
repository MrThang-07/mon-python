# (1) Phân tích và thiết kế giải pháp
    # 1. Phân tích Input / Output
        # Input: * ho_ten (String): Họ tên bệnh nhân.

        # ma_ba (String): Mã bệnh án (cần viết hoa để chuẩn hóa).

        # khoa_phong (String): Khoa/Phòng khám chỉ định.

        # Output: Chuỗi ký tự định dạng chuẩn:
        # Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

    # 2. Đề xuất giải pháp
        # Dùng hàm input() để nhận dữ liệu từ bàn phím.

        # Dùng phương thức .strip() xóa khoảng trắng thừa và .upper() để viết hoa mã bệnh án.

        # Dùng cấu trúc f-string (f"...") để nối các biến thành chuỗi Output theo khuôn mẫu yêu cầu.

    # 3. Thiết kế thuật toán (Pseudocode)
        # Plaintext
        # BẮT ĐẦU
        #     Nhập ho_ten từ bàn phím 
        #     Nhập ma_ba từ bàn phím -> Chuyển thành CHỮ HOA
        #     Nhập khoa_phong từ bàn phím
            
        #     Tạo chuỗi kết quả = "Bệnh nhân: " + ho_ten + " - Mã BA: " + ma_ba + " - Chuyển tới: " + khoa_phong
            
        #     Hiển thị chuỗi kết quả ra màn hình
        # KẾT THÚC
#  (2) Triển khai code
ho_ten = input("Nhập họ tên bệnh nhân : ")
ma_ba = input("Mã bệnh nhân : ")
khoa_phong = input("Khoa/Phòng khám chỉ định : ")

ma_ba_chuan = ma_ba.upper()
phieu_kham = f"Bệnh nhân: {ho_ten} - Mã BA: {ma_ba_chuan} - Chuyển tới: {khoa_phong}"
print("\n--- Phiếu khám điện tử ---")
print(phieu_kham)
