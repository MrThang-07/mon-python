# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#  1. Phân tích Input / Output
# Dữ liệu hệ thống (Input): Danh sách product_list gồm các dictionary lưu thông tin sản phẩm có sẵn: [product_id (str), product_name (str), price (int), quantity (int), sold (int)].

# Dữ liệu người dùng nhập (Input từ bàn phím):

# choice: Lựa chọn tính năng tại menu chính (Kiểu str từ "1" đến "5").

# ma_sp: Mã sản phẩm dùng để tìm kiếm khi Bán hàng hoặc Nhập kho (Kiểu str).

# sl_str: Số lượng khách mua hoặc số lượng nhập kho do người dùng nhập (Kiểu str).

# Kết quả hiển thị (Output màn hình):

# Giao diện Menu vận hành và danh sách sản phẩm hiển thị kèm trạng thái tồn kho động (Còn hàng / Sắp hết hàng / Hết hàng).

# Báo cáo doanh thu chi tiết, tổng doanh thu và tên sản phẩm bán chạy nhất (có số lượng sold cao nhất).

# Các dòng chữ thông báo lỗi bẫy dữ liệu hoặc thông báo thao tác thành công.

# 2. Đề xuất giải pháp thực hiện
# Quản lý Menu: Dùng vòng lặp while True: duy trì chương trình chạy liên tục và cấu trúc rẽ nhánh match-case để phân phối 5 chức năng.

# Chuẩn hóa chuỗi (String): Sử dụng .strip().upper() để xử lý triệt để bẫy nhập chữ thường hoặc thừa dấu cách của mã sản phẩm (Bẫy 1).

# Kiểm tra số nguyên dương: Sử dụng phương thức .isdigit() để kiểm tra chuỗi nhập vào trước khi ép kiểu sang int(), giúp chặn hoàn toàn bẫy nhập chữ, số âm hoặc bằng 0 (Bẫy 3).

# Phân tích thuật toán báo cáo (Chức năng 4):

# Duyệt vòng lặp qua danh sách để tính toán revenue = price * sold.

# Sử dụng thuật toán tìm giá trị lớn nhất (Max) bằng cách gán một biến max_sold = -1 và biến best_seller = "" để tìm ra sản phẩm bán chạy nhất.

# Dùng biến cờ hiệu has_revenue để kiểm tra xem đã có bất kỳ sản phẩm nào phát sinh số lượng bán (sold > 0) hay chưa.
# (2) Viết code 


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("""
        ===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
        1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
        2. Bán sản phẩm cho khách hàng
        3. Nhập thêm hàng vào kho
        4. Xem báo cáo doanh thu
        5. Thoát chương trình
          """)
    
    choice = input("Nhập lựa chọn của bạn : ").strip()
    
    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại:")
                stt = 1
                for item in product_list:
                    if item["quantity"] == 0:
                        trang_thai = "Hết hàng"
                    elif item["quantity"] <= 5:
                        trang_thai = "Sắp hết hàng"
                    else:
                        trang_thai = "Còn hàng"
                        
                    print(f"{stt}. Mã SP: {item['product_id']} | Tên: {item['product_name']} | Giá: {item['price']} | Tồn kho: {item['quantity']} | Đã bán: {item['sold']} | Trạng thái: {trang_thai}")
                    stt += 1
                    
        case "2":
            print("--- BÁN SẢN PHẨM ---")
            ma_sp = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            
            found = False
            for item in product_list:
                if item["product_id"] == ma_sp:
                    found = True
                    sl_str = input("Nhập số lượng khách mua: ").strip()
                    
                    if not sl_str.isdigit():
                        print("Số lượng mua không hợp lệ")
                    elif int(sl_str) <= 0:
                        print("Số lượng mua không hợp lệ")
                    elif int(sl_str) > item["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        sl_mua = int(sl_str)
                        item["quantity"] -= sl_mua
                        item["sold"] += sl_mua
                        thanh_tien = sl_mua * item["price"]
                        print(f"Bán hàng thành công! Số tiền khách cần thanh toán: {thanh_tien:,}đ")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần bán")
                
        case "3":
            print("--- NHẬP THÊM HÀNG VÀO KHO ---")
            ma_sp = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            
            found = False
            for item in product_list:
                if item["product_id"] == ma_sp:
                    found = True
                    sl_str = input("Nhập số lượng nhập thêm: ").strip()
                    
                    if not sl_str.isdigit():
                        print("Số lượng nhập kho không hợp lệ")
                    elif int(sl_str) <= 0:
                        print("Số lượng nhập kho không hợp lệ")
                    else:
                        sl_nhap = int(sl_str)
                        item["quantity"] += sl_nhap
                        print(f"Nhập kho thành công! Số lượng tồn kho mới của {ma_sp} là: {item['quantity']}")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")
                
        case "4":
            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            
            has_revenue = False
            tong_doanh_thu = 0
            max_sold = -1
            best_seller = ""
            stt = 1
            
            for item in product_list:
                if item["sold"] > 0:
                    has_revenue = True
                    
                doanh_thu_sp = item["price"] * item["sold"]
                tong_doanh_thu += doanh_thu_sp
                
                print(f"{stt}. {item['product_name']} | Đã bán: {item['sold']} | Doanh thu: {doanh_thu_sp:,}đ")
                stt += 1
                
                if item["sold"] > max_sold:
                    max_sold = item["sold"]
                    best_seller = item["product_name"]
                    
            if not has_revenue:
                print("Chưa có doanh thu phát sinh.")
            else:
                print("-" * 50)
                print(f"Tổng doanh thu: {tong_doanh_thu:,}đ")
                print(f"Sản phẩm bán chạy nhất: {best_seller}")
                
        case "5":
            print("Thoát chương trình. Sau đó dừng chương trình.")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            
