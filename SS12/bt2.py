# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Phân tích Input / Output
# Dữ liệu hệ thống (Input): Danh sách saving_accounts chứa các dictionary lưu thông tin sổ tiết kiệm mẫu: [account_id (str), customer_name (str), balance (int), term_months (int), interest_rate (float), status (str)].

# Dữ liệu người dùng nhập (Input từ bàn phím):

# choice: Lựa chọn tính năng tại menu chính (Kiểu chuỗi str từ "1" đến "7").

# ma_nhap: Mã sổ tiết kiệm phục vụ việc tìm kiếm, chèn, xóa hoặc tính lãi (Kiểu str).

# ten_nhap: Tên khách hàng (Kiểu str).

# tien_str, ky_han_str, thang_gui_str: Chuỗi nhập số tiền, kỳ hạn, số tháng thực gửi cần dùng .isdigit() để kiểm tra trước khi chuyển sang số nguyên int.

# lai_suat_str: Chuỗi nhập lãi suất năm, cần kiểm tra định dạng số thực rồi chuyển sang kiểu float.

# Kết quả hiển thị (Output màn hình):

# Giao diện Menu quản lý và danh sách sổ tiết kiệm hiển thị chi tiết theo mẫu.

# Bảng số liệu tính toán tiền lãi dự kiến, tiền lãi thực tế nhận trước hạn kèm tổng số tiền.

# Các dòng thông báo trạng thái thành công hoặc báo lỗi vi phạm bẫy dữ liệu (Edge Cases).

# 2. Đề xuất giải pháp thực hiện
# Quản lý Menu: Dùng vòng lặp while True: kết hợp với cấu trúc match-case để phân phối luồng chạy của 7 chức năng.

# Chuẩn hóa chuỗi (String): Áp dụng .strip().upper() cho mọi ô nhập mã sổ tiết kiệm nhằm xóa khoảng trắng thừa và viết hoa đồng bộ.

# Kiểm tra dữ liệu số nguyên dương (Tiền, Kỳ hạn, Số tháng thực gửi): Dùng .isdigit() để quét chuỗi, nếu trả về True thì mới tiến hành ép kiểu int(), giúp chặn hoàn toàn lỗi sập ứng dụng khi nhập chữ cái hoặc số âm.

# Kiểm tra số thực (Lãi suất năm): Vì Python không có sẵn hàm .isfloat() đơn giản, cách kiểm tra thủ công hiệu quả nhất khi chưa học hàm nâng cao là: Loại bỏ một dấu chấm . duy nhất trong chuỗi lãi suất bằng .replace(".", "", 1), sau đó kiểm tra chuỗi còn lại có phải toàn số bằng .isdigit() hay không.

