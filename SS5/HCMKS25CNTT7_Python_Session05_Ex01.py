# (1) Phân tích lỗi 
#     Nguyên nhân lỗi: Do đặt vòng lặp Tháng ở ngoài, Chi nhánh ở trong. Theo nguyên lý vòng lặp lồng nhau, chương trình sẽ bị cố định 
#     ở Tháng 1 -> duyệt qua hết Chi nhánh 1, 2, 3 -> rồi mới đổi sang Tháng 2. Dẫn đến dữ liệu bị gom cụm theo tháng, sai lệch nghiệp vụ.
#     Vòng lặp ngoài: Phải duyệt theo Chi nhánh (branch).
#     Vòng lặp trong: Phải duyệt theo Tháng (month).
# (2) Sửa lỗi 

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3


result = ""


for branch in range(1, branch_count + 1):
    print(f"\n--- Nhập dữ liệu cho Chi nhánh {branch} ---")
    
 
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        

        result += f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"

print("\n-------------- Kết quả --------------")
print(result)