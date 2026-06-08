# (1) PHÂN TÍCH LỖI HỆ THỐNG
# 1. Bản chất của lỗi "Xuyên không" dữ liệu (Aliasing)
# Nguyên nhân: Dòng lệnh new_prescription = old_prescription thực chất không tạo ra một danh sách mới nào cả. Trong Python, List là một đối tượng có thể thay đổi (Mutable). Phép gán bằng dấu = chỉ đơn giản là tạo ra một cái nhãn mới (new_prescription) trỏ chung vào cùng một vùng nhớ với danh sách gốc (yesterday_prescription).

# Hậu quả: Vì hai biến dùng chung một "nhà kho" bộ nhớ, nên khi bạn gọi lệnh new_prescription.append("Oresol"), máy tính sẽ thêm thuốc thẳng vào vùng nhớ chung đó. Hệ quả là biến yesterday_prescription ở bên ngoài cũng bị thay đổi theo, làm sai lệch hoàn toàn dữ liệu lịch sử bệnh án.
# (2) SỬA CODE 

yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    new_prescription.append("Oresol")
    return new_prescription
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)