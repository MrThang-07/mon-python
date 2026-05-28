laptop_stock = 0
phone_stock = 0
tablet_stock = 0

while True:
    print("\n--- HỆ THỐNG QUẢN LÝ KHO ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    
    choice = input("Vui lòng chọn chức năng (1-5): ")
    
    if choice == "1":
        print("\n--- BÁO CÁO TỒN KHO VÀ BIỂU ĐỒ ---")
        
        print(f"Laptop ({laptop_stock}): ", end="")
        for i in range(laptop_stock):
            print("*", end="")
        print()
        
        print(f"Phone ({phone_stock}): ", end="")
        for i in range(phone_stock):
            print("*", end="")
        print()
        
        print(f"Tablet ({tablet_stock}): ", end="")
        for i in range(tablet_stock):
            print("*", end="")
        print()

    elif choice == "2":
        print("\n--- NHẬP KHO ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        item_choice = input("Chọn mặt hàng muốn nhập (1-3): ")
        
        if item_choice in ["1", "2", "3"]:
            while True:
                quantity = int(input("Nhập số lượng cần thêm: "))
                if quantity >= 0:
                    break
                else:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
            
            if item_choice == "1":
                laptop_stock += quantity
                print(f"Đã nhập thành công {quantity} Laptop.")
            elif item_choice == "2":
                phone_stock += quantity
                print(f"Đã nhập thành công {quantity} Phone.")
            elif item_choice == "3":
                tablet_stock += quantity
                print(f"Đã nhập thành công {quantity} Tablet.")
        else:
            print("Mặt hàng chọn không hợp lệ! Hủy thao tác nhập kho.")

    elif choice == "3":
        print("\n--- XUẤT KHO ---")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")
        item_choice = input("Chọn mặt hàng muốn xuất (1-3): ")
        
        if item_choice in ["1", "2", "3"]:
            while True:
                quantity = int(input("Nhập số lượng cần xuất: "))
                if quantity >= 0:
                    break
                else:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
            
            if item_choice == "1":
                if quantity <= laptop_stock:
                    laptop_stock -= quantity
                    print(f"Đã xuất thành công {quantity} Laptop.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
                    
            elif item_choice == "2":
                if quantity <= phone_stock:
                    phone_stock -= quantity
                    print(f"Đã xuất thành công {quantity} Phone.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
                    
            elif item_choice == "3":
                if quantity <= tablet_stock:
                    tablet_stock -= quantity
                    print(f"Đã xuất thành công {quantity} Tablet.")
                else:
                    print("Không đủ hàng! Giao dịch xuất kho bị hủy.")
        else:
            print("Mặt hàng chọn không hợp lệ! Hủy thao tác xuất kho.")

    elif choice == "4":
        print("\n--- KIỂM TRA CẢNH BÁO ---")
        so_mat_hang_sap_het = 0 
        
        if laptop_stock < 10:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop_stock} sản phẩm).")
            so_mat_hang_sap_het += 1
            
        if phone_stock < 10:
            print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {phone_stock} sản phẩm).")
            so_mat_hang_sap_het += 1
            
        if tablet_stock < 10:
            print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {tablet_stock} sản phẩm).")
            so_mat_hang_sap_het += 1
            
        if so_mat_hang_sap_het == 0:
            print("Tất cả các mặt hàng đều an toàn (>= 10 sản phẩm).")

    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống quản lý kho. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")