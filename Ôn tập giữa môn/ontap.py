
danh_sach_cau_thu = [
    {"ma": "CT001", "ten": "Nguyen Quang Hai", "so_tran": 10, "ban_thang": 5, "kien_tao": 4, "diem": 33, "phong_do": "Trụ cột đội bóng"},
    {"ma": "CT002", "ten": "Nguyen Van Toan", "so_tran": 12, "ban_thang": 12, "kien_tao": 6, "diem": 60, "phong_do": "Ngôi sao đẳng cấp"}
]

def nhap_so_hop_le(thong_bao, so_thap_nhat, so_cao_nhat):
    """Hàm gộp 1: Ép người dùng nhập đúng số trong khoảng yêu cầu"""
    while True:
        chuoi_nhap = input(thong_bao).strip()
        if chuoi_nhap.isdigit(): 
            so = int(chuoi_nhap)
            if so_thap_nhat <= so <= so_cao_nhat:
                return so # Đúng thì trả về con số và thoát hàm
        print(f"[Lỗi]: Vui lòng nhập số từ {so_thap_nhat} đến {so_cao_nhat}!")

def tinh_phong_do_tu_dong(so_tran, ban_thang, kien_tao):
    """Hàm gộp 2: Tính điểm hiệu suất và trả về (Điểm, Phong độ)"""
    diem = (so_tran * 1) + (ban_thang * 3) + (kien_tao * 2)
    
    if diem < 15:
        phong_do = "Cần thanh lý/Cho mượn"
    elif diem < 30:
        phong_do = "Dự bị chiến lược"
    elif diem < 50:
        phong_do = "Trụ cột đội bóng"
    else:
        phong_do = "Ngôi sao đẳng cấp"
        
    return diem, phong_do # Trả về một lúc 2 kết quả


# =====================================================================
# 6 CHỨC NĂNG CHÍNH CỦA ĐỀ BÀI
# =====================================================================

def chuc_nang_1_xem_danh_sach(danh_sach):
    """In danh sách dưới dạng bảng căn lề"""
    print("\n--- DANH SÁCH CẦU THỦ ---")
    if len(danh_sach) == 0:
        print("Danh sách đang trống!")
        return
        
    # In tiêu đề cột (Căn lề trái <)
    print(f"{'Mã CT':<7} | {'Họ và Tên Cầu Thủ':<20} | {'Số Trận':<7} | {'BànThắng':<8} | {'KiếnTạo':<7} | {'Điểm':<5} | Phong độ")
    print("-" * 85)
    for ct in danh_sach:
        print(f"{ct['ma']:<7} | {ct['ten']:<20} | {ct['so_tran']:<7} | {ct['ban_thang']:<8} | {ct['kien_tao']:<7} | {ct['diem']:<5} | {ct['phong_do']}")

def chuc_nang_2_them_moi():
    """Tiếp nhận cầu thủ mới"""
    print("\n--- TIẾP NHẬN CẦU THỦ MỚI ---")
    ma_moi = input("Nhập mã cầu thủ (Mã CT): ").strip().upper()
    if ma_moi == "":
        print("[Lỗi]: Không được để trống mã!")
        return
        
    # Kiểm tra trùng mã bằng vòng lặp cơ bản
    for ct in danh_sach_cau_thu:
        if ct["ma"] == ma_moi:
            print("[Lỗi]: Mã cầu thủ này đã tồn tại!")
            return
            
    ten_moi = input("Nhập họ và tên: ").strip().title()
    if ten_moi == "":
        print("[Lỗi]: Không được để trống tên!")
        return
        
    # Gọi hàm gộp nhập số siêu nhanh
    so_tran = nhap_so_hop_le("Nhập số trận (0-50): ", 0, 50)
    ban_thang = nhap_so_hop_le("Nhập số bàn thắng (>=0): ", 0, 100)
    kien_tao = nhap_so_hop_le("Nhập số kiến tạo (>=0): ", 0, 100)
    
    # Gọi hàm gộp tính điểm và phong độ
    diem, phong_do = tinh_phong_do_tu_dong(so_tran, ban_thang, kien_tao)
    
    # Tạo dictionary mới và nạp vào danh sách
    cau_thu_moi = {
        "ma": ma_moi, "ten": ten_moi, "so_tran": so_tran, 
        "ban_thang": ban_thang, "kien_tao": kien_tao, "diem": diem, "phong_do": phong_do
    }
    danh_sach_cau_thu.append(cau_thu_moi)
    print(">> Thêm cầu thủ thành công!")

