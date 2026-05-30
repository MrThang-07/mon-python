# (I)
# 1. Phân tích Input / Output
# Input: * N: Số lượng phiếu (Kiểu int).

# chuoi_nhap: Chuỗi thông tin thô chứa dấu | (Kiểu string).

# Output: * Thông báo lỗi tương ứng nếu dính bẫy dữ liệu (Bỏ qua hoặc Dừng).

# Phiếu đã chuẩn hóa: Họ tên (Title), Khóa học (Title), Mã SV (UPPER), Email (lower), Mã xác nhận (MÃ_KHÓA-HỌC).

# 2. Đề xuất giải pháp & Các bước thực hiệnHệ thống sử dụng Pipeline 3 bước: 
#     Kiểm tra số lượng -> Kiểm tra định dạng -> Biến đổi chuỗi.Công cụ xử lý chuỗi: * Dùng .split('|') để bóc tách 4 trường dữ liệu.
#     Dùng .strip() dọn sạch khoảng trắng thừa.Dùng .title(), .lower(), .upper() để đồng bộ font chữ.Dùng .replace(" ", "-") 
#     để đổi khoảng trắng thành dấu gạch ngang khi tạo mã xác nhận.
# (II) Viết code 




so_luong_nhap = input("Nhập số lượng phiếu đăng ký cần xử lý: ")
so_luong = int(so_luong_nhap)

if so_luong <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
    print("Chương trình kết thúc.")
else:

    for i in range(so_luong):
        print("\n--- Nhập dữ liệu cho phiếu thứ", i + 1, "---")
        chuoi_tho = input("Họ tên | Khóa học | Mã học viên | Email: ")

        cac_phan = chuoi_tho.split("|")
        if len(cac_phan) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue  

        ho_ten = cac_phan[0].strip()
        khoa_hoc = cac_phan[1].strip()
        ma_sv = cac_phan[2].strip()
        email = cac_phan[3].strip()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

       
        if len(ma_sv) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

      
        ho_ten_chuan = ho_ten.title()
        khoa_hoc_chuan = khoa_hoc.title()

        
        ma_sv_chuan = ma_sv.upper()

   
        email_chuan = email.lower()

        khoa_hoc_viet_hoa = khoa_hoc_chuan.upper()
        ten_khoa_hoc_gach_ngang = khoa_hoc_viet_hoa.replace(" ", "-")
        ma_xac_nhan = ma_sv_chuan + "_" + ten_khoa_hoc_gach_ngang

        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", ho_ten_chuan)
        print("Khóa học:", khoa_hoc_chuan)
        print("Mã học viên:", ma_sv_chuan)
        print("Email:", email_chuan)
        print("Mã xác nhận:", ma_xac_nhan)