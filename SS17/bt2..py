# Dữ liệu ban đầu (Mock data) mẫu để chạy thử chương trình
bus_records = [
    {
        "id": "CX001",
        "route": "Sài Gòn - Đà Lạt",
        "price": 300000,
        "available_seats": 5,
        "total_seats": 40,
        "revenue": 10500000,
        "status": "Hút khách"
    },
    {
        "id": "CX002",
        "route": "Hà Nội - Sầm Sơn",
        "price": 200000,
        "available_seats": 40,
        "total_seats": 40,
        "revenue": 0,
        "status": "Ế khách"
    }
]

def update_status(available, total):
    if available == 0:
        return "Hết vé"
    # Tính tỷ lệ phần trăm số ghế trống hiện tại so với tổng số ghế thiết kế
    rate = (available / total) * 100
    
    if rate < 15.0:
        return "Hút khách"
    elif rate <= 80.0:
        return "Bình thường"
    else:
        return "Ế khách"

def display_records(records):
    print("\n------------------------------------------- DANH SÁCH CHUYẾN XE -------------------------------------------")
    if len(records) == 0:
        print("Hệ thống hiện chưa có chuyến xe nào trong lịch trình.")
        return
    print(f"{'Mã CX':<8} | {'Tuyến Đường':<22} | {'Giá Vé':<12} | {'Ghế Trống':<10} | {'Tổng Ghế':<10} | {'Doanh Thu':<15} | {'Trạng Thái'}")
    print("-" * 107)
    for bus in records:
        print(f"{bus['id']:<8} | {bus['route']:<22} | {bus['price']:<12,} | {bus['available_seats']:<10} | {bus['total_seats']:<10} | {bus['revenue']:<15,} | {bus['status']}")
    print("-----------------------------------------------------------------------------------------------------------")

def add_bus(records):
    print("\n--- KHAI BÁO CHUYẾN XE MỚI ---")
    
    bus_id = input("Nhập mã chuyến xe (VD: CX004): ").strip().upper()
    if bus_id == "":
        print("[Lỗi]: Mã chuyến xe không được để trống!")
        return
    # Kiểm tra bẫy trùng mã chuyến xe
    for bus in records:
        if bus["id"] == bus_id:
            print("[Lỗi]: Mã chuyến xe này đã tồn tại trong hệ thống!")
            return
            
    route = input("Nhập tuyến đường (Điểm đi - Điểm đến): ").strip()
    if route == "":
        print("[Lỗi]: Tuyến đường không được để trống!")
        return
        
    # Nhập và ép kiểu kiểm tra Giá vé
    price_str = input("Nhập giá vé niêm yết (VNĐ): ").strip()
    if not price_str.isdigit():
        print("[Lỗi]: Giá vé phải là số nguyên dương!")
        return
    price = int(price_str)
    if price <= 0:
        print("[Lỗi]: Giá vé phải lớn hơn 0!")
        return
        
    # Nhập và ép kiểu kiểm tra Tổng số ghế
    total_str = input("Nhập tổng số ghế thiết kế (Sức chứa): ").strip()
    if not total_str.isdigit():
        print("[Lỗi]: Số ghế thiết kế phải là số nguyên dương!")
        return
    total_seats = int(total_str)
    if total_seats <= 0:
        print("[Lỗi]: Sức chứa của xe phải lớn hơn 0!")
        return
        
    # Các thông số tự động tính toán cho chuyến xe mới tinh
    available_seats = total_seats
    revenue = 0
    status = update_status(available_seats, total_seats)
    
    # Đóng gói dữ liệu vào Dictionary mới
    new_bus = {
        "id": bus_id,
        "route": route,
        "price": price,
        "available_seats": available_seats,
        "total_seats": total_seats,
        "revenue": revenue,
        "status": status
    }
    
    records.append(new_bus)
    print(f">> Khai báo thành công chuyến xe {bus_id} đi tuyến {route}!")

def book_ticket(records):
    print("\n--- CẬP NHẬT ĐẶT VÉ ---")
    if len(records) == 0:
        print("Hệ thống chưa có chuyến xe nào để thực hiện đặt vé.")
        return
        
    bus_id = input("Nhập mã chuyến xe muốn đặt vé: ").strip().upper()
    
    # Tìm kiếm chuyến xe mục tiêu
    target_bus = None
    for bus in records:
        if bus["id"] == bus_id:
            target_bus = bus
            break
            
    if target_bus is None:
        print(f"[Lỗi]: Không tìm thấy mã chuyến xe {bus_id} trong hệ thống!")
        return
        
    print(f"Chuyến xe: {target_bus['route']} | Số ghế trống hiện tại: {target_bus['available_seats']}")
    
    tickets_str = input("Nhập số lượng vé muốn mua: ").strip()
    if not tickets_str.isdigit():
        print("[Lỗi]: Số lượng vé đặt phải là một số nguyên dương!")
        return
        
    tickets_count = int(tickets_str)
    if tickets_count <= 0:
        print("[Lỗi]: Số lượng vé đặt phải lớn hơn 0!")
        return
        
    # Kiểm tra bẫy dữ liệu: Đặt vượt quá số ghế còn trống
    if tickets_count > target_bus["available_seats"]:
        print(f"[Lỗi]: Không đủ ghế! Số ghế trống hiện tại của xe chỉ còn {target_bus['available_seats']} ghế.")
        return
        
    # Tiến hành tính toán tự động và ghi đè cập nhật lại Dictionary dữ liệu
    target_bus["available_seats"] = target_bus["available_seats"] - tickets_count
    
    sold_seats = target_bus["total_seats"] - target_bus["available_seats"]
    target_bus["revenue"] = target_bus["price"] * sold_seats
    
    # Gọi hàm tự động cập nhật lại trạng thái lấp đầy mới
    target_bus["status"] = update_status(target_bus["available_seats"], target_bus["total_seats"])
    
    print(f">> Đặt vé thành công! Bạn đã mua {tickets_count} vé trên chuyến {bus_id}.")

