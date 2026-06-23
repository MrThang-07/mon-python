class Student:
    def __init__(self, student_id, name, theory_score, practice_score, project_score):
        self.id = student_id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0.0
        self.academic_rank = ""
        self.update_academic_info()
    def calculate_final_score(self):
        self.final_score = (self.theory_score * 0.2) + (self.practice_score * 0.3) + (self.project_score * 0.5)
    def classify_academic_rank(self):
        if self.final_score < 5.0:
            self.academic_rank = "Yếu"
        elif self.final_score < 7.0:
            self.academic_rank = "Trung bình"
        elif self.final_score < 8.5:
            self.academic_rank = "Khá"
        else:
            self.academic_rank = "Giỏi"  
    def update_academic_info(self):
        self.calculate_final_score()
        self.classify_academic_rank()

class StudentManager:
    def __init__(self):
        self.students = []
    def is_id_exist(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return True
        return False
    def input_score(self, prompt_text):
        while True:
            try:
                score = float(input(prompt_text).strip())
                if 0.0 <= score <= 10.0:
                    return score
                else:
                    print(">> Lỗi: Điểm phải nằm trong khoảng từ 0.0 đến 10.0!")
            except ValueError:
                print(">> Lỗi: Vui lòng nhập đúng định dạng số!")

    def show_all(self):
        """Chức năng 1: Hiển thị danh sách sinh viên"""
        if not self.students:
            print(">> Danh sách sinh viên hiện đang trống.")
            return
        print("-" * 105)
        print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Lý Thuyết':<10} | {'Thực Hành':<10} | {'Đồ Án':<10} | {'Tổng Kết':<10} | {'Học Lực':<10}")
        print("-" * 105)
        for s in self.students:
            print(f"{s.id:<10} | {s.name:<20} | {s.theory_score:<10.1f} | {s.practice_score:<10.1f} | {s.project_score:<10.1f} | {s.final_score:<10.2f} | {s.academic_rank:<10}")
        print("-" * 105)
    def add_student(self):
        """Chức năng 2: Thêm sinh viên mới"""
        print("\n--- THÊM SINH VIÊN MỚI ---")
        while True:
            student_id = input("Nhập Mã SV: ").strip()
            if not student_id:
                print(">> Lỗi: Mã SV không được để rỗng!")
                continue
            if self.is_id_exist(student_id):
                print(">> Lỗi: Mã SV đã tồn tại trong hệ thống!")
                continue
            break
        while True:
            name = input("Nhập Họ tên: ").strip()
            if not name:
                print(">> Lỗi: Họ tên không được để rỗng!")
                continue
            break
        theory = self.input_score("Nhập Điểm Lý thuyết (0-10): ")
        practice = self.input_score("Nhập Điểm Thực hành (0-10): ")
        project = self.input_score("Nhập Điểm Đồ án (0-10): ")
        new_student = Student(student_id, name, theory, practice, project)
        self.students.append(new_student)
        print(f">> Thành công: Đã thêm sinh viên {name} vào hệ thống!")

    def update_student(self):
        print("\n--- CẬP NHẬT ĐIỂM SINH VIÊN ---")
        student_id = input("Nhập Mã SV cần cập nhật: ").strip()
        
        for s in self.students:
            if s.id == student_id:
                print(f"Đang cập nhật thông tin cho sinh viên: {s.name}")
                s.theory_score = self.input_score("Nhập Điểm Lý thuyết mới: ")
                s.practice_score = self.input_score("Nhập Điểm Thực hành mới: ")
                s.project_score = self.input_score("Nhập Điểm Đồ án mới: ")

                s.update_academic_info()
                print(">> Thành công: Đã cập nhật điểm và xét lại học lực!")
                return  
        print(">> Lỗi: Không tồn tại mã sinh viên này trong hệ thống!")

    def delete_student(self):
        print("\n--- XÓA SINH VIÊN ---")
        student_id = input("Nhập Mã SV cần xóa: ").strip()
        for s in self.students:  
            if s.id == student_id:
                confirm = input(f"Bạn có chắc muốn xóa sinh viên '{s.name}' không? (Y/N): ").strip().lower()
                if confirm == 'y':
                    self.students.remove(s)  
                    print(">> Thành công: Đã xóa sinh viên khỏi hệ thống!")
                else:
                    print(">> Đã hủy thao tác xóa.")
                return
                
        print(">> Lỗi: Không tồn tại mã sinh viên này trong hệ thống!")
    def search_student(self):
        """Chức năng 5: Tìm kiếm sinh viên theo tên gần đúng"""
        print("\n--- TÌM KIẾM SINH VIÊN ---")
        keyword = input("Nhập tên sinh viên cần tìm: ").strip().lower()
        found_students = []
        
        for s in self.students:
            if keyword in s.name.lower():
                found_students.append(s)
                
        if not found_students:
            print(">> Không tìm thấy sinh viên phù hợp.")
        else:
            print(f">> Tìm thấy {len(found_students)} sinh viên phù hợp:")
            print("-" * 105)
            print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Lý Thuyết':<10} | {'Thực Hành':<10} | {'Đồ Án':<10} | {'Tổng Kết':<10} | {'Học Lực':<10}")
            print("-" * 105)
            for s in found_students:
                print(f"{s.id:<10} | {s.name:<20} | {s.theory_score:<10.1f} | {s.practice_score:<10.1f} | {s.project_score:<10.1f} | {s.final_score:<10.2f} | {s.academic_rank:<10}")
            print("-" * 105)

def main():
    manager = StudentManager()
    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên theo tên")
        print("6. Thoát")
        print("=====================================")
        choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
        if choice == "1":
            manager.show_all()
        elif choice == "2":
            manager.add_student()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!")
            break
        else:
            print(">> Lỗi: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")

if __name__ == "__main__":
    main()