def chuc_nang_3_cap_nhat():
    """Cập nhật lại chỉ số trận đấu, bàn thắng"""
    print("\n--- CẬP NHẬT CHỈ SỐ ---")
    ma_tim = input("Nhập Mã CT cần cập nhật: ").strip().upper()
    
    for ct in danh_sach_cau_thu:
        if ct["ma"] == ma_tim:
            print(f"Cầu thủ: {ct['ten']} | Phong độ cũ: {ct['phong_do']}")
            # Cho nhập lại các chỉ số mới
            ct["so_tran"] = nhap_so_hop_le("Nhập số trận mới (0-50): ", 0, 50)
            ct["ban_thang"] = nhap_so_hop_le("Nhập số bàn thắng mới (>=0): ", 0, 100)
            ct["kien_tao"] = nhap_so_hop_le("Nhập số kiến tạo mới (>=0): ", 0, 100)
            
            # Tính toán lại và cập nhật đè vào dictionary
            ct["diem"], ct["phong_do"] = tinh_phong_do_tu_dong(ct["so_tran"], ct["ban_thang"], ct["kien_tao"])
            print(">> Cập nhật thành công!")
            return
            
    print("[Lỗi]: Không tìm thấy mã cầu thủ này!")

def chuc_nang_4_xoa():
    """Xóa cầu thủ (Thanh lý hợp đồng)"""
    print("\n--- XÓA CẦU THỦ ---")
    ma_xoa = input("Nhập Mã CT cần xóa: ").strip().upper()
    
    for i in range(len(danh_sach_cau_thu)):
        if danh_sach_cau_thu[i]["ma"] == ma_xoa:
            xac_nhan = input(f"Bạn có chắc muốn xóa {danh_sach_cau_thu[i]['ten']}? (Y/N): ").strip().upper()
            if xac_nhan == "Y":
                danh_sach_cau_thu.pop(i) # Xóa phần tử tại vị trí i
                print(">> Đã xóa thành công!")
            return
            
    print("[Lỗi]: Không tìm thấy mã cầu thủ này!")

def chuc_nang_5_tim_kiem():
    """Tìm kiếm bằng vòng lặp và append cơ bản"""
    print("\n--- TÌM KIẾM CẦU THỦ ---")
    print("1. Tìm chính xác theo Mã CT\n2. Tìm gần đúng theo Tên")
    lua_chon = input("Chọn kiểu tìm (1-2): ").strip()
    
    ket_qua_tim_kiem = [] # Mảng rỗng để chứa các cầu thủ tìm thấy
    
    if lua_chon == "1":
        ma_tim = input("Nhập mã chính xác: ").strip().upper()
        for ct in danh_sach_cau_thu:
            if ct["ma"] == ma_tim:
                ket_qua_tim_kiem.append(ct)
                
    elif lua_chon == "2":
        ten_tim = input("Nhập tên cần tìm: ").strip().lower()
        for ct in danh_sach_cau_thu:
            if ten_tim in ct["ten"].lower(): # Không phân biệt hoa thường
                ket_qua_tim_kiem.append(ct)
                
    # Gọi lại hàm chức năng 1 để in cái mảng kết quả vừa tìm được ra dạng bảng
    chuc_nang_1_xem_danh_sach(ket_qua_tim_kiem)

def chuc_nang_6_thong_ke():
    """Đếm số lượng cầu thủ theo nhóm phong độ"""
    print("\n--- THỐNG KÊ PHONG ĐỘ ---")
    sao, cot, bi, ly = 0, 0, 0, 0
    
    for ct in danh_sach_cau_thu:
        if ct["phong_do"] == "Ngôi sao đẳng cấp":
            sao += 1
        elif ct["phong_do"] == "Trụ cột đội bóng":
            cot += 1
        elif ct["phong_do"] == "Dự bị chiến lược":
            bi += 1
            
    # Tính số người cần thanh lý bằng cách lấy tổng trừ đi 3 nhóm trên cho nhanh
    ly = len(danh_sach_cau_thu) - (sao + cot + bi)
    
    print(f"Ngôi sao: {sao} | Trụ cột: {cot} | Dự bị: {bi} | Thanh lý: {ly}")

while True:
    print("\n=== MENU QUẢN LÝ CẦU THỦ ===")
    print("1. Xem danh sách | 2. Thêm mới | 3. Cập nhật | 4. Xóa cầu thủ")
    print("5. Tìm kiếm      | 6. Thống kê | 7. Thoát")
    
    chon = input("Chọn chức năng (1-7): ").strip()
    
    match chon:
        case "1":
            chuc_nang_1_xem_danh_sach(danh_sach_cau_thu)
        case "2":
            chuc_nang_2_them_moi()
        case "3":
            chuc_nang_3_cap_nhat()
        case "4":
            chuc_nang_4_xoa()
        case "5":
            chuc_nang_5_tim_kiem()
        case "6":
            chuc_nang_6_thong_ke()
        case "7":
            print("Tạm biệt huấn luyện viên!")
            break
        case _:
            print("Lựa chọn sai, vui lòng nhập từ 1 đến 7!")
            
    input("\nNhấn Enter để quay lại Menu...")