# Kiểm tra trạng thái sổ: Sử dụng cấu trúc biến cờ hiệu found (True/False) để xác định sổ có tồn tại không. Nếu có, thực hiện kiểm tra điều kiện item["status"] == "active" trước khi cho phép cập nhật thông tin hoặc tính toán tài chính.
# (2) Viết code 
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("""
        ===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
        1. Xem danh sách sổ tiết kiệm
        2. Mở sổ tiết kiệm mới
        3. Cập nhật thông tin sổ tiết kiệm
        4. Tất toán hoặc xóa sổ tiết kiệm
        5. Tính lãi dự kiến khi đến hạn
        6. Kiểm tra điều kiện rút trước hạn
        7. Thoát chương trình
          """)
    
    choice = input("Mời bạn chọn chức năng (1-7): ").strip()
    
    match choice:
        case "1":
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("Danh sách sổ tiết kiệm:")
                stt = 1
                for item in saving_accounts:
                    print(f"{stt}. Mã sổ: {item['account_id']} | Khách hàng: {item['customer_name']} | Số tiền gửi: {item['balance']} | Kỳ hạn: {item['term_months']} tháng | Lãi suất: {item['interest_rate']}%/năm | Trạng thái: {item['status']}")
                    stt += 1
                    
        case "2":
            print("--- MỞ SỔ TIẾT KIỆM MỚI ---")
            ma_nhap = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            
            if ma_nhap == "":
                print("Lỗi: Mã sổ tiết kiệm không được để trống!")
                continue
                
            found = False
            for item in saving_accounts:
                if item["account_id"] == ma_nhap:
                    found = True
                    break
                    
            if found:
                print("Mã sổ tiết kiệm đã tồn tại!")
            else:
                ten_nhap = input("Nhập tên khách hàng: ").strip()
                if ten_nhap == "":
                    print("Tên khách hàng không được để trống")
                    continue
                    
                tien_str = input("Nhập số tiền gửi: ").strip()
                ky_han_str = input("Nhập kỳ hạn gửi theo tháng: ").strip()
                lai_suat_str = input("Nhập lãi suất năm: ").strip()
                
                if not tien_str.isdigit() or not ky_han_str.isdigit():
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue
                    
                check_rate = lai_suat_str.replace(".", "", 1)
                if not check_rate.isdigit():
                    print("Lại suất không hợp lệ!")
                    continue
                    
                balance = int(tien_str)
                term_months = int(ky_han_str)
                interest_rate = float(lai_suat_str)
                
                if balance <= 0 or term_months <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                elif interest_rate <= 0:
                    print("Lại suất không hợp lệ!")
                else:
                    new_account = {
                        "account_id": ma_nhap,
                        "customer_name": ten_nhap,
                        "balance": balance,
                        "term_months": term_months,
                        "interest_rate": interest_rate,
                        "status": "active"
                    }
                    saving_accounts.append(new_account)
                    print("Mở sổ tiết kiệm mới thành công!")
                    
        case "3":
            print("--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
            ma_nhap = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            
            found = False
            for item in saving_accounts:
                if item["account_id"] == ma_nhap:
                    found = True
                    if item["status"] == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    else:
                        ten_nhap = input("Nhập tên khách hàng mới: ").strip()
                        if ten_nhap == "":
                            print("Tên khách hàng không được để trống")
                            break
                            
                        tien_str = input("Nhập số tiền gửi mới: ").strip()
                        ky_han_str = input("Nhập kỳ hạn mới theo tháng: ").strip()
                        lai_suat_str = input("Nhập lãi suất năm mới: ").strip()
                        
                        if not tien_str.isdigit() or not ky_han_str.isdigit():
                            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                            break
                            
                        check_rate = lai_suat_str.replace(".", "", 1)
                        if not check_rate.isdigit():
                            print("Lại suất không hợp lệ!")
                            break
                            
                        balance = int(tien_str)
                        term_months = int(ky_han_str)
                        interest_rate = float(lai_suat_str)
                        
                        if balance <= 0 or term_months <= 0:
                            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        elif interest_rate <= 0:
                            print("Lại suất không hợp lệ!")
                        else:
                            item["customer_name"] = ten_nhap
                            item["balance"] = balance
                            item["term_months"] = term_months
                            item["interest_rate"] = interest_rate
                            print("Cập nhật thông tin sổ tiết kiệm thành công!")
                    break
                    
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")
                
        case "4":
            print("--- TẤT TOÁN SỔ TIẾT KIỆM ---")
            ma_nhap = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            
            found = False
            for item in saving_accounts:
                if item["account_id"] == ma_nhap:
                    found = True
                    if item["status"] == "closed":
                        print("Sổ tiết kiệm này đã được tất toán trước đó!")
                    else:
                        item["status"] = "closed"
                        print("Tất toán sổ tiết kiệm thành công!")
                    break
                    
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")
                
        case "5":
            print("--- TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
            ma_nhap = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            
            found = False
            for item in saving_accounts:
                if item["account_id"] == ma_nhap:
                    found = True
                    if item["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    else:
                        tien_lai = item["balance"] * item["interest_rate"] / 100 * item["term_months"] / 12
                        tong_nhan = item["balance"] + tien_lai
                        print(f"Tiền lãi dự kiến đến hạn: {tien_lai:,}đ")
                        print(f"Tổng tiền nhận khi đến hạn: {tong_nhan:,}đ")
                    break
                    
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")
                
        case "6":
            print("--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
            ma_nhap = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            
            found = False
            for item in saving_accounts:
                if item["account_id"] == ma_nhap:
                    found = True
                    if item["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    else:
                        thang_gui_str = input("Nhập số tháng thực gửi: ").strip()
                        if not thang_gui_str.isdigit() or int(thang_gui_str) <= 0:
                            print("Số tháng thực gửi không hợp lệ!")
                        else:
                            thang_gui = int(thang_gui_str)
                            if thang_gui < item["term_months"]:
                                lai_suat_ap_dung = 0.5
                                print("Thông báo: Khách hàng rút tiền trước hạn (Hưởng lãi suất không kỳ hạn 0.5%/năm).")
                            else:
                                lai_suat_ap_dung = item["interest_rate"]
                                print("Thông báo: Khách hàng gửi đủ hoặc quá kỳ hạn (Hưởng lãi suất đúng hạn ban đầu).")
                                
                            tien_lai = item["balance"] * lai_suat_ap_dung / 100 * thang_gui / 12
                            tong_nhan = item["balance"] + tien_lai
                            print(f"Tiền lãi thực nhận: {tien_lai:,}đ")
                            print(f"Tổng tiền thực nhận: {tong_nhan:,}đ")
                    break
                    
            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")
                
        case "7":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")
            
    input("\nNhấn Enter để tiếp tục...")