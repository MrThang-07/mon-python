players =[
    {"id": "CT007" , "name": "Nguyen Quang Hai" , "sotran": 10 , "goat": 5 , "kientao": 4 ,"diem_hieusuat": 33, "phongdo": "Dự bị chiến lược"},
    {"id": "CT005" , "name": "Nguyen Quang Trung" , "sotran": 20 , "goat": 30 , "kientao": 10 ,"diem_hieusuat": 60, "phongdo": "Ngôi sao đẳng cấp"}
]
def validate_phongdo(sotran,banthang,kientao):
    phanloai = (sotran * 1) + (banthang * 3) + (kientao * 2)

    if phanloai < 15:
        phongdo_player = "Cần thanh lý"
    elif phanloai < 30:
        phongdo_player = "Dự bị chiến lược"
    elif phanloai < 50:
        phongdo_player = "Trụ cột đội bóng"
    else:
        phongdo_player = "Ngôi sao đẳng cấp"
    return phanloai,phongdo_player
def validate_player(input_player,min_input,max_input):
    while True:
        input_vl = input(input_player).strip()
        if not input_vl.isdigit():
            print("Vui lòng nhập số nguyên !")
            continue
        input_vl = int(input_vl)
        if min_input <= input_vl <= max_input:
            return int(input_vl)
        else:
            print(f"Vui lòng nhập từ {min_input} đến {max_input}")
            continue
def display_players(player):
    print("="*60)
    if len(player) == 0:
        print("Hiện tại danh sách cầu thủ không có thông tin nào !")
        return
    print(" Danh sách thông tin cầu thủ ")
    print(f"{'Mã cầu thủ':<10} |{'Họ và tên cầu thủ':<20} |{'Số trận thi đấu':<20} |{'Số bàn thắng':<20} |{'Số đường kiến tạo':<20} |{'Điểm hiệu suất':<20} |{'Phân loại phong độ':<20}")
    for item in player:
        print(f"{item['id']:<10} |{item['name']:<20} |{item['sotran']:<20} |{item['goat']:<20} |{item['kientao']:<20} |{item['diem_hieusuat']:<20} |{item['phongdo']:<20}")

def add_player(player):
    input_id = input("Nhập id cầu thủ cần thêm : ").strip().upper()
    if len(input_id) == 0:
        print("Mã cầu thủ không được để trống !")
        return
    for item in player:
        if input_id == item["id"]:
            print("Đã bị trùng id !")
            return
    input_name = input("Nhập tên cầu thủ : ").strip().title()
    if len(input_name) == 0:
        print("Vui lòng không để tên trống !")
        return
    input_sotran = validate_player("Nhập số trận đấu : ",0,50)
    input_banthang = validate_player("Nhập số bàn thắng : ",0,10000)
    input_kientao = validate_player("Nhập số kiến tạo : ",0,10000)
    diem_hieusuat,phanloai_phongdo = validate_phongdo(input_sotran,input_banthang,input_kientao)
    new_player ={"id": input_id , "name": input_name , "sotran": input_sotran , "goat": input_banthang, "kientao": input_kientao ,"diem_hieusuat": diem_hieusuat, "phongdo": phanloai_phongdo}
    players.append(new_player)
    print("Đã thêm thành công cầu thủ mới .")

def update_player(player):
    find_id = input("Nhập mã cầu thủ cần cập nhật : ").strip().upper()
    for item in player:
        if find_id == item["id"]:
            print(f" === Cập nhật cầu thủ {item['name']} ===")
            item["sotran"] = validate_player("Nhập số trận đấu : ",0,50)
            item["goat"] = validate_player("Nhập số bàn thắng : ",0,10000)
            item["kientao"] = validate_player("Nhập số kiến tạo : ",0,10000)
            item["diem_hieusuat"],item["phongdo"] = validate_phongdo(item["sotran"],item["goat"],item["kientao"])
            print("Đã cập nhật thành công ")
            return
    print("Không tìm thấy cầu thủ nào")
    return
def remove_player(player):
    input_id = input("Nhập id để xóa cầu thủ : ").strip().upper()
    for item in player:
        if input_id == item["id"]:
            choice_yn = input("Bạn có chắc muốn xóa cầu thủ này ra khỏi danh sách không? (Y/N)").strip().upper()
            if choice_yn == "Y":
                player.remove(item)
                print("Đã xóa cầu thủ này")
                return
            else:
                return
    print("Không tìm thấy cầu thủ !")
    return
def share_player(player):
    share =[]
    choice_idname = input("bạn muốn tìm kiếm cầu thủ bằng 1.(Mã cầu thủ) hay 2.(họ tên cầu thủ ) :").strip()
    if choice_idname == "1":
        find_id = input("Nhập id của cầu thủ : ").strip().upper()
        for item in player:
            if find_id == item["id"]:
                share.append(item)
    elif choice_idname == "2":
        find_name = input("Nhập tên của cầu thủ : ").strip().lower()
        for item in player:
            if find_name in item["name"].lower():
                share.append(item) 
    display_players(share)

def count(player):
    count_ns = 0
    count_db = 0
    count_tc = 0
    count_ctl = 0
    for item in player:
        if item["phongdo"] == "Cần thanh lý":
            count_ctl += 1
        elif item["phongdo"] == "Dự bị chiến lược":
            count_db += 1
        elif item["phongdo"] == "Trụ cột đội bóng":
            count_tc += 1
        else:
            count_ns += 1
    print(f"Ngôi sao: {count_ns} | Trụ cột: {count_tc} | Dự bị: {count_db} | Cần thanh lý: {count_ctl}")
while True:
    print("""======= DANH SÁCH CHỨC NĂNG =======
        1. Hiển thị danh sách cầu thủ  
        2. Tiếp nhận cầu thủ mới 
        3. Cập nhật thông tin và chỉ số 
        4. Xóa cầu thủ ( Thanh ý hợp đồng )
        5. Tìm kiếm cầu thủ 
        6. Thống kê phân loại phong độ 
        7. Đánh giá phong độ tự động 
        8. Thoát chương trình """)
    print("="*35)
    choice = input("Nhập lựa chọn của bạn : ")
    match (choice):
        case "1":
            display_players(players)
        case "2":
            add_player(players)
        case "3":
            update_player(players)
        case "4":
            remove_player(players)
        case "5":
            share_player(players)
        case "6":
            count(players)
        case "7":
            print("Chức năng đã làm .")
        case "8":
            print("Đã thoát chương trình .")
            break
        case _:
            print("Vui lòng nhập nhập 1 - 8 !")