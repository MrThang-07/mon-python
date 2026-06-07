# (1) PHÂN TÍCH LỖI
# 1. Bản chất của biến total_points
# Biến total_points = 100 khai báo ở đầu chương trình là biến toàn cục (Global Variable)
# vì nó nằm ngoài tất cả các hàm, mọi nơi đều có quyền truy cập để đọc giá trị.
# 2. Nguyên nhân gây lỗi UnboundLocalError
# Cơ chế của Python: Trong hàm cũ xuất hiện phép gán: total_points = .... Quy tắc 
# của Python quy định: Bất kỳ biến nào bị thay đổi giá trị bằng phép gán = bên trong 
# hàm sẽ tự động bị coi là biến cục bộ (Local Variable) mới.
# (2) ĐỀ XUẤT GIẢI PHÁP
# Không dùng từ khóa global để can thiệp trực tiếp vào bộ nhớ ngoài
# (dễ gây lỗi dây chuyền khi hệ thống phình to).
# Thiết kế hàm cô lập bằng cách truyền dữ liệu qua tham số đầu vào 
# (điểm cũ, điểm thưởng) và dùng lệnh return để trả kết quả tổng điểm mới ra ngoài.
# # (3)Viết code 
# Biến lưu tổng điểm hiện tại của khách hàng ở chương trình chính
total_points = 100
def add_reward_points(current_points, points_earned):
    updated_points = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return updated_points


total_points = add_reward_points(total_points, 50)


print("Tổng điểm hiện tại của khách hàng:", total_points)