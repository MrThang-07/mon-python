import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    datefmt='%Y-%m-%d %H:%M:%S'
)

def show_devices(device_list):
    if len(device_list) == 0:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    print("— DANH SÁCH THIẾT BỊ GIÁM SÁT —")
    print(f"{'MÃ TB':<6} | {'VỊ TRÍ PHÂN XƯỞNG':<25} | {'CHỈ SỐ CŨ':>10} | {'CHỈ SỐ MỚI':>10} | {'TRẠNG THÁI'}")
    print("-" * 75)
    
    for d in device_list:
        print(f"{d['id']:<6} | {d['location']:<25} | {d['old_index']:>10} | {d['new_index']:>10} | {d['status']}")

def update_indices(device_list):
    print("— CẬP NHẬT CHỈ SỐ ĐIỆN —")
    ma_tb = input("Nhập mã thiết bị: ").strip()
    
    thiet_bi_tim_thay = None
    for d in device_list:
        if d['id'] == ma_tb:
            thiet_bi_tim_thay = d
            break
            
    if thiet_bi_tim_thay is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống")
        return
        
    while True:
        try:
            chi_so_cu = int(input("Nhập chỉ số cũ: "))
            chi_so_moi = int(input("Nhập chỉ số mới: "))
            
            if chi_so_cu < 0 or chi_so_moi < 0:
                print("Lỗi: Chỉ số phải lớn hơn hoặc bằng 0. Vui lòng nhập lại!")
                continue
                
            if chi_so_moi < chi_so_cu:
                print("[Lỗi] (ERR-E02): Chỉ số mới không được nhỏ hơn chỉ số cũ. Vui lòng nhập lại!")
                continue
                
            thiet_bi_tim_thay['old_index'] = chi_so_cu
            thiet_bi_tim_thay['new_index'] = chi_so_moi
            print(f"[Thành công]: Thiết bị {ma_tb} đã được cập nhật số liệu mới")
            break
            
        except ValueError:
            print("Lỗi: Bạn phải nhập bằng số (không nhập chữ). Vui lòng nhập lại!")

def activate_warning(device_list):
    print("— KÍCH HOẠT TRẠNG THÁI CẢNH BÁO —")
    ma_tb = input("Nhập mã thiết bị cần duyệt: ").strip()
    
    for d in device_list:
        if d['id'] == ma_tb:
            tieu_thu = d['new_index'] - d['old_index']
            print(f"Tìm thấy thiết bị tại: {d['location']} (Lượng tiêu thụ: {tieu_thu} kWh)")
            
            if d['status'] == 'Overload':
                print("[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước!")
                return
                
            if tieu_thu > 5000:
                d['status'] = 'Overload'
                log_msg = f"[Cảnh báo]: Thiết bị {ma_tb} đã vượt ngưỡng tiêu thụ an toàn, chuyển sang OVERLOAD!"
                logging.warning(log_msg)
                print(f"[Thành công]: Thiết bị {ma_tb} đã được kích hoạt trạng thái OVERLOAD!")
            else:
                print("Thiết bị vẫn trong ngưỡng an toàn (<= 5000 kWh).")
            return
            
    print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống")

def calculate_energy_financials(device_list):
    tong_dien = 0
    for d in device_list:
        tong_dien += (d['new_index'] - d['old_index'])
        
    phan_tram_chiet_khau = 0
    if tong_dien >= 50000:
        phan_tram_chiet_khau = 3
        
    don_gia = 3000
    tong_tien = tong_dien * don_gia
    tien_sau_chiet_khau = tong_tien - (tong_tien * phan_tram_chiet_khau / 100)
    
    return (tong_dien, phan_tram_chiet_khau, tien_sau_chiet_khau)

def main():
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]

    while True:
        print("\nSMART ENERGY MONITOR - PHÒNG CƠ ĐIỆN")
        print("==========================================")
        print("1. Xem danh sách thiết bị giám sát")
        print("2. Cập nhật chỉ số điện tiêu thụ (Check-in)")
        print("3. Kích hoạt trạng thái cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí năng lượng")
        print("5. Thoát chương trình")
        print("==========================================")
        
        try:
            chon = int(input("Mời chọn chức năng (1-5): "))
            
            if chon == 1:
                show_devices(devices)
            elif chon == 2:
                update_indices(devices)
            elif chon == 3:
                activate_warning(devices)
            elif chon == 4:
                tong_dien, chiet_khau, tong_tien = calculate_energy_financials(devices)
                print("— BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG —")
                print(f"+ Tổng lượng điện tiêu thụ thực tế: {tong_dien:,} kWh")
                print(f"+ Tỷ lệ chiết khấu áp dụng từ nhà nước: {chiet_khau}%")
                print(f"+ Tổng chi phí năng lượng phải trả sau chiết khấu: {int(tong_tien):,} VND")
            elif chon == 5:
                print("Cảm ơn bạn đã sử dụng phần mềm Smart Energy Monitor!")
                print("[Chương trình kết thúc]")
                break
            else:
                print("Lỗi: Vui lòng chọn số từ 1 đến 5!")
                
        except ValueError:
            print("Lỗi: Bạn phải nhập bằng số. Xin vui lòng thử lại!")

if __name__ == "__main__":
    main()