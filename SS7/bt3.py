# 1. Phân tích Input / Output
#     Input (Đầu vào): Chuỗi raw_data (Kiểu str) và dữ liệu do người dùng nhập từ bàn phím (Lựa chọn menu, Mã ID cần tìm).

#     Output (Đầu ra): Dữ liệu gốc, Bảng báo cáo đã làm sạch, hoặc Kết quả tìm kiếm nhân viên.

#     Đề xuất Giải pháp (Dùng String & Vòng lặp cơ bản)
#     Cắt chuỗi: Dùng .split("|") để tách từng người và .split(";") để tách thuộc tính (ID, Tên, SĐT, Phòng).

#     Làm sạch chữ: Dùng .strip() (xóa khoảng trắng), .upper() (viết hoa ID/Phòng), .title() (viết hoa chữ cái đầu của Tên).

#     Xử lý SĐT (Bẫy 1): Dùng .replace("-", "") xóa dấu gạch ngang. Nếu .isdigit() (toàn số) thì che bằng "******" + sdt[6:], ngược lại hiện "Invalid Format".

#     Chặn lỗi (Bẫy 2 & 3): * Dùng if len(thong_tin) == 4: để bỏ qua dòng lỗi, tránh sập nguồn.

#     Kiểm tra lựa chọn menu bằng danh sách ["1", "2", "3", "4"].

# (2) Triển khai code




raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
while True :
    print(""" ===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
        1. Hiển thị chuỗi dữ liệu gốc
        2. Chuẩn hóa dữ liệu và in báo cáo
        3. Tìm kiếm nhân viên theo mã ID
        4. Thoát chương trình """ )
    choice = int(input("Nhập lựa chọn của bạn (1 - 4) : "))
    if choice == 1 :
        print(raw_data)
    elif choice == 2 :
        list_danhsach = raw_data.split("|")
        print(f"{'ma_id':<10} | {'ho_ten':<20} | {'sdt':<15} | {'phong_ban':<10}")
       
        for i in list_danhsach :
            thong_tin = i.split(";")
            if len(thong_tin)== 4 :
                ma_id = thong_tin[0].strip().upper()
                ho_ten = thong_tin[1].strip().title()
                phong_ban = thong_tin[2].strip().upper()
                sdt = thong_tin[3].replace("-","")
                if sdt.isdigit():
                    sdt = "******" + sdt[6:] 
                else :
                    sdt = "Invalid Format"
                print(f"{ma_id:<10} | {ho_ten:<20} | {sdt:<15} | {phong_ban:<10}")

    elif choice == 3 :
        print("\n--- TÌM KIẾM NHÂN VIÊN ---")
        id_tim_kiem = input("Nhập mã nhân viên cần tìm: ")
       
        id_tim_kiem = id_tim_kiem.strip().upper()
        
        tim_thay = False
        list_danhsach = raw_data.split("|")
        
        for i in list_danhsach :
            thong_tin = i.split(";")
            if len(thong_tin) == 4 :
                ma_id_trong_data = thong_tin[0].strip().upper()
                if ma_id_trong_data == id_tim_kiem :
                    ho_ten = thong_tin[1].strip().title()
                    phong_ban = thong_tin[3].strip().upper()
                    
                    sdt = thong_tin[2].strip().replace("-", "")
                    if sdt.isdigit():
                        sdt = "******" + sdt[6:]
                    else:
                        sdt = "Invalid Format"
                    print(f"\n[Kết quả tìm thấy]")
                    print(f"- Mã ID: {ma_id_trong_data}")
                    print(f"- Họ tên: {ho_ten}")
                    print(f"- SĐT: {sdt}")
                    print(f"- Phòng ban: {phong_ban}\n")
                    tim_thay = True
                    break 
        
        # Sau khi tìm hết danh sách mà vẫn không thấy thì báo lỗi
        if tim_thay == False :
            print("\n Không tìm thấy nhân viên\n")
    elif choice == 4 :
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập đúng 1- 4 : ")