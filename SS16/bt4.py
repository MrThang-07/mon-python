patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):
            return i
    return -1

def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return
    stt = 1
    for info_str in records:
        parts = info_str.split("-")
        print(f"{stt}. [{parts[0]}] {parts[1]:<15} | Năm sinh: {parts[2]} | Chẩn đoán: {parts[3]}")
        stt += 1
    print("-" * 74)

def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return
        
    name = input("Nhập tên bệnh nhân: ").replace("-", " ").strip().title()
    if name == "":
        print("Tên bệnh nhân không được để trống!")
        return
        
    while True:
        birth_year_str = input("Nhập năm sinh: ").strip()
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if 1900 <= birth_year <= 2026:
                break
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        
    diagnosis = input("Nhập chẩn đoán: ").replace("-", " ").strip().capitalize()
    if diagnosis == "":
        print("Chẩn đoán không được để trống!")
        return
        
    new_record = "-".join([patient_id, name, str(birth_year), diagnosis])
    records.append(new_record)
    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(new_record)

def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    index = find_patient_index(records, patient_id)
    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return
        
    parts = records[index].split("-")
    print(f"\nTìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    
    new_diag = input("Nhập chẩn đoán mới: ").replace("-", " ").strip().capitalize()
    if new_diag == "":
        print("Chẩn đoán mới không được để trống!")
        return
        
    parts[3] = new_diag
    records[index] = "-".join(parts)
    print("\nCập nhật chẩn đoán thành công!")

def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    tre_em = 0
    truong_thanh = 0
    cao_tuoi = 0
    
    for info_str in records:
        parts = info_str.split("-")
        age = 2026 - int(parts[2])
        if age < 16:
            tre_em += 1
        elif age <= 60:
            truong_thanh += 1
        else:
            cao_tuoi += 1
            
    print(f"Trẻ em: {tre_em} bệnh nhân")
    print(f"Trưởng thành: {truong_thanh} bệnh nhân")
    print(f"Người cao tuổi: {cao_tuoi} bệnh nhân")
    print("-" * 38)

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====
1. Xem danh sách hồ sơ bệnh án
2. Thêm hồ sơ bệnh nhân mới
3. Cập nhật chẩn đoán theo Mã BN
4. Báo cáo phân loại theo độ tuổi
5. Thoát chương trình
===================================================""")
    choice = input("Chọn chức năng (1-5): ").strip()
    match choice:
        case "1":
            display_records(patient_records)
        case "2":
            add_patient(patient_records)
        case "3":
            update_diagnosis(patient_records)
        case "4":
            generate_age_report(patient_records)
        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
    input("\nNhấn Enter để quay lại bảng điều khiển...")