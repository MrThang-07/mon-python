# (1) Phân tích và thiết kế giải pháp
# Phân tích Input / Output
# Dữ liệu ban đầu (Cố định): Danh sách lồng nhau cart_items chứa mã, tên, số lượng, đơn giá.

# Dữ liệu đầu vào (Input từ bàn phím):

# Lựa chọn menu (Chuỗi từ '1' đến '5').

# Khi thêm/sửa/xóa: Nhập mã sản phẩm (Chuỗi), tên sản phẩm (Chuỗi), số lượng (Số nguyên), đơn giá (Số nguyên).

# Dữ liệu đầu ra (Output): Các dòng chữ in ra màn hình (Bảng giỏ hàng, thông báo lỗi, thông báo thành công) định dạng giống như ảnh mô tả.

#  Đề xuất giải pháp & Thuật toán (Không dùng hàm)
# Quản lý menu: Sử dụng một vòng lặp vô hạn while True: để chương trình chạy liên tục cho đến khi người dùng chọn 5 để thoát (break).

# Xử lý lỗi nhập chữ vào ô số: Để tránh chương trình bị crash khi bạn chưa học try-except, chúng ta sẽ dùng phương thức kiểm tra chuỗi .isdigit() của String để xem người dùng có nhập đúng số nguyên dương hay không.

# Kiểm tra trùng mã: Sử dụng một biến cờ hiệu (Flag) kiểu Boolean (True/False) kết hợp vòng lặp for để quét qua danh sách sản phẩm xem mã nhập vào đã tồn tại chưa.
# (2) viết code

cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
while True :
    print("==================================================")
    print("          SHOPEE CART MANAGEMENT SYSTEM           ")
    print("==================================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("==================================================")
    choice = input("Nhập lựa chọn của bạn : ")
    match (choice):
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print("STT | Mã SP | Tên Sản Phẩm              | SL | Đơn Giá       | Thành Tiền")
            print("-" * 75)
            tong_so_luong = 0
            tong_tien_thanh_toan = 0
            sst = 1
            for item in cart_items:
                ma_sp = item[0]
                ten_sp = item[1]
                sl = item[2]
                gia = item[3]
                thanh_tien = sl*gia 
                tong_so_luong += sl
                tong_tien_thanh_toan += thanh_tien
                print(f"{stt:<4}| {ma_sp:<5} | {ten_sp:<25} | {sl:<2} | {gia:<13,}đ | {thanh_tien:<13,}")
                stt += 1
            print("-"*75)
            print(f"Tổng số lượng sản phẩm trong giỏ hàng là : {tong_so_luong}")
            print(f"Tổng tiền thanh toán : {tong_tien_thanh_toan}")
        case "2" :
            print("--- Thêm sản phẩm --- ")
            ma_nhap = input("Nhập mã sản phẩm : ").strip()
            if ma_nhap == "" :
                print("Lỗi: Mã sản phẩm không được để trống!")
                continue
            found = True 
            for item in cart_items : 
                if item[0] == ma_nhap:
                    found = False
                    sl_them_str = input("Mã sản phẩm đã tồn tại . Nhập số lượng cộng thêm : ").strip()
                    if not sl_them_str.isdigit() or int(sl_them_str) <= 0 : 
                        print("Lỗi: Số lượng nhập vào phải là số nguyên dương lớn hơn 0!")
                    else:
                        item[2] += int(sl_them_str)
                        print(f"Đã cộng dồn thành công sản phẩm {ma_nhap}.")
                        break
            if not found :
                ten_nhap = input("Nhập tên sản phẩm mới : ").strip()
                sl_nhap_str = input("Nhập số lượng: ").strip()
                gia_nhap_str = input("Nhập đơn giá : ").strip()
                if not sl_nhap_str.isdigit() or not gia_nhap_str.isdigit():
                    print("Lỗi: Số lượng và đơn giá phải là ký tự số!")
                elif int(sl_nhap_str) <= 0 or int(gia_nhap_str) < 0:
                    print("Lỗi: Số lượng phải > 0 và Đơn giá phải >= 0!")
                else:
                    new_item = [ma_nhap, ten_nhap, int(sl_nhap_str), int(gia_nhap_str)]
                    cart_items.append(new_item)
                    print(f"Đã thêm mới thành công sản phẩm {ma_nhap} vào giỏ hàng.")
        case "3":
            print("\n--- CẬP NHẬT SỐ LƯỢNG ---")
            ma_nhap = input("Nhập mã sản phẩm cần sửa: ").strip()
            found = False
            for item in cart_items:
                if item[0] == ma_nhap:
                    found = True 
                    sl_moi_str = input(f"Nhập số lượng mới cho sản phẩm {ma_nhap}: ").strip()
                    if not sl_moi_str.isdigit() or int(sl_moi_str) <= 0:
                        print("Lỗi: Số lượng mới phải là số nguyên dương lớn hơn 0!")
                    else:
                        item[2] = int(sl_moi_str) # Tiến hành gán đè số lượng mới
                        print(f"Cập nhật số lượng mới cho sản phẩm {ma_nhap} thành công.")
                    break
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
        case "4" : 
            print("\n--- XÓA SẢN PHẨM ---")
            ma_nhap = input("Nhập mã sản phẩm muốn xóa: ").strip()
            found = False
            for item in cart_items:
                if item[0] == ma_nhap:
                    found = True
                    cart_items.remove(item)
                    print(f"Đã xóa hoàn toàn sản phẩm {ma_nhap} khỏi giỏ hàng.")
                    break
            if not found :
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
        case "5":
            print("\nCảm ơn bạn đã sử dụng Shopee Cart Management System. Tạm biệt!")
            break
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chỉ nhập từ số 1 đến số 5.")



