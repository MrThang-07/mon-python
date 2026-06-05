list_parking = []
stt = 1
while True :
    print("""
          ===========================================
                QUẢN LÝ BÃI XE - SMART PARKING
          ===========================================
          1. Thêm xe mới vào bãi
          2. hiển thị danh sách xe trong bãi
          3. xóa xe khỏi bãi (khi xe ra )
          4. Thoát chương trình 
          ==========================================="""
          )
    choice = input("Nhập lựa chọn của bạn : ")
    match (choice):
        
        case "1":
            
            while True :
                loai_xe = input("Nhập loại xe :").strip()
                loai_xe = loai_xe.title()
                chu_xe = input("Nhập chủ xe : ").strip().upper()
                if loai_xe == "" or chu_xe == "":
                    print("Vui lòng nhập thông tin không để trống !")
                else:
                    break
            
            new_car = {"id": stt, "type": loai_xe, "owner": chu_xe}
            stt += 1
            list_parking.append(new_car)
            
            print("Thêm thành công !")
        case "2":
            if len(list_parking) == 0:
                print("Bãi xe hiện đang trống !")
            else:
                print(f"{'ID':<5}| {'Loai xe':<10}| {'Chu xe':<10}")
                print("-"*30)
                for item in list_parking:
                    print(f"{item["id"]:<5}| {item["type"]:<10}| {item["owner"]:<10}")
        case "3":
            found_cart = input("Nhập id cần xóa xe : ").strip()
            found = False
            found_cart = int(found_cart)
            for item in list_parking:
                if item["id"] == found_cart:
                    found = True
                    list_parking.remove(item)
                    print(f"Đã xóa xe ID {found_cart} thành công!")
                    break
            if not found:
                print("Không tìm thấy xe để xóa!")
        case "4":
            print("Đã thoát chương trình !")
            break
        case _:
            print("Vui lòng nhập 1 - 4 !")

