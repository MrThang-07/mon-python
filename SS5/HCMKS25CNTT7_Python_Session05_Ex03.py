# 1. Phân tích lỗi 
#     Vấn đề: Khi gặp phòng quá lớn (row_count > 10 hoặc seat_count > 10), đoạn code của bạn đang dùng lệnh break.

#     Hậu quả: Lệnh break này chỉ thoát ra khỏi vòng lặp nhập phòng (for room...), 
#     chương trình vẫn sẽ chạy tiếp các câu lệnh nằm ngoài vòng lặp (nếu có) chứ chưa dừng 
#     hẳn toàn bộ chương trình ngay lập tức.

# 2. (2) Triển khai code
room_count = int(input("Nhập số lượng phòng học: "))
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, room_count + 1):
        print(f"Phòng học {room}")
        row_count = int(input("Nhập số hàng ghế: "))
        seat_count = int(input("Nhập số ghế mỗi hàng: "))
        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        print("\nSơ đồ chỗ ngồi:")
        for row in range(row_count):
            for seat in range(seat_count):
                print("*", end=" ")
            print()