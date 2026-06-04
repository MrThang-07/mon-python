parking_lot = [
    {
        "id": 1,
        "plate": "29A-12345",
        "type": 1,
        "entry_time": 8
    },
    {
        "id": 2,
        "plate": "30B-99999",
        "type": 2,
        "entry_time": 9
    }
]

next_id = 3

while True:
    print("""
    ========================================================
                   QUẢN LÝ BÃI XE - SMART PARKING
    ========================================================
    1. Check-in (Đăng ký xe vào)
    2. Báo cáo tồn kho (Hiển thị danh sách)
    3. Tìm kiếm xe (Theo biển số)
    4. Check-out (Xử lý xe ra & Tính phí)
    5. Thoát chương trình
    ========================================================""")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    match choice:
        case "1":
            print("\n--- CHỨC NĂNG: CHECK-IN ---")
            plate_input = input("Nhập biển số xe: ").strip().upper()
            
            if plate_input == "":
                print("[Lỗi]: Biển số xe không được để trống!")
                continue
                
            is_duplicate = False
            for vehicle in parking_lot:
                if vehicle["plate"] == plate_input:
                    is_duplicate = True
                    break
                    
            if is_duplicate:
                print(f"ERR-01 - [Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
                continue
                
            while True:
                type_str = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
                if type_str == "1" or type_str == "2":
                    type_vehicle = int(type_str)
                    break
                else:
                    print(f"ERR-02 - [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                    
            while True:
                entry_str = input("Nhập giờ vào bãi (0-24): ").strip()
                if entry_str.isdigit():
                    entry_time = int(entry_str)
                    if 0 <= entry_time <= 24:
                        break
                print("[Lỗi]: Giờ vào không hợp lệ! Vui lòng nhập số nguyên từ 0 đến 24.")
                
            new_vehicle = {
                "id": next_id,
                "plate": plate_input,
                "type": type_vehicle,
                "entry_time": entry_time
            }
            parking_lot.append(new_vehicle)
            print(f"[Thành công]: Xe {plate_input} đã được đăng ký vào bãi (ID: {next_id}).")
            next_id += 1
            
        case "2":
            print("\n--- CHI TIẾT BÃI XE ---")
            if len(parking_lot) == 0:
                print("[Thông báo: Bãi xe hiện đang trống!]")
            else:
                print(f"{'ID':<5} | {'Biển số xe':<15} | {'Loại xe':<10} | {'Giờ vào':<8}")
                print("-" * 50)
                for vehicle in parking_lot:
                    text_type = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
                    print(f"{vehicle['id']:<5} | {vehicle['plate']:<15} | {text_type:<10} | {vehicle['entry_time']:<8}")
                print("-" * 50)
                
        case "3":
            print("\n--- CHỨC NĂNG: TÌM KIẾM XE ---")
            plate_input = input("Nhập biển số xe cần tìm: ").strip().upper()
            
            found = False
            for vehicle in parking_lot:
                if vehicle["plate"] == plate_input:
                    found = True
                    print(f"Thông tin chi tiết: {vehicle}")
                    break
                    
            if not found:
                print(f"ERR-04 - [Lỗi]: Không tìm thấy biển số {plate_input} trong hệ thống!")
                
        case "4":
            print("\n--- CHỨC NĂNG: CHECK-OUT ---")
            plate_input = input("Nhập biển số xe cần ra: ").strip().upper()
            
            target_vehicle = None
            for vehicle in parking_lot:
                if vehicle["plate"] == plate_input:
                    target_vehicle = vehicle
                    break
                    
            if target_vehicle is None:
                print(f"ERR-04 - [Lỗi]: Không tìm thấy biển số {plate_input} trong hệ thống!")
                continue
                
            while True:
                exit_str = input("Nhập giờ ra: ").strip()
                if exit_str.isdigit():
                    exit_time = int(exit_str)
                    if 0 <= exit_time <= 24:
                        if exit_time >= target_vehicle["entry_time"]:
                            break
                        else:
                            print("ERR-03 - [Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                            continue
                print("[Lỗi]: Giờ ra không hợp lệ! Vui lòng nhập số nguyên từ 0 đến 24.")
                
            duration = exit_time - target_vehicle["entry_time"]
            if duration == 0:
                duration = 1
                
            unit_price = 5000 if target_vehicle["type"] == 1 else 30000
            total_fee = duration * unit_price
            
            print(f"Tổng phí phải trả: {total_fee} VNĐ")
            parking_lot.remove(target_vehicle)
            print(f"[Thành công]: Đã xóa xe ID {target_vehicle['id']} thành công!")
            
        case "5":
            print("\nThoát chương trình. Hẹn gặp lại!")
            break
            
        case _:
            print("ERR-05 - [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
            
    input("\nNhấn Enter để tiếp tục...")