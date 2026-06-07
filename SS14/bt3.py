# Khởi tạo dữ liệu hệ thống ban đầu
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_str):
    """Kiểm tra điểm số đầu vào có phải là số hợp lệ từ 0 đến 10 không."""
    # Bẫy lỗi nhập chuỗi không phải số bằng cách thử ép kiểu float
    # Vì chưa học try-except, ta kiểm tra thủ công bằng cách loại bỏ dấu chấm thập phân
    check_str = score_str.replace(".", "", 1)
    if not check_str.isdigit():
        return False
    
    score_float = float(score_str)
    if 0.0 <= score_float <= 10.0:
        return True
    return False

def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student  
    return None

def get_rank(average_score):
    """Quy đổi điểm trung bình sang chuỗi xếp loại học lực."""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def display_students(student_list):
    """Chức năng 1: Hiển thị danh sách toàn bộ học viên."""
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return
        
    stt = 1
    for item in student_list:
        print(f"{stt}. Mã: {item['student_id']} | Tên: {item['name']:<15} | Toán: {item['math_score']:<4} | Anh: {item['english_score']}")
        stt += 1

def add_student(student_list):
    """Chức năng 2: Thêm học viên mới vào hệ thống (có bẫy trùng mã, sai điểm)."""
    print("\n--- THÊM HỌC VIÊN MỚI ---")
    student_id = input("Nhập mã học viên: ").strip().upper()
    
    if student_id == "":
        print("[Lỗi]: Mã học viên không được để trống!")
        return
        
    # Gọi hàm phụ trợ kiểm tra trùng mã
    existing_student = find_student_by_id(student_list, student_id)
    if existing_student is not None:
        print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        return
        
    name = input("Nhập tên học viên: ").strip().title()
    if name == "":
        print("[Lỗi]: Tên học viên không được để trống!")
        return
        
    # Vòng lặp ép nhập đúng điểm Toán
    while True:
        math_str = input("Nhập điểm Toán (0-10): ").strip()
        if validate_score(math_str):
            math_score = float(math_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    # Vòng lặp ép nhập đúng điểm Tiếng Anh
    while True:
        english_str = input("Nhập điểm Tiếng Anh (0-10): ").strip()
        if validate_score(english_str):
            english_score = float(english_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")

def update_score(student_list):
    """Chức năng 3: Cập nhật điểm thi của học viên theo ID."""
    print("\n--- CẬP NHẬT ĐIỂM THI ---")
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    
    student = find_student_by_id(student_list, student_id)
    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
        
    print(f"Đang cập nhật điểm cho học viên: {student['name']}")
    
    while True:
        math_str = input("Nhập điểm Toán mới (0-10): ").strip()
        if validate_score(math_str):
            student["math_score"] = float(math_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    while True:
        english_str = input("Nhập điểm Tiếng Anh mới (0-10): ").strip()
        if validate_score(english_str):
            student["english_score"] = float(english_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    print("Cập nhật thông tin điểm thi thành công!")

def evaluate_students(student_list):
    """Chức năng 4: Đánh giá học lực dựa trên điểm trung bình."""
    print("\n--- BÁO CÁO ĐÁNH GIÁ HỌC LỰC ---")
    if len(student_list) == 0:
        print("Hệ thống chưa có dữ liệu học viên để đánh giá.")
        return
        
    for item in student_list:
        avg_score = (item["math_score"] + item["english_score"]) / 2
        rank = get_rank(avg_score)
        print(f"Mã: {item['student_id']} | Tên: {item['name']:<15} | ĐTB: {avg_score:<5} | Xếp loại: {rank}")


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====
1. Hiển thị danh sách học viên
2. Thêm học viên mới
3. Cập nhật điểm thi theo mã học viên
4. Đánh giá học lực của toàn bộ học viên
5. Thoát chương trình
    """)
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    match choice:
        case "1":
            display_students(students)
        case "2":
            add_student(students)
        case "3":
            update_score(students)
        case "4":
            evaluate_students(students)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            
    input("\nNhấn Enter để tiếp tục...")