def delete_bus(records):
    print("\n--- HỦY CHUYẾN XE KHỎI LỊCH TRÌNH ---")
    if len(records) == 0:
        print("Hệ thống chưa có chuyến xe nào để thực hiện hủy.")
        return
        
    bus_id = input("Nhập mã chuyến xe cần xóa khỏi lịch trình: ").strip().upper()
    
    target_index = -1
    for i in range(len(records)):
        if records[i]["id"] == bus_id:
            target_index = i
            break
            
    if target_index == -1:
        print(f"[Lỗi]: Không tìm thấy chuyến xe mang mã {bus_id} để xóa!")
        return
        
    print(f"Tìm thấy chuyến xe: {records[target_index]['id']} - {records[target_index]['route']}")
    confirm = input("Bạn có chắc muốn xóa chuyến xe này khỏi lịch trình không? (Y/N): ").strip().upper()
    
    if confirm == "Y":
        records.pop(target_index)
        print(f">> Đã xóa thành công chuyến xe {bus_id} ra khỏi hệ thống.")
    else:
        print(">> Hủy bỏ tác vụ xóa hồ sơ chuyến xe.")

def search_bus(records):
    print("\n--- TÌM KIẾM CHUYẾN XE ---")
    if len(records) == 0:
        print("Hệ thống không có dữ liệu chuyến xe để tìm kiếm.")
        return
        
    print("1. Tìm chính xác theo Mã Chuyến Xe")
    print("2. Tìm gần đúng theo Tuyến Đường")
    search_type = input("Chọn hình thức tìm kiếm (1-2): ").strip()
    
    results = []
    
    if search_type == "1":
        keyword = input("Nhập chính xác mã chuyến xe (VD: CX001): ").strip().upper()
        for bus in records:
            if bus["id"] == keyword:
                results.append(bus)
                
    elif search_type == "2":
        keyword = input("Nhập từ khóa tuyến đường cần tìm (VD: da lat): ").strip().lower()
        for bus in records:
            # lower() giúp tìm kiếm không phân biệt chữ hoa hay chữ thường
            if keyword in bus["route"].lower():
                results.append(bus)
    else:
        print("[Lỗi]: Lựa chọn hình thức không hợp lệ!")
        return
        
    # Hiển thị bảng kết quả tìm kiếm thu được
    print("\n--- KẾT QUẢ TÌM KIẾM ĐƯỢC ---")
    display_records(results)

def show_statistics(records):
    print("\n--- THỐNG KÊ TRẠNG THÁI CHUYẾN XE ---")
    
    count_het_ve = 0
    count_hut_khach = 0
    count_binh_thuong = 0
    count_e_khach = 0
    
    for bus in records:
        if bus["status"] == "Hết vé":
            count_het_ve += 1
        elif bus["status"] == "Hút khách":
            count_hut_khach += 1
        elif bus["status"] == "Bình thường":
            count_binh_thuong += 1
        elif bus["status"] == "Ế khách":
            count_e_khach += 1
            
    print(f"1. Số chuyến Hết vé      : {count_het_ve} chuyến")
    print(f"2. Số chuyến Hút khách   : {count_hut_khach} chuyến")
    print(f"3. Số chuyến Bình thường : {count_binh_thuong} chuyến")
    print(f"4. Số chuyến Ế khách     : {count_e_khach} chuyến")
    print(f"-> Tổng số lượng quản lý: {len(records)} chuyến xe.")
    print("-" * 38)

# VÒNG LẶP MENU ĐIỀU HƯỚNG TƯƠNG TÁC CHƯƠNG TRÌNH CHÍNH (CLI)
while True:
    print("""
========== HỆ THỐNG QUẢN LÝ CHUYẾN XE & ĐẶT VÉ ==========
1. Xem danh sách toàn bộ chuyến xe
2. Khai báo thêm chuyến xe mới
3. Cập nhật đặt vé chuyến xe
4. Hủy chuyến xe khỏi lịch trình
5. Tìm kiếm thông tin chuyến xe
6. Báo cáo thống kê trạng thái lấp đầy
7. Thoát chương trình
=========================================================""")
    
    choice = input("Vui lòng nhập lựa chọn chức năng (1-7): ").strip()
    
    if choice == "1":
        display_records(bus_records)
    elif choice == "2":
        add_bus(bus_records)
    elif choice == "3":
        book_ticket(bus_records)
    elif choice == "4":
        delete_bus(bus_records)
    elif choice == "5":
        search_bus(bus_records)
    elif choice == "6":
        show_statistics(bus_records)
    elif choice == "7":
        print("\nCảm ơn bạn đã sử dụng hệ thống quản lý nhà xe! Chúc một ngày tốt lành!")
        break 
    else:
        print("[Lỗi]: Lựa chọn không hợp lệ! Vui lòng nhập số chính xác từ 1 đến 7.")
        
    input("\nNhấn phím Enter để tiếp tục điều hướng về Menu chính...")