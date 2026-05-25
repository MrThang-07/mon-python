# (1) Phân tích và thiết kế giải pháp (Ngắn gọn)
    # 1. Phân tích Input / Output
        # Input: * ho_ten (String): Họ tên bệnh nhân từ input().

        # tuoi (Integer): Tuổi bệnh nhân (ép kiểu về int).

        # Output: * Nếu dính bẫy dữ liệu: In thông báo LỖI:... và dừng chương trình.

        # Nếu hợp lệ: In Phiếu khám bệnh gồm Tên, Tuổi và Kết quả phân luồng (Phòng Nhi / Lão khoa / Khám thường).

    # 2. Đề xuất giải pháp
        # Xử lý Bẫy 1 (Tên trống/Space): Sử dụng phương thức .strip() để xóa khoảng trắng thừa. Nếu chuỗi sau khi xóa bằng rỗng "" thì tên lỗi.

        # Xử lý Bẫy 2 (Tuổi phi lý): Giới hạn độ tuổi con người hợp lệ từ 0 đến 150 tuổi.

        # Cấu trúc: Sử dụng Điều kiện lồng nhau (Nested if). Khối if bên ngoài dùng toán tử logic or để chặn toàn bộ dữ liệu rác (Bẫy 1 & Bẫy 2).
        #  Nếu dữ liệu vượt qua vòng giữ xe này, khối if-elif-else bên trong mới tiến hành phân loại tuổi.

    # 3. Thiết kế thuật toán (Mô tả luồng)
        # Plaintext
        # BẮT ĐẦU
        #     Nhập ho_ten -> Xóa khoảng trắng thừa bằng .strip()
        #     Nhập tuoi -> Ép kiểu sang int
            
        #     KIỂM TRA BẪY DỮ LIỆU (Vòng 1):
        #     Nếu (ho_ten == "") HOẶC (tuoi < 0) HOẶC (tuoi > 150):
        #         In "LỖI: Thông tin không hợp lệ!"
        #         KẾT THÚC CHƯƠNG TRÌNH NGAY
                
        #     PHÂN LUỒNG Y KHOA (Vòng 2 - Khi dữ liệu đã sạch):
        #         Nếu tuoi < 6: Xếp loại phòng khám Nhi
        #         Nếu tuoi >= 80: Xếp loại hỗ trợ xe lăn, phòng khám Lão khoa
        #         Các trường hợp còn lại: Xếp loại Khám thường
                
        #     IN PHIẾU KHÁM BỆNH TỔNG HỢP
        # KẾT THÚC



# (2) Triển khai mã nguồn Python

ho_ten = str(input("Nhập ho ten của bệnh nhân : "))
age = int(input("Nhập tuổi của bệnh nhân : "))
if ho_ten == "" or ho_ten == " " or age <= 0 :
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else :
    if age > 80 :
        hienthi = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    elif age > 6 :
        hienthi = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
    else :
        hienthi = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi." 
    print(hienthi)