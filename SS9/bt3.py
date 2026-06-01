# (I) phân tích

    # - Sử dụng List để lưu danh sách mã đơn hàng.
    # - Chức năng 1: Hiển thị toàn bộ đơn hàng trong danh sách bằng enumerate().
    # - Chức năng 2: Nhập mã đơn hàng mới, chuẩn hóa bằng strip() và upper(),
    #   sau đó thêm vào cuối danh sách bằng append().
    # - Chức năng 3: Nhập mã đơn hàng cần xóa, kiểm tra có tồn tại hay không.
    #   Nếu có thì xóa bằng remove(), nếu không thì thông báo không tìm thấy.
    # - Chức năng 4: Thoát chương trình bằng break.
    # - Kiểm tra trường hợp danh sách rỗng khi hiển thị.
    # - Xử lý lựa chọn menu không hợp lệ bằng câu lệnh if-elif-else.
# (II) viết code 


order_list = ["GE001", "GE002", "GE003"]
while True:
    print(""" ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
                    1. Hiển thị danh sách đơn hàng
                    2. Thêm đơn hàng mới
                    3. Xóa đơn hàng theo mã
                    4. Thoát chương trình
    """)
    choice = input("Nhập 1- 4 để thực hiện chương trình : ")
    if choice == "1":
        
        if len(order_list) == 0 :
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i,item in enumerate(order_list,start = 1) :
                print(f"{i}. {item}")
    elif choice == "2" :
        new_order = input("Nhập mã đơn hàng mới : ")
        new_order=new_order.strip().upper()
        order_list.append(new_order)
        print("Thêm thành công !")
    elif choice == "3":
        found = False 
        delete_order = input("Nhập đơn hàng cần xóa : ").strip().upper()
        for i in order_list:
            if delete_order == i :
                order_list.remove(delete_order)
                found = True 
                print("Đã xóa thành công !")
                break
        if found == False :
            print("Không tìm thấy đơn hàng cần xóa !")
    elif choice == "4":
        print("Đã thoát chương trình !")
        break
    else:
        print("vUI LÒNG NHẬP 1 -4 !")
             
