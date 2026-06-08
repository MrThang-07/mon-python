patients = [
	["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
	["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]
def display_patients(patient_list):
    if len(patient_list) == 0 :
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    else:
        stt = 1 
        print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
        for item in patient_list:
            print(f"{stt}. Mã: {item[0]} | Tên: {item[1]:<15} | Giới tính: {item[2]:<5} | Bệnh: {item[3]:<10}")
            stt += 1


def find_patient_index(input_idpatients,patient_list):
    while True:
        found = False
        ma_id = input(input_idpatients).strip().upper()
        if len(ma_id) == 0:
            print("Mã bệnh nhân không được để trống!")
            continue
        for item in patient_list:
                if ma_id == item[0]:
                    found = True
                    print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
                    break
        if not found :
            return ma_id
            continue
def validate_gender(input_genderpatients):
    found = False
    while True:
        new_gender = input(input_genderpatients).strip().lower()
        if len(new_gender) == 0:
                print("Giới tính bệnh nhân không được để trống!")
                continue
        if new_gender == "nam" or new_gender == "nu":
            found = True
            return new_gender
            break
        if not found:
            print("Giới tính không hợp lệ, vui lòng nhập lại!")
            continue

        
def add_patient(patient_list):
    input_id = find_patient_index("Nhập mã bệnh nhân: ",patients)
    input_name = input("Nhập tên bệnh nhân : ").strip().title()
    if len(input_name) == 0 or " ":
        print("Tên bệnh nhân không được để trống!")
    else:
        input_gender = validate_gender("Nhập giới tính bệnh nhân: ")
        input_chuandoan = input("Nhập chuẩn đoán bệnh :").strip().title()
        if len(input_chuandoan) == 0 or " ":
            print("Chuẩn đoán không được rỗng")
        else:
            new_list =[input_id,input_name,input_gender,input_chuandoan]
            patients.append(new_list)
            print("Tiếp nhận bệnh nhân thành công!")

def find_patient_index(patient_list, patient_id):
    update_id = input(patient_id).strip().upper()
    if len(update_id) == 0 or " ":
        print("Không được phép nhập rỗng !")
    find = -1 
    for i,value in enumerate(patient_list,start = 0):
        if value[0] == update_id:
            find = i
            break
        else:
            find = -1 
    if find == -1 :
        print(f"Không tìm thấy hồ sơ mang mã [{update_id}]]!")
        return
    else:
        print(f"Chuẩn đoán hiện tại: {patient_list[find][3]}")
        new_chuandoan = input("Nhập chuẩn đoán mới:" ).strip().title()
        if len(new_chuandoan) == 0 or " ":
            print("Chuẩn đoán không được rỗng")
        else:
            patient_list[find][3] = new_chuandoan
            print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    stt = 1
    found = False
    find_benh = input("Nhập từ khóa tên bệnh : ").strip().lower()
    if len(find_benh) == 0 :
        print("Kết quả tìm kiếm: ")
    for item in patient_list:
        if find_benh in item[3].lower():
            found = True
            print(f"{stt}. Mã: {item[0]} | Tên: {item[1]:<15} | Giới tính: {item[2]:<5} | Bệnh: {item[3]:<10}")
            stt += 1
    if not found:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    print(f"Có tổng cộng {stt - 1} bệnh nhân mắc bệnh liên quan đến {find_benh}")




while True :
    print("""===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====
        1. Hiển thị danh sách bệnh nhân
        2. Tiếp nhận bệnh nhân mới
        3. Cập nhật chẩn đoán bệnh theo mã BN
        4. Tìm kiếm và thống kê theo tên bệnh
        5. Thoát chương trình
==============================================
        """)
    choice = input("Nhập lựa chọn của bạn: ")
    match (choice):
        case "1":
            display_patients(patients)
        case "2":
            add_patient(patients)
        case "3":
            find_ma =  find_patient_index(patients, "Nhập mã bệnh nhân cần cập nhật chẩn đoán bệnh : ")
        case "4":
            search_by_disease(patients)
        case "5":
            print("Đã thoát chương trình ")
            break
        case _:
            print("Vui lòng nhập 1 - 5 !")