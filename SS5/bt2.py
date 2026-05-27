# (1) Phân tích lỗi 
#     Nguyên nhân lỗi: Biến total_students = 0 đang bị đặt bên ngoài cả hai vòng lặp.
#     Điều này khiến nó biến thành biến tích lũy toàn cục, cộng dồn liên tục từ đầu đến 
#     cuối chương trình mà không bao giờ được đưa về 0 khi chuyển sang chi nhánh mới.

#     Quá trình dò luồng thực thi (Trace code):
#     Chi nhánh 1: * Ban đầu total_students = 0.
#         Cộng dồn 3 lớp của Chi nhánh 1: (0 + 30 + 25 + 28 = 83).
#         Kết quả hiển thị: 83 học viên -> ĐÚNG vì biến xuất phát từ 0.

#     Chi nhánh 2:Do không được reset, trước khi chạy Chi nhánh 2 thì total_students vẫn đang giữ giá trị cũ là 83.
#         Cộng dồn tiếp 3 lớp của Chi nhánh 2: (83 + 20 + 22 + 18 = 143).
#         Kết quả hiển thị: 143 học viên -> SAI (Lấy tổng CN1 + tổng CN2).

#     Chi nhánh 3:
#         Lúc này total_students tiếp tục giữ giá trị cũ là 143.
#         Cộng dồn tiếp 3 lớp của Chi nhánh 3:(143 + 35 + 32 + 30 = 240).
#         Kết quả hiển thị: 240 học viên -> SAI (Lấy tổng CN1 + CN2 + CN3).

# (2) Sửa lỗi
branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    

    total_students = 0

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")