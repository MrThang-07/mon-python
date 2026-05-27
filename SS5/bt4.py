# (1) Phân tích và thiết kế giải pháp 
#     1. Phân tích Input / Output
#         Input:

#         branch_count: Số lượng chi nhánh cần kiểm tra (Số nguyên int).

#         student_count: Số học viên đi học của từng lớp (Số nguyên int).

#         Output: Trạng thái của từng lớp học sau khi nhập liệu (Chuỗi văn bản str).

#     2. Đề xuất giải pháp & Xử lý Edge Cases
#         Vòng lặp: Dùng 2 vòng lặp for lồng nhau. Vòng ngoài duyệt qua từng chi nhánh. Vòng trong chạy cố định 2 lần ứng với 2 lớp học của chi nhánh đó.

#         Xử lý Bẫy 1 (Số âm): Dùng vòng lặp while True để bắt người dùng nhập lại liên tục nếu student_count < 0, cho đến khi nhập số hợp lệ mới thoát ra.

#         Xử lý Bẫy 2 (Sĩ số bằng 0): Dùng if student_count == 0 để in thông báo bỏ qua và dùng lệnh continue sang lớp tiếp theo.

#         Đánh giá trạng thái: Sử dụng cấu trúc if-else cơ bản (>= 20: ổn định; < 20: nhắc nhở).

#     3. Thiết kế thuật toán 
#         Plaintext
#         Nhập branch_count
#         Vòng lặp branch chạy từ 1 đến branch_count:
#             Vòng lặp classroom chạy từ 1 đến 2:
#                 Vòng lặp while True (Bẫy 1 - Nhập lại nếu số học viên < 0):
#                     Nhập student_count
#                     Nếu student_count >= 0: Thoát vòng lặp while
#                     Ngược lại: In thông báo lỗi và yêu cầu nhập lại
#                 Nếu student_count == 0 (Bẫy 2):
#                     In "Lớp vắng toàn bộ..." -> Sang lớp tiếp theo (continue)
#                 Nếu student_count >= 20: 
#                     In "Lớp học ổn định"
#                 Ngược lại (< 20): 
#                     In "Lớp cần được nhắc nhở theo dõi"
# (2) Triển khai mã nguồn Python cơ bản, dễ hiểu

branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\n--- Chi nhánh {branch} ---")
 
    for classroom in range(1, 3):
    
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))
            
            if student_count >= 0:
                break 
            else:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")

        
        if student_count == 0:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue 
            
        
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")

print("\n--- Hoàn thành kiểm tra sĩ số ---")