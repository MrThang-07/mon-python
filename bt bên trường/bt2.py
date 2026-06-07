# # BAI 1
# ho_ten = input("Nhập họ tên nhân viên: ")
# gio_lam = int(input("Nhập số giờ làm việc: "))
# luong_gio = int(input("Nhập lương mỗi giờ: "))
# tong_luong = gio_lam * luong_gio
# print("Tổng lương tháng của", ho_ten, "là:", tong_luong)

# # BAI 2
# dtb = float(input("Nhập điểm trung bình của học sinh: "))
# if dtb >= 8.0:
#     xep_loai = "Giỏi"
# elif dtb >= 6.5:
#     xep_loai = "Khá"
# elif dtb >= 5.0:
#     xep_loai = "Trung bình"
# else:
#     xep_loai = "Yếu"
# print("Xếp loại học lực của học sinh là:", xep_loai)

# # BAI 3
# don_gia = int(input("Nhập đơn giá sản phẩm: "))
# so_luong = int(input("Nhập số lượng sản phẩm: "))
# tong_tien = don_gia * so_luong
# if tong_tien > 500000:
#     tong_tien = tong_tien * 0.9
# print("Số tiền phải thanh toán là:", tong_tien)

# # BAI 4
# n = int(input("Nhập số nguyên dương n: "))
# tong = 0
# for i in range(1, n + 1):
#     tong = tong + i
# print("Tổng các số từ 1 đến", n, "là:", tong)

# # BAI 5
# n = int(input("Nhập số n: "))
# dem = 0
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         dem = dem + 1
# print("Số lượng các số từ 1 đến", n, "chia hết cho 3 là:", dem)

# # BAI 6
# for lan in range(1, 4):
#     print("Lần thử thứ", lan)
#     user = input("Nhập username: ")
#     password = input("Nhập password: ")
#     if user == "admin" and password == "123456":
#         print("Đăng nhập thành công!")
#         break
#     else:
#         print("Sai tài khoản hoặc mật khẩu!")

# # BAI 7
# tong_doanh_thu = 0
# for ngay in range(1, 8):
#     doanh_thu = int(input("Nhập doanh thu ngày " + str(ngay) + ": "))
#     tong_doanh_thu = tong_doanh_thu + doanh_thu
# print("Tổng doanh thu của cả tuần là:", tong_doanh_thu)

# # BAI 8
# so_du = 10000000
# so_tien_rut = int(input("Nhập số tiền bạn muốn rút: "))
# if so_tien_rut > so_du:
#     print("Giao dịch thất bại: Số dư tài khoản không đủ!")
# elif so_tien_rut % 50000 != 0:
#     print("Giao dịch thất bại: Số tiền rút phải là bội số của 50.000đ!")
# else:
#     so_du = so_du - so_tien_rut
#     print("Giao dịch thành công! Số dư còn lại là:", so_du)

# # BAI 9
# print("MENU QUÁN:")
# print("1. Cà phê - 25.000đ")
# print("2. Trà sữa - 35.000đ")
# print("3. Nước cam - 30.000đ")
# chon_mon = input("Mời bạn chọn món (1-3): ")
# so_luong = int(input("Nhập số lượng ly: "))
# if chon_mon == "1":
#     don_gia = 25000
# elif chon_mon == "2":
#     don_gia = 35000
# else:
#     don_gia = 30000
# hoa_don = don_gia * so_luong
# if hoa_don > 100000:
#     hoa_don = hoa_don * 0.9
#     print("Hóa đơn trên 100k, bạn được giảm giá 10%!")
# print("Số tiền bạn cần thanh toán là:", hoa_don)

# # BAI 10
# so_nguyen = int(input("Nhập một số nguyên bất kỳ: "))
# if so_nguyen % 2 == 0:
#     print("Số", so_nguyen, "là số CHẴN.")
# else:
#     print("Số", so_nguyen, "là số LẺ.")

# # BAI 11
# a = float(input("Nhập số thứ nhất (a): "))
# b = float(input("Nhập số thứ hai (b): "))
# c = float(input("Nhập số thứ ba (c): "))
# so_lon_nhat = a
# if b > so_lon_nhat:
#     so_lon_nhat = b
# if c > so_lon_nhat:
#     so_lon_nhat = c
# print("Số lớn nhất trong 3 số vừa nhập là:", so_lon_nhat)

# bài 15 
sai_lien_tiep = 0
tong_so_lan_sai = 0

for lan in range(1, 6):
    print("--- LẦN THỬ THỨ", lan, "/ 5 ---")
    user = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    
    if user == "ADMIN" and password == "123456":
        print("ĐĂNG NHẬP THÀNH CÔNG!")
        break
    else:
        sai_lien_tiep = sai_lien_tiep + 1
        tong_so_lan_sai = tong_so_lan_sai + 1
        print("Sai tài khoản hoặc mật khẩu!")
        
        if sai_lien_tiep == 3:
            print("MÔ PHỎNG THÔNG BÁO: BẠN ĐÃ NHẬP SAI 3 LẦN LIÊN TIẾP! KHÓA TÀI KHOẢN 30S!")
            sai_lien_tiep = 0  
            
        if tong_so_lan_sai == 5:
            print("KHÓA TÀI KHOẢN VÌ NHẬP SAI QUÁ 5 LẦN!")