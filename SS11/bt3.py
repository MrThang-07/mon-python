# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Phân tích Input / Output
# Dữ liệu hệ thống (Input): Danh sách product_list gồm các đối tượng dictionary lưu thông tin sản phẩm mẫu: [product_id (str), product_name (str), price (int), quantity (int)].

# Dữ liệu người dùng nhập (Input từ bàn phím):

# choice: Lựa chọn chức năng của menu chính (Kiểu str từ "1" đến "5").

# ma_sp, found_id, delete_id: Mã sản phẩm nhập vào phục vụ tìm kiếm/thêm/xóa (Kiểu str).

# name_sp: Tên sản phẩm mới hoặc tên cần sửa (Kiểu str).

# sl_sp, price_sp: Số lượng và giá bán do người dùng nhập (Kiểu chuỗi str, cần kiểm tra hợp lệ rồi ép về số nguyên int).

# Kết quả hiển thị (Output màn hình): * Giao diện Menu quản lý Yody và danh sách sản phẩm đánh số thứ tự từ 1 tăng dần.

# Các dòng thông báo thành công hoặc thông báo lỗi bẫy dữ liệu (trùng mã, nhập rỗng, nhập chữ vào ô số, mã không tồn tại).

# 2. Đề xuất giải pháp thực hiện
# Điều hướng luồng chạy: Dùng vòng lặp vô hạn while True: kết hợp cấu trúc match-case giúp chia tách 5 chức năng riêng biệt một cách trực quan, mạch lạc.

# Xử lý chuỗi (String):

# Dùng .strip() để làm sạch khoảng trắng thừa và .upper() để chuẩn hóa mã sản phẩm thành chữ hoa tự động (Xử lý Bẫy 1).

# Kiểm tra chuỗi rỗng ma_sp == "" kết hợp lệnh continue để hủy thao tác lập tức và quay về menu nếu người dùng để trống mã sản phẩm.

# Dùng phương thức .isdigit() để chặn triệt để bẫy người dùng nhập chữ vào ô số, ngăn chương trình bị sập nguồn (crash).

# Xử lý cấu trúc dữ liệu (List & Dictionary):

# Dùng vòng lặp for item in product_list: phối hợp biến cờ hiệu found (True/False) đặt ngoài vòng lặp để kiểm tra chính xác trạng thái tồn tại của mã sản phẩm (Xử lý Bẫy 2 & Bẫy 3).

# Dùng phương thức .append() để thêm mới một dictionary sản phẩm vào danh sách và .remove(item) để xóa trực tiếp dictionary ra khỏi danh sách.
# (2) Viết code 


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True :
    print("""
        ===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
        1. Hiển thị danh sách sản phẩm
        2. Thêm sản phẩm mới
        3. Cập nhật thông tin sản phẩm
        4. Xóa sản phẩm theo mã
        5. Thoát chương trình 
          """)
    choice = input("Nhập lựa chọn của bạn : ")
    match (choice):
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                stt = 1
                for item in product_list:
                    print(f"{stt}. Mã SP: {item['product_id']} | Tên: {item['product_name']} | Giá: {item['price']} | Số Lượng: {item['quantity']}")
                    stt += 1
        case "2":
            print("--- Nhập thông tin sản phẩm mới ---")
            ma_sp = input("Nhập mã sản phẩm : ").strip()
            ma_sp = ma_sp.upper()
            if ma_sp == "":
                print("Lỗi: Mã sản phẩm không được để trống!")
                continue
            found =False
            for item in product_list:
                if ma_sp == item["product_id"]:
                    found = True 
                    break
            if found == True :
                    print("Mã sản phẩm bị trùng !")
            else:
                name_sp = input("Nhập tên sản phẩm :  ")
                sl_sp = input("Nhập số lượng : ")
                price_sp = input("Nhập giá sản phẩm")
                if not sl_sp.isdigit() or not price_sp.isdigit():
                    print("Giá/Số lượng không hợp lệ")
                elif int(sl_sp) <= 0 or int(price_sp) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    new_sp = {"product_id": ma_sp,"product_name": name_sp, "price": int(price_sp), "quantity": int(sl_sp)}
                    product_list.append(new_sp)  
                    print("Thêm sản phẩm thành công") 
        case "3":
            found_id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
            found_id = found_id.upper()
            found = False 
            for item in product_list:
                if found_id == item["product_id"] :
                    found = True 
                    name_sp = input("Nhập tên sản phẩm :  ")
                    sl_sp = input("Nhập số lượng : ")
                    price_sp = input("Nhập giá sản phẩm")
                    if not sl_sp.isdigit() or not price_sp.isdigit():
                        print("Giá/Số lượng không hợp lệ")
                    elif int(sl_sp) <= 0 or int(price_sp) <= 0:
                        print("Giá/Số lượng không hợp lệ")
                    else:
                        item["product_name"] = name_sp
                        item["price"] = int(price_sp)
                        item["quantity"] = int(sl_sp)
                        print("Cập nhật thông tin sản phẩm thành công")
                    break
            if not found :
                    print("Không tìm thấy mã sản phẩm cần cập nhật!")
        case "4":
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip()
            delete_id = delete_id.upper()
            found = False
            for item in product_list:
                if delete_id == item["product_id"]:
                    found = True 
                    break
            if found == True:
                product_list.remove(item)
                print("Xóa Thành công !")
            else:
                    print("Không tìm thấy mã sản phẩm cần xoá!")
        case "5":
            print("Thoát chương trình.Sau đó dừng chương trình.")
            break
        case _:
            print("Vui lòng nhập từ 1 - 5 : ")