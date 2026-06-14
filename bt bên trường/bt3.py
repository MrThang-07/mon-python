
students = ["An", "Bình", "Cường"]

while True:
    print("\nHỆ THỐNG QUẢN LÝ DANH SÁCH SINH VIÊN")
    print("STUDENT MANAGER")
    print("1. THÊM SINH VIÊN")
    print("2. HIỂN THỊ DANH SÁCH")
    print("3. TÌM SINH VIÊN")
    print("4. SỬA SINH VIÊN")
    print("5. XÓA SINH VIÊN")
    print("6. THOÁT")
    
    chon = input("Nhập lựa chọn của bạn (1-6): ")
    
    if chon == "1":
        ten_moi = input("Nhập tên sinh viên cần thêm: ")
        students.append(ten_moi)  
        print(" Đã thêm thành công!")
        
    elif chon == "2":
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for ten in students:
            print("-", ten)
            
    elif chon == "3":
        ten_tim = input("Nhập tên sinh viên cần tìm: ")
        if ten_tim in students:   
            print("CÓ sinh viên", ten_tim, "trong danh sách.")
        else:
            print("=> KHÔNG tìm thấy sinh viên này.")
            
    elif chon == "4":
        ten_cu = input("Nhập tên sinh viên cần sửa: ")
        
        if ten_cu in students:
            ten_moi = input("Nhập tên mới: ")
            
            
            for i in range(len(students)):
                if students[i] == ten_cu:  
                    students[i] = ten_moi  
                    break                  
                    
            print("Đã sửa xong!")
        else:
            print("=> Không tìm thấy sinh viên này!")
            
    elif chon == "5":
        ten_xoa = input("Nhập tên sinh viên muốn xóa: ")
        if ten_xoa in students:
            students.remove(ten_xoa)  
            print("=> Đã xóa thành công!")
        else:
            print("=> KHÔNG tìm thấy sinh viên này để xóa.")
            
    elif chon == "6":
        print("=> Đã thoát chương trình. Tạm biệt!")
        break  
        
    else:
        print("=> Lựa chọn sai, vui lòng nhập số từ 1 đến 6!")