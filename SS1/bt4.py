# (1) Phân tích và Đề xuất giải pháp (Rút gọn)
    # 1. Phân tích Input / Output
        # Input (Mặc định là chuỗi str): ma_bn ("BN999"), nhiet_do_raw ("37.5"), nhip_tim_raw ("85").

        # Output mong muốn: * Nhiệt độ chuyển sang kiểu float (số thực).

        # Nhịp tim chuyển sang kiểu int (số nguyên).

        # Kiểm tra và hiển thị đúng nhãn <class 'float'> và <class 'int'>.

    # 2. Đề xuất 2 giải pháp ép kiểu (Type Casting)
        # Giải pháp 1 (Gián tiếp): Giữ nguyên biến chuỗi ban đầu, tạo thêm biến trung gian mới để lưu giá trị sau khi ép kiểu.

        # Giải pháp 2 (Trực tiếp): Lồng hàm ép kiểu float() và int() ngay bên ngoài hàm input() để ghi đè dữ liệu.

    # 3. Bảng so sánh giải pháp
        # Tiêu chí                   Giải pháp 1 (Biến trung gian)             Giải pháp 2 (Ép kiểu trực tiếp)
        # Bộ nhớ                     Tốn nhiều bộ nhớ hơn                      Tối ưu, ít tốn bộ nhớ hơn 
        # Độ gọn của code            Dài dòng                                  Ngắn gọn, tường minh
        # Khả năng                   dễ debugTốt hơn (giữ được dữ liệu thô)    Kém hơn (gặp lỗi sẽ crash ngay)


        # Chốt lựa chọn: Giải pháp 2 (Ép kiểu trực tiếp).
        # Lý do: Phù hợp với môi trường cấp cứu cần xử lý dữ liệu cực nhanh, code tối giản giúp hệ thống Monitor tiếp nhận sinh hiệu tức thì mà không bị trễ hoặc tốn tài nguyên bộ nhớ.
# (2) Triển khai mã nguồn Python
ma_bn = input("Nhập mã bệnh nhân: ").upper()
nhiet_do = float(input("Nhập nhiệt độ cơ thể: "))
nhip_tim = int(input("Nhập nhịp tim: "))

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {ma_bn}")

print(f"Nhiệt độ cơ thể: {nhiet_do} độ C")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}")

print(f"Nhịp tim: {nhip_tim} nhịp/phút")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}")

print("----------------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")