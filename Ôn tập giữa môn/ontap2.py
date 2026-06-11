players = [
    {"id": "CT007","name":"Nguyễn Văn A","sotran": 10,"goat" : 10,"kientao": 20 ,"diemhieusuat": 30,"phongdo": "Ngôi sao đẳng cấp"},
    {"id": "CT005","name":"Trần Văn B","sotran": 30,"goat" : 50,"kientao": 40 ,"diemhieusuat": 60,"phongdo": "Cần thanh lý"}
]
def validate_phongdo(sotran,banthang,kientao):
    diem_player = (sotran * 1) + (banthang * 3) + (kientao * 2)
    if diem_player < 15:
        phongdo_player = "Cần thanh lý"
    elif diem_player < 30:
        phongdo_player = "Dự bị chiến lược"
    elif diem_player < 50:
        phongdo_player = "Trụ cột đội bóng"
    else:
        phongdo_player = "Ngôi sao đẳng cấp"
    return diem_player,phongdo_player

def validate_player(input_in,input_min,input_max):
    while True:
        input_player = input(input_in).strip()
        if len(input_player) == 0:
            print("Vui lòng không để trống !")
            continue
        if input_player.isdigit():
            input_player = int(input_player)
            if input_min <= input_player <= input_max:
                return input_player
        print(f"Vui lòng nhập nhập số nguyên từ {input_min} đến {input_max}")

def display_player(player):
    if len(player) == 0:
        print("Danh sách bị rỗng !")
        return
    print(f"{'ID':<5} | {'Họ và tên':<25} | {'Số trận':<15} | {'Bàn thắng':<15} | {'Kiến tạo':<15} | {'Điểm hiệu suất':<20} | {'Phân loại phong độ':25}")
    print("-"*120)
    for item in player:
        print(f"{item['id']:<5} | {item['name']:<25} | {item['sotran']:<15} | {item['goat']:<15} | {item['kientao']:<15} | {item['diemhieusuat']:<20} | {item['phongdo']:25}")

def add_player(player):
    add_id = input("Nhập mã cầu thủ : ").strip().upper()
    if len(add_id) == 0:
        print("Vui lòng không để trống !")
        return
    for item in player:
        if add_id == item["id"]:
            print("Mã cầu thủ đã bị trùng!")
            return
    add_name = input("Nhập tên cầu thủ : ").strip().title()
    if len(add_name) == 0:
        print("Vui lòng không để tên rỗng !")
        return
    add_sotran = validate_player("Vui lòng số trận đấu : ",0,50)
    add_banthang = validate_player("Vui lòng nhập số bàn thăng : ",0,10000)
    add_kientao = validate_player("Vui lòng nhập số kiến tạo : ",0,10000)
    diemhieusuat,phongdo = validate_phongdo(add_sotran,add_banthang,add_kientao)
    new_player = {"id": add_id,"name": add_name,"sotran": add_sotran,"goat" : add_banthang,"kientao": add_kientao ,"diemhieusuat": diemhieusuat,"phongdo": phongdo}
    players.append(new_player)
    print("Đã thêm mới thành công !")
def update_player(player):
    input_id = input("Nhập vào mã cầu thủ cần cập nhật : ").strip()
    if len(input_id) == 0:
        print("Vui lòng không để rỗng !")
        return
    for item in player:
        if input_id == item["id"]:
            item["sotran"] = validate_player("Vui lòng số trận đấu : ",0,50)
            item["goat"] = validate_player("Vui lòng nhập số bàn thăng : ",0,10000)
            item["kientao"] = validate_player("Vui lòng nhập số kiến tạo : ",0,10000)
            item["diemhieusuat"] , item["phongdo"] =validate_phongdo(item["sotran"],item["goat"],item["kientao"])
            print("Đã thêm cập nhật thành công .")
            return
    print("Không tìm thấy mã cầu thủ nào !")

def remove_player(player):
    input_id = input("Nhập vào mã cầu thủ cần cập nhật : ").strip().upper()
    if len(input_id) == 0:
        print("Vui lòng không để rỗng !")
        return
    for item in player:
        if input_id == item["id"]:
            input_yn = input("Bạn có chắc muốn xóa cầu thủ này khỏi danh sách không ? (Y/N) : ").strip().upper()
            if input_yn == "Y":
                player.remove(item)
                print("Đã xóa thành công.")
                return
            elif input_yn == "N":
                print("Đã hủy bỏ .")
                return
            else:
                return
    print("Không tìm thấy mã cầu thủ !")

def share_player(player):
    share = []
    input_player = input("Bạn muốn tìm kiếm theo 1-(theo Mã cầu thủ) hay 2-(theo họ tên) - (chọn 1/2) : ").strip()
    if input_player == "1":
        share_id = input("Vui lòng nhập mã cầu thủ : ").strip().upper()
        for item in player:
            if share_id == item["id"]:
                share.append(item)
    elif input_player == "2":
        share_name = input("Vui lòng nhập họ tên cầu thủ : ").strip().lower()
        for item in player:
            if share_name in item["name"].lower():
                share.append(item)
    display_player(share)

def count_player(player):
    count_ns = 0
    count_tc = 0
    count_db = 0
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
    print(f"Ngôi sao: {count_ns} | Trụ cột: {count_tc} | Dự bị : {count_db} | Cần thanh lý: {count_ctl}")

while True:
    print(""" ========= Danh sách chức năng =========
        1. Hiển thị danh sách cầu thủ
        2. Tiếp nhận cầu thủ mới
        3. Cập nhật thông tin và chỉ số
        4. Xóa cầu thủ (Thanh lý hợp đồng)
        5. Tìm kiếm cầu thủ
        6. Thống kê phân loại phong độ
        7. Thoát chương trình """  )
    print("="*40)
    choice = input("Nhập lựa chọn của bạn : ")
    match (choice):
        case "1":
            display_player(players)
        case "2":
            add_player(players)
        case "3":
            update_player(players)
        case "4":
            remove_player(players)
        case "5":
            share_player(players)
        case "6":
            count_player(players)
        case "7":
            print("Đã thoát chương trình .")
            break
        case _:
            print("Vui lòng nhập 1 - 7 !")
