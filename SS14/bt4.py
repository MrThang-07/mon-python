# (1) PHÂN TÍCH TÀI LIỆU THIẾT KẾ HÀM 
# Hàm phụ trợ: calculate_average(student)
# Input: student (dict)
# Output: float (Điểm trung bình 3 môn)
#  Chức năng 1: display_grades(records)
# Input: records (list chứa các dict)
# Output: None (Chỉ in màn hình)
# Chức năng 2: update_student_score(records)
# Input: records (list chứa các dict)

# Output: None (Cập nhật trực tiếp vào danh sách)
# Chức năng 3: generate_report(records)
# Input: records (list chứa các dict)

# Output: None (Chỉ in màn hình)
# Chức năng 4: find_valedictorian(records)
# Input: records (list chứa các dict)

# Output: None (Chỉ in màn hình)
# (2) TRIỂN KHAI CODE PYTHON
student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def display_grades(records):
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    stt = 1
    for student in records:
        dtb = calculate_average(student)
        if dtb >= 8.0:
            hoc_luc = "Giỏi"
        elif dtb >= 6.5:
            hoc_luc = "Khá"
        elif dtb >= 5.0:
            hoc_luc = "Trung bình"
        else:
            hoc_luc = "Yếu (Cảnh báo đỏ)"
        print(f"{stt}. [{student['student_id']}] {student['name']:<15} | Toán: {student['math']:<4.1f} | Lý: {student['physics']:<4.1f} | Hóa: {student['chemistry']:<4.1f} | ĐTB: {dtb:.2f} - {hoc_luc}")
        stt += 1
    print("-" * 27)

def update_student_score(records):
    print("\n--- CẬP NHẬT ĐIỂM THI ---")
    ma_nhap = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    target_student = None
    for student in records:
        if student["student_id"] == ma_nhap:
            target_student = student
            break
    if target_student is None:
        print(f"Không tìm thấy sinh viên mang mã {ma_nhap} trong hệ thống!")
        return
    print(f"Đang sửa điểm cho sinh viên: {target_student['name']}")
    print("1-Toán, 2-Lý, 3-Hóa")
    while True:
        mon_choice = input("Chọn môn học (1-3): ").strip()
        if mon_choice in ["1", "2", "3"]:
            break
        print("Lựa chọn môn học không hợp lệ! Vui lòng chọn từ 1 đến 3.")
    if mon_choice == "1":
        key_mon = "math"
        ten_mon = "Toán"
    elif mon_choice == "2":
        key_mon = "physics"
        ten_mon = "Lý"
    else:
        key_mon = "chemistry"
        ten_mon = "Hóa"
    while True:
        try:
            diem_moi = float(input(f"Nhập điểm {ten_mon} mới: ").strip())
            if 0.0 <= diem_moi <= 10.0:
                break
            else:
                print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("[Lỗi]: Điểm số phải là một số thực hợp lệ. Vui lòng không nhập chữ!")
    target_student[key_mon] = diem_moi
    print(f">> Đã cập nhật điểm {ten_mon} của sinh viên '{target_student['name']}' thành {diem_moi:.1f}.")

def generate_report(records):
    print("\n--- BÁO CÁO HỌC VỤ ---")
    tong_sv = len(records)
    if tong_sv == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    qua_mon = 0
    truot_mon = 0
    for student in records:
        dtb = calculate_average(student)
        if dtb >= 5.0:
            qua_mon += 1
        else:
            truot_mon += 1
    ty_le_qua = (qua_mon / tong_sv) * 100
    ty_le_truot = (truot_mon / tong_sv) * 100
    print(f"Tổng số sinh viên: {tong_sv}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {qua_mon} sinh viên (Chiếm {ty_le_qua:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {truot_mon} sinh viên (Chiếm {ty_le_truot:.2f}%)")
    print("-" * 22)

def find_valedictorian(records):
    print("\n--- VINH DANH THỦ KHOA ---")
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    thu_khoa = records[0]
    max_dtb = calculate_average(thu_khoa)
    for student in records[1:]:
        dtb_hien_tai = calculate_average(student)
        if dtb_hien_tai > max_dtb:
            max_dtb = dtb_hien_tai
            thu_khoa = student
    print(f" Sinh viên: {thu_khoa['name']} (Mã: {thu_khoa['student_id']})")
    print(f" Điểm Trung Bình: {max_dtb:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("-" * 26)

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====
1. Xem bảng điểm và học lực
2. Cập nhật điểm thi sinh viên
3. Báo cáo thống kê (Đỗ/Trượt)
4. Tìm sinh viên Thủ khoa
5. Thoát chương trình
=======================================================""")
    choice = input("Chọn chức năng (1-5): ").strip()
    match choice:
        case "1":
            display_grades(student_records)
        case "2":
            update_student_score(student_records)
        case "3":
            generate_report(student_records)
        case "4":
            find_valedictorian(student_records)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        case _:
            print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5!")
    input("\nNhấn Enter để tiếp tục điều hướng...")