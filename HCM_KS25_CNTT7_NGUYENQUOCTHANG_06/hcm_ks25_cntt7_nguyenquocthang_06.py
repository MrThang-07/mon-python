list_booking =[
    {"id": "BK001","name_room": "Phòng Thảo Luận A","name_user": "Phòng Marketting" ,"fist_time": 9 , "last_time" : 18,"sum_time" : 9, "phanloai" : "Quá tải ( Cần xem xét lại )"}
]

def validate_time(fist,last):
    sum_time = fist + last 
    if sum_time < 2:
        phanloai = "Ngắn"
    elif sum_time < 4:
        phanloai = "Tiêu chuẩn"
    elif sum_time < 6:
        phanloai = "Dài"
    else:
        phanloai = "Quá tải ( Cần xem xét lại )"
    return sum_time,phanloai

def validate(input_time,input_min,input_max):
    while True:
        input_in = input(input_time).strip()
        if input_in.isdigit():
            input_in = int(input_in)
            if input_min <= input_in < input_max :
                return input_in
        print("Vui lòng nhập số nguyên ! - (nhập giờ đầu 0 - 24 - giờ kết thúc >= giờ đầu) :")

def display_list(booking):
    if len(booking) == 0 :
        print("Danh sách hiện không có dữ liệu nào !")
        return
    print(f"{'Mã BK':<5} | {'Tên phòng':<20} | {'Người đặt':<20} | {'Giờ bắt đầu':<15} | {'Giờ kết thúc':<15} | {'Thời lượng':<15} | {'Phân loại':<20}")
    for item in booking:
        print(f"{item['id']:<5} | {item['name_room']:<20} | {item['name_user']:<20} | {item['fist_time']:<15} | {item['last_time']:<15} | {item['sum_time']:<15} | {item['phanloai']:<20}")

def add_room(booking):
    input_id = input("Nhập mã đặt phòng :").strip().upper()
    if len(input_id) == 0:
        print("Vui lòng nhập mã không được rỗng !")
        return
    for item in booking:
        if input_id == item["id"]:
            print("Mẫ đã tồn tại !")
            return
    input_nameroom = input("Nhập tên phòng họp :").strip().title()
    if len(input_nameroom) == 0:
        print("Vui lòng nhập tên phòng không được rỗng !")
        return
    input_nameuser = input("Nhập tên người đặt :").strip().title()
    if len(input_nameuser) == 0:
        print("Vui lòng nhập tên không được rỗng !")
        return
    time_fist = validate("Nhập giờ bắt đầu : ",0,24)
    time_last = validate("Nhập giờ kết thúc : ",time_fist,24)
    tong_thoiluong, khunggio = validate_time(time_fist,time_last)
    new_room = {"id": input_id,"name_room": input_nameroom,"name_user": input_nameuser ,"fist_time": time_fist , "last_time" : time_last,"sum_time" : tong_thoiluong, "phanloai" : khunggio}
    list_booking.append(new_room)
    print("Đã thêm phòng mới")

def update_room(booking):
    input_id = input("Nhập mã phòng cần cập nhật :").strip().upper()
    for item in booking:
        if input_id == item["id"]:
            item["name_room"] = input("Nhập lại tên phòng cần cập nhật: ").strip().title()
            if len(item["name_room"]) == 0:
                print("Vui lòng nhập tên phòng không được rỗng !")
                return
            item["fist_time"] = validate("Nhập giờ bắt đầu : ",0,24)
            item["last_time"] = validate("Nhập giờ kết thúc : ",item["fist_time"],24)
            item["sum_time"],item["phanloai"] = validate_time(item["fist_time"],item["last_time"])
            print("Cập nhật thành công .")
            return
    print("Không tìm thấy mã phòng !")
    return
def remove_room(booking):
    input_id = input("Nhập mã phòng cần xóa :").strip().upper()
    for item in booking:
        if input_id == item["id"]:
            choice_yn = input("Bạn có chắc muốn hủy lịch đặt phòng này không ? (Y/N) :").strip().upper()
            if choice_yn == "Y":
                booking.remove(item)
                print("Đã xóa thành công .")
                return
            elif choice_yn == "N":
                print("Đã bỏ lựa chọn .")
                return
    print("Không tìm thấy mã !")

def share_room(booking):
    share = []
    choice_idname = input("Bạn muốn tìm kiém theo 1(mã bk) - 2(tên phòng) ? nhập 1 -2 : ").strip()
    if choice_idname == "1":
        input_ma = input("Nhập mã bk tìm kiếm :").strip().upper()
        for item in booking:
            if input_ma == item["id"]:
                share.append(item)
    elif choice_idname == "2":
        input_nameroom = input("Nhập tên phòng tìm kiếm :").strip().lower()
        for item in booking:
            if input_nameroom in item["name_room"].lower():
                share.append(item)
    else: 
        print("Nhập sai ! Bạn chỉ cần 1 hoặc 2 !")
        
    print(display_list(share))
            
def thongke_room(booking):
    count_n = 0
    count_t = 0
    count_d = 0
    count_q = 0
    for item in booking:
        if item["sum_time"] == "Ngắn":
            count_n += 1
        elif item["sum_time"] == "Tiêu chuẩn":
            count_t += 1
        elif item["sum_time"] == "Dài":
            count_d += 1
        else:
            count_q += 1
    print(f"Ngắn: {count_n} | Tiêu chuẩn: {count_t} | Dài: {count_d} | Quá tải: {count_q}")
while True:
    print(""" ======= Danh sách chức năng =======
        1. Hiển thị danh sách đặt lịch
        2. Đăng kí lịch đặt phòng mới 
        3. Cập nhật thông tin lịch hẹn
        4. Hủy lịch đặt phòng
        5. Tìm kiếm lịch đặt phòng
        6. Thống kê mật độ sử dụng 
        7. Thoát chương trình 
        """)
    
    print("="*40)
    choice = input("Nhập lựa chọn của bạn : ").strip()
    match (choice):
        case "1":
            display_list(list_booking)
        case "2":
            add_room(list_booking)
        case "3":
            update_room(list_booking)
        case "4":
            remove_room(list_booking)
        case "5":
            share_room(list_booking)
        case "6":
            thongke_room(list_booking)
        case "7":
            print("Đã thoát chương trình .")
            break
        case _:
            print("Vui lòng nhập 1 - 7 !")