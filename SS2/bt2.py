# (1) Phân tích lỗi (Bug Analysis)
    # 1. Toán tử logic bị sử dụng sai
        # Hệ thống hiện tại đang sử dụng sai toán tử or (Hoặc) thay vì phải dùng toán tử and (Và).
    # 2. Dò luồng thực thi (Trace code) với donor_age = 16, donor_weight = 55
        # Kiểm tra điều kiện if donor_age >= 18 or donor_weight >= 50:
        # Nhánh 1: 16 >= 18 -> Sai (False).Nhánh 2: 55 >= 50 -> Đúng (True).
        # Do dùng toán tử or, chỉ cần một trong hai nhánh đúng là toàn bộ điều kiện sẽ Đúng (True).
        # Do đó, hệ thống duyệt sai cho học sinh 16 tuổi hiến máu.
    # 3. Phân biệt and và or
        # Toán tử and: Chỉ trả về True khi tất cả các điều kiện đều đúng. (Bắt buộc thỏa mãn đồng thời).

        # Toán tử or: Trả về True nếu có ít nhất một điều kiện đúng. (Chỉ cần một trong các yếu tố thỏa mãn).
# (2) Sửa lỗi
print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    
    if donor_age < 18:
        print("- Reason: Under 18 years old.")
    if donor_weight < 50:
        print("- Reason: Under 50 kg.")