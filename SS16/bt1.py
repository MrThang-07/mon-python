# (1) PHÂN TÍCH LỖI (Vấn đề hiện tại)
# 1. Tính bất biến (Immutable) của String
# Thực trạng: Hai dòng lệnh raw_diagnosis.strip() và raw_diagnosis.title() trong code cũ không có tác dụng vì String trong Python là kiểu dữ liệu bất biến. Các phương thức xử lý chuỗi chỉ tính toán và sinh ra một chuỗi mới ở vùng nhớ tạm thời chứ không thể ghi đè trực tiếp lên chuỗi gốc.

# Cách sửa: Cần phải gán kết quả trả về ngược lại vào biến để lưu trữ giá trị mới. Bạn đã sửa rất chuẩn bằng cú pháp: raw_diagnosis = raw_diagnosis.strip().title() (Kỹ thuật nối phương thức - Method Chaining).

# 2. Sai lầm khi dùng extend() thay vì append()
# Thực trạng: Khi truyền một String vào phương thức extend(), Python coi String đó là một tập hợp (iterable) gồm nhiều ký tự độc lập. extend() sẽ bẻ gãy chuỗi ra và nhồi từng ký tự rải rác 'v', 'i', 'E', 'm',... cùng các dấu cách vào list dưới dạng các phần tử riêng biệt.

# Cách sửa: Để đưa nguyên vẹn cả một cụm từ (coi cả chuỗi là một phần tử duy nhất) vào danh sách, ta bắt buộc phải dùng phương thức append(). Bạn đổi sang current_list.append(raw_diagnosis) là hoàn toàn chính xác.

# (2) Sửa code :
patient_diagnoses = ["Sốt Xuất Huyết"]
def add_diagnosis(raw_diagnosis, current_list):
    
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list


new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)