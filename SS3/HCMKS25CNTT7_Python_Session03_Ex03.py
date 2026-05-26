# (1) Phân Tích và Thiết Kế Giải Pháp
    # 1. Phân tích Input/Output

        # Input: 3 chuỗi văn bản (String) nhập từ bàn phím cho mỗi lượt gồm: Mã nhân viên, Họ và tên, Phòng ban.

        # Output: * Trường hợp hợp lệ: Đoạn văn bản hiển thị "Phiếu Hồ Sơ Điện Tử".

        # Trường hợp không hợp lệ: Chuỗi cảnh báo đỏ: [CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.

    # 2. Đề xuất giải pháp

        # Vòng lặp: Sử dụng vòng lặp for lặp đúng 3 lần để xử lý 3 nhân sự.

        # Kiểm tra dữ liệu: Dùng cấu trúc if...else kết hợp với phương thức .strip(). 
        # Hàm .strip() giúp cắt bỏ khoảng trắng; nếu chuỗi sau khi cắt là rỗng (""), xác định ngay là lỗi (bỏ trống hoặc toàn dấu cách).

        # In phiếu: Nếu dữ liệu vượt qua bước kiểm tra (vào nhánh else), sử dụng thêm .upper() (viết hoa toàn bộ mã) 
        # và .title() (viết hoa chữ đầu của tên) để làm đẹp dữ liệu trước khi xuất ra màn hình.

    # 3. Thiết kế thuật toán (Pseudocode)

        # Plaintext
        # BẮT ĐẦU CHƯƠNG TRÌNH
        #   LẶP 3 LẦN:
        #     Nhập ma_nv, ten_nv, phong_ban
            
        #     # Kiểm tra tính hợp lệ
        #     NẾU ma_nv.strip() là rỗng HOẶC ten_nv.strip() là rỗng:
        #       In ra "[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ..."
            
        #     # Xử lý khi dữ liệu đúng
        #     NGƯỢC LẠI:
        #       ma_chuan = ma_nv.strip().upper()
        #       ten_chuan = ten_nv.strip().title()
            
        #       In ra "PHIẾU HỒ SƠ" với ma_chuan và ten_chuan
            
        #   KẾT THÚC LẶP
        # KẾT THÚC CHƯƠNG TRÌNH


#  2 Triển khai code

print("--- CHƯƠNG TRÌNH NHẬP HỒ SƠ NHÂN SỰ ---")


for i in range(1, 4):
    print(f"\nNhập thông tin cho nhân viên thứ {i}:")
    
  
    ma_nv = input("Mã nhân viên: ")
    ten_nv = input("Họ và tên   : ")
    phong_ban = input("Phòng ban   : ")
    

    if ma_nv.strip() == "" or ten_nv.strip() == "":
        print("-> LỖI: Bạn chưa nhập Mã hoặc Tên! Hủy bỏ hồ sơ này.")
        
    else:
       
        ma_chuan = ma_nv.strip().upper()      
        ten_chuan = ten_nv.strip().title()    
        phong_chuan = phong_ban.strip().title()
     
        print("\n--- PHIẾU HỒ SƠ ---")
        print(f"Mã NV : {ma_chuan}")
        print(f"Họ Tên: {ten_chuan}")
        print(f"Phòng : {phong_chuan}")
        print("-------------------")