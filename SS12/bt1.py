
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
#  1. Phân tích Input / Output
# Dữ liệu hệ thống (Input): Danh sách cart_items chứa các phần tử con là dictionary biểu diễn sản phẩm: {"id": str, "name": str, "number": int, "price": int}.

# Dữ liệu người dùng nhập (Input):

# choice: Lựa chọn số chức năng từ menu chính (str từ "1" đến "5").

# ma_nhap, name_nhap: Thông tin mã định danh và tên sản phẩm (str).

# sl_sp, sl_nhap, don_gia: Chuỗi nhập số lượng và đơn giá, cần kiểm tra định dạng để ép về số nguyên (int).

# Kết quả hiển thị (Output): Bảng chi tiết giỏ hàng được căn lề thẳng cột, tổng tiền, tổng số lượng và các dòng thông báo phản hồi trạng thái dữ liệu (báo lỗi hoặc báo thành công).

#  2. Đề xuất giải pháp thực hiện
# Vòng lặp & Luồng xử lý: Sử dụng while True: để duy trì menu chạy liên tục và cấu trúc match-case giúp chia tách 5 chức năng một cách trực quan, mạch lạc.

# Chuẩn hóa chuỗi (String): Sử dụng phương thức .strip().upper() nhằm xóa khoảng trắng thừa và viết hoa mã nhập vào tự động. Áp dụng phương thức .isdigit() trên các chuỗi nhập số để ngăn chặn triệt để lỗi sập chương trình (crash) khi người dùng gõ chữ cái.

# Tương tác cấu trúc dữ liệu: Dùng vòng lặp for kết hợp biến cờ hiệu logic found kiểm tra sự tồn tại của mã sản phẩm. Nếu tìm thấy thì thực hiện các thao tác cập nhật trực tiếp trên các khóa tương ứng (item["number"]), nếu không tìm thấy thì tiến hành chèn thêm dictionary mới bằng .append() hoặc đưa ra thông báo phù hợp. Dùng .remove() để xóa phần tử.
# (2) Viết code 


cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]
while True :
    print("""
        ========================================================
                     SHOPEE CART MANAGEMENT SYSTEM
        ========================================================
        1. Xem chi tiết giỏ hàng & Tính tổng tiền 
        2. Thêm sản phẩm mới / Cộng dồn só lượng 
        3. Cập nhật số lượng của một sản phẩm 
        4. Xóa sản phẩm khỏi giỏ hàng 
        5. Thoát chương trình 
        ========================================================""")
    choice = input("Mời bạn chọn chức năng (1- 5): ")
    match (choice):
        case "1":
            print("--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<5} | {'Mã SP':<5} | {'Tên Sản Phẩm':<20} | {'SL':<5} | {'Đơn giá':<10} | {'Thành Tiền':<10}")
            print("-"*65)
            stt = 1
            thanh_tien = 0 
            tong_thanh_tien = 0
            tong_sl = 0 
            for item in cart_items:
                thanh_tien = item["number"] * item["price"]
                tong_thanh_tien += thanh_tien
                tong_sl += item["number"]
                print(f"{stt:<5} | {item['id']:<5} | {item['name']:<20} | {item['number']:<5} | {item['price']:<10} | {thanh_tien:<10} ")
                stt += 1
            print("-"*65)
            print(f"=> Tổng số lượng sản phẩm trong giỏ : {tong_sl}")
            print(f"=> TỔNG TIỀN THANH TOÁN {tong_thanh_tien:,}đ")
        case "2":
            ma_nhap = input("Nhập mã sản phẩn cần thêm hoặc tăng số lượng : ").strip().upper()
            found = False 
            for item in cart_items:
                if ma_nhap == item["id"]:
                    found = True 
                    sl_sp = input("Nhập số lượng cần thêm : ")
                    if not sl_sp.isdigit():
                        print("Vui lòng nhập số nguyên dương !")
                    else:
                        if int(sl_sp) <= 0 :
                            print("Vui lòng nhập số lượng > 0 !")
                            
                        else:
                            item["number"] += int(sl_sp)
                            print("Đã thêm số lượng thành công !")
                    break
            if not found:
                name_nhap = input("Nhập tên sản phẩm cần thêm : ").strip()
                sl_nhap = input("Nhập số lượng cần thêm : ").strip()
                don_gia = input("Nhập đơn giá cho sản phẩm : ").strip()
                if not sl_nhap.isdigit() or not don_gia.isdigit() :
                        print("Vui lòng nhập số nguyên dương !")
                else:
                    if int(sl_nhap) <= 0 or int(don_gia) < 0:
                        print("Vui lòng nhập  số lượng > 0 hoặc đơn giá >= 0 ! ")
                    else:
                        new_sp = {"id": ma_nhap, "name": name_nhap, "number": int(sl_nhap), "price": int(don_gia)}
                        cart_items.append(new_sp)
                        print("Đã thêm sản phẩm mới thành công !")
        case "3":
            ma_nhap = input("Nhập mã sản phẩm cần cập nhật : ").strip().upper()
            found = False
            for item in cart_items:
                if ma_nhap == item["id"] :
                    found = True 
                    sl_sp = input("Nhập số lượng cần cập nhật lại : ")
                    if not sl_sp.isdigit():
                        print("Vui lòng nhập số nguyên dương !")
                    else:
                        if int(sl_sp) <= 0 :
                            print("Vui lòng nhập số lượng > 0 !")
                            
                        else:
                            item["number"] = int(sl_sp)
                            print("Đã cập nhật thành công !")
                    break
            if not found :
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
        case "4":
            ma_nhap = input("Nhập mã sản phẩm cần xóa : ").strip().upper()
            found = False
            for item in cart_items:
                if ma_nhap == item["id"] :
                    found = True 
                    cart_items.remove(item)
                    print("Đã xóa sản phẩm thành công.")
                    break
            if not found :
                print("Không tìm thấy sản phẩm !")
        case "5":
            print("Thoát chương trình !")
            break
        case _:
            print("Vui lòng nhập từ 1 - 5 !")

