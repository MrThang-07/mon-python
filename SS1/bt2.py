# 1. Phân Tích Lỗi 

# Dò luồng thực thi (Trace code): Khi điều dưỡng nhập dữ liệu 65.5, giá trị này được gán thẳng vào biến weight.
# Khi dùng hàm type(weight) để kiểm tra, hệ thống trả về kiểu dữ liệu là <class 'str'> (chuỗi ký tự).

# Đặc điểm hàm input(): Mặc định trong Python, hàm input() luôn luôn trả về dữ liệu dưới dạng chuỗi ký tự (str),
# cho dù người dùng có gõ vào là một con số.

# Nguyên nhân gây lỗi: Do mã nguồn cũ trực tiếp gán hàm input() vào biến weight mà không thực hiện ép kiểu (Type Casting) sang số thực. 
# Hệ thống lưu trữ sai kiểu dữ liệu khiến các công thức toán học (như tính BMI) ở phía sau không thể thực hiện được.

# 2. Mã Nguồn Sửa Lỗi 
print("--- Hệ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : " , name_patient)
print("Cân nặng đã nhập : " , weight)
# Trưởng nhóm IT kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO - Kiểu dữ liệu dạng đang lưu là : ", type(weight))