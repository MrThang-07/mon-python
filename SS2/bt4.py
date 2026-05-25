# (1) Phân tích & Đề xuất giải pháp (Rút gọn)
    # 1. Phân tích Input / Output
    # Input (Số nguyên int): tuoi (tuổi), huyet_ap (huyết áp tâm thu), duong_huyet (đường huyết).

    # Output: * Dữ liệu âm: In "Dữ liệu nhập vào không hợp lệ" và dừng.

    # Đạt toàn bộ tiêu chí: In "ĐỦ ĐIỀU KIỆN PHẪU THUẬT".

    # Trượt tiêu chí: In "TỪ CHỐI PHẪU THUẬT" kèm lý do chi tiết.
    # 2. Bảng so sánh hai giải pháp
    # Tiêu chí                Giải pháp 1: Gộp điều kiện (and/or)                      Giải pháp 2: Điều kiện lồng nhau (Nested If)
    # Độ ngắn                 gọnCực kỳ ngắn gọn, ít dòng code.                        Dài hơn do phải chia nhiều tầng 
    # Độ phức tạp(Thụt lề)    Thấp (code thẳng hàng, dễ đọc lướt).                     Cao (nhiều cấp thụt lề thụt ra thụt vào).
    # Giá trị y khoa & UX     Kém. Chỉ báo chung chung là "Từ chối"                    Chỉ rõ bệnh nhân không đạt vì Tuổi, Huyết áp hay Đường huyết để bác sĩ xử lý.
    #                         chứ không biết bệnh nhân bị tạch ở chỉ số nào.Rất tốt.

    # Chốt lựa chọn: Chọn Giải pháp 2 (Điều kiện lồng nhau).

    # Lý do (Trade-off): Chấp nhận code dài hơn và thụt lề nhiều hơn (trade-off) để đổi lấy giá trị y khoa cao nhất
    # — cung cấp lý do từ chối chi tiết, giúp điều dưỡng biết ngay chỉ số nào của bệnh nhân đang vượt ngưỡng nguy hiểm để kịp thời cứu chữa.

# (2) Triển khai mã nguồn Python (Đơn giản, dễ hiểu)

print("--- HỆ THỐNG SÀNG LỌC ĐIỀU KIỆN PHẪU THUẬT ---")

# 1. Nhập dữ liệu đầu vào
tuoi = int(input("Nhập tuổi bệnh nhân: "))
huyet_ap = int(input("Nhập huyết áp tâm thu (mmHg): "))
duong_huyet = int(input("Nhập đường huyết (mg/dL): "))

# 2. Xử lý Edge Case: Chặn dữ liệu âm từ vòng ngoài
if tuoi < 0 or huyet_ap < 0 or duong_huyet < 0:
    print("\nLỖI: Dữ liệu nhập vào không hợp lệ!")

# 3. Tiến hành xét duyệt y khoa bằng cấu trúc lồng nhau (Giải pháp 2)
else:
    print("\n--- KẾT QUẢ SÀNG LỌC TIỀN PHẪU ---")
    
    # Kiểm tra điều kiện 1: Tuổi
    if tuoi < 75:
        # Kiểm tra tiếp điều kiện 2: Huyết áp (90 - 140)
        if 90 <= huyet_ap <= 140:
            # Kiểm tra nốt điều kiện 3: Đường huyết
            if duong_huyet < 150:
                print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
            else:
                print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
                print("- Lý do: Đường huyết cao vượt mức cho phép (>= 150 mg/dL).")
        else:
            print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
            print("- Lý do: Huyết áp tâm thu nằm ngoài khoảng an toàn (90 - 140 mmHg).")
    else:
        print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
        print("- Lý do: Bệnh nhân từ 75 tuổi trở lên (Nguy cơ biến chứng cao).")