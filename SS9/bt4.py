# (I) Phân tích 
   # 1. Input:
# - Lựa chọn menu (1-4)
# - Mã đơn hàng, trạng thái đơn hàng
# - Vị trí đơn hàng (dạng số)

# 2. Output:
# - Danh sách đơn hàng
# - Thông báo thêm / sửa / xóa thành công
# - Thống kê số lượng đơn theo trạng thái
# - Thông báo lỗi khi nhập sai hoặc vị trí không hợp lệ

# 3. Chức năng:
# - Hiển thị danh sách đơn hàng (list)
# - Thêm đơn hàng mới (append)
# - Sửa đơn hàng theo vị trí (gán lại theo index)
# - Xóa đơn hàng theo vị trí (pop)
# - Thống kê theo trạng thái (duyệt list + đếm)

# 4. Xử lý dữ liệu:
# - Chuẩn hóa mã và trạng thái (strip + upper)
# - Kiểm tra nhập số bằng isdigit()
# - Kiểm tra vị trí hợp lệ trước khi sửa/xóa
# (II). Viết code 
order_list = []
while True :
    print("""  
    ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
        1. Hiển thị danh sách đơn hàng
        2. Cập nhật danh sách đơn hàng
        3. Thống kê đơn hàng theo trạng thái
        4. Thoát chương trình
    """)
    choice = input("Nhập lựa chọn chức năng 1 -4 : ")
    if choice == "1" :
        if len(order_list) == 0 :
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i,item in enumerate(order_list,start = 1) :
                print(f"{i}. {item}")

    elif choice ==  "2": 
        while True :
            print("""
            ----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
                1. Thêm đơn hàng mới
                2. Sửa đơn hàng theo vị trí
                3. Xóa đơn hàng theo vị trí
                4. Quay lại menu chính
            """)
            choice2 = input("Nhập lựa chọn chắc năng trên : ")
            if choice2 == "1":
                madonhang =input("Nhập mã đơn hàng : ").strip().upper()
                status = input("Nhập trạng thái đơn hàng : ").strip().upper()
                newOrder = madonhang + " - " + status 
                order_list.append(newOrder)
                print("Thêm thành công ")
            elif choice2 == "2":
                vitri = (input("Nhập ví trí đơn hàng cần sửa : "))
                if vitri.isdigit():
                    vitri = int(vitri)
                    found = False
                    for i in range(len(order_list)):
                        if (vitri - 1) == i:
                            madonhang =input("Nhập mã đơn hàng : ").strip().upper()
                            status = input("Nhập trạng thái đơn hàng : ").strip().upper()
                            newOrder = madonhang + " - " + status 
                            order_list[i] = newOrder
                            print("Sửa thành công ")
                            found = True 
                            break
                    if found == False:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else :
                    print("Vị trí không hợp lệ!")
            elif choice2 == "3":
                found =False 
                delete = (input("Nhập vị trí đơn hàng cần xóa : "))
                if delete.isdigit():
                    delete =int(delete)
                    for i in range(len(order_list)):
                        if delete - 1 == i :
                            vitridaxoa = order_list.pop(delete -1 )
                            print(f"Đơn hàng đã xóa : {vitridaxoa}")
                            found = True 
                            break 
                    if found == False :
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else :
                    print("Vị trí không hợp lệ!")
            elif choice2 == "4":
                    print("Đã quay lại menu chính !")
                    break
            else :
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
    elif choice == "3" :
        coutPENDING = 0
        coutDELIVERING = 0 
        coutCOMPLETED = 0
        coutCANCELLED = 0
        
        for item in order_list:
            i = item.split("-")[-1].strip().upper()
            
            if i == "PENDING":
                coutPENDING += 1 
            elif i == "DELIVERING":
                coutDELIVERING += 1
            elif i == "COMPLETED":
                coutCOMPLETED += 1
            elif i == "CANCELLED":
                coutCANCELLED += 1  
        
        print("===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING = {coutPENDING}")
        print(f"DELIVERING = {coutDELIVERING}")
        print(f"COMPLETED = {coutCOMPLETED}")
        print(f"CANCELLED = {coutCANCELLED}")
        print(f"Tổng số lượng đơn hàng : {len(order_list)}")
    elif choice == "4" :
        print("Thoát chương trình !")
        break
    else :
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
