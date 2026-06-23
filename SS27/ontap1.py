class Student:
    def __init__(self,id,name,theory_score,practice_score,project_score):
        self.id = id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0.0
        self.academic_rank = ""
        self.update_score_rank()

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
    def update_score_rank(self):
        self.calculate_final_score()
        self.classify_academic_rank()

class StudentManager:
    def __init__(self):
        self.students = []
    def is_number(self,prompt):
        while True:
            try:
                score = float(input(prompt).strip())
                if 0.0 <= score <= 10.0:
                    return score
                else:
                    print(">> Lỗi: Điểm phải nằm trong khoảng từ 0.0 đến 10.0!")
            except ValueError:
                print(">> Lỗi: Vui lòng nhập đúng định dạng số!")

            
    def show_all(self):
        if not self.students:
            print("Danh sách hiện rỗng !")
            return
        print(f"{'Mã SV':<10} | {'Họ tên':<20}|{'Điểm Lý Thuyết':<20}|{'Điểm Thực Hành':<20}| {'Điểm Đồ Án':<20}| {'Điểm Tổng Kết':<20}| {'Học Lực':<15}|")
        for i in self.students:
            print("-"*38)
            print(f"{i.id:<10} | {i.name:<20}|{i.theory_score:<20}|{i.practice_score:<20}| {i.project_score:<20}| {i.final_score:<20}| {i.academic_rank:<15}|")
    def add_student(self):
        input_id = input("Nhập mã sv cần thêm : ").strip().upper()
        if not input_id:
            print("Mã bị rỗng !")
            return
        for i in self.students:
            if input_id == i.id:
                print("Mã đã tồn tại !")
                return
        input_name = input("Nhập tên sv : ").strip().title()
        if not input_name:
            print("Tên bị rỗng !")
            return
        theory_score = self.is_number("Vui lòng nhập điểm lý thuyết : ")
        practice_score = self.is_number("Vui lòng nhập điểm thực hành : ")
        project_score = self.is_number("Vui lòng nhập điểm đồ án : ")
        new_student = Student(input_id,input_name,theory_score,practice_score,project_score)
        self.students.append(new_student)
        print("Đã thêm sv thành công .")
    def update_student(self):
        input_id = input("Nhập mã sinh viên cần cập nhật : ").strip().upper()
        for i in self.students:
            if input_id == i.id:
                i.theory_score = self.is_number("Vui lòng nhập điểm lý thuyết : ")
                i.practice_score = self.is_number("Vui lòng nhập điểm thực hành : ")
                i.project_score = self.is_number("Vui lòng nhập điểm đồ án : ")
                i.update_score_rank()
                print(">> Thành công: Đã cập nhật điểm và xét lại học lực!")
                return 
        print(">> Lỗi: Không tồn tại mã sinh viên này trong hệ thống!")
    def delete_student(self):
        input_id = input("Nhập mã sinh viên cần xóa : ").strip().upper()
        for i in self.students:
            if input_id == i.id:
                choice = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ").strip().upper()
                if choice == "Y":
                    self.students.remove(i)
                    print("Đã xóa thành công ")
                    return
                return
        print("Không tìm thấy id sv !")
    def search_student(self):
        list_name = []
        share_name = input("Tìm kiếm tên gần đúng : ").strip().upper()
        for i in self.students:
            if share_name in i.name.upper():
                list_name += [i]
        if not list_name:
            print("Hiện kh tìm thấy thông tin sv nào !")
        else:
            for i in list_name:
                print("-"*38)
                print(f"{i.id:<10} | {i.name:<20}|{i.theory_score:<20}|{i.practice_score:<20}| {i.project_score:<20}| {i.final_score:<20}| {i.academic_rank:<15}|")

        
def main():
    manager = StudentManager()
    while True:
        print("""================ MENU ================
    1. Hiển thị danh sách sinh viên
    2. Thêm sinh viên mới
    3. Cập nhật thông tin sinh viên
    4. Xóa sinh viên
    5. Tìm kiếm sinh viên theo tên
    6. Thoát
    =====================================

    """)
        choice = input("Nhập lựa chọn của bạn: ")
        match (choice):
            case "1":
                manager.show_all()
            case "2": 
                manager.add_student()
            case "3":
                manager.update_student()
            case "4":
                manager.delete_student()
            case "5":
                manager.search_student()
            case "6":
                print("Đã thoát .")
                return
            case _:
                print("Vui lòng nhập lại từ 1 - 6 !")
if __name__ == "__main__":
    main()