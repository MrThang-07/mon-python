from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    # --- SÁCH ---
    def add_book(self):
        b_id = input("Nhập mã sách: ").strip()
        if not b_id:
            print("Mã sách không được để trống!")
            return
        for b in self.books:
            if b.id == b_id:
                print("Mã sách đã tồn tại!")
                return
        title = input("Nhập tên sách: ").strip()
        author = input("Nhập tác giả: ").strip()
        try:
            qty = int(input("Nhập số lượng: "))
            if qty < 0:
                print("Số lượng không được âm!")
                return
            self.books.append(Book(b_id, title, author, qty))
            print("Thêm sách thành công!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

    def view_books(self):
        if not self.books:
            print("Thư viện chưa có sách!")
            return
        print("\n--- DANH SÁCH SÁCH ---")
        for b in self.books:
            b.show_info()

    def search_book(self):
        b_id = input("Nhập mã sách cần tìm: ").strip()
        for b in self.books:
            if b.id == b_id:
                print("Đã tìm thấy sách:")
                b.show_info()
                return
        print("Book not found")

    def delete_book(self):
        b_id = input("Nhập mã sách cần xóa: ").strip()
        for b in self.books:
            if b.id == b_id:
                self.books.remove(b)
                print("Xóa sách thành công!")
                return
        print("Book not found")

    # --- SINH VIÊN ---
    def add_student(self):
        s_id = input("Nhập mã sinh viên: ").strip()
        if not s_id:
            print("Mã sinh viên không được để trống!")
            return
        for s in self.students:
            if s.id == s_id:
                print("Mã sinh viên đã tồn tại!")
                return
        name = input("Nhập họ tên: ").strip()
        class_name = input("Nhập lớp: ").strip()
        self.students.append(Student(s_id, name, class_name))
        print("Thêm sinh viên thành công!")

    def view_students(self):
        if not self.students:
            print("Chưa có sinh viên nào!")
            return
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for s in self.students:
            s.show_info()

    def search_student(self):
        s_id = input("Nhập mã sinh viên cần tìm: ").strip()
        for s in self.students:
            if s.id == s_id:
                print("Đã tìm thấy sinh viên:")
                s.show_info()
                return
        print("Student not found")

    def delete_student(self):
        s_id = input("Nhập mã sinh viên cần xóa: ").strip()
        for s in self.students:
            if s.id == s_id:
                self.students.remove(s)
                print("Xóa sinh viên thành công!")
                return
        print("Student not found")

    # --- MƯỢN / TRẢ ---
    def borrow_book(self):
        s_id = input("Nhập mã sinh viên mượn: ").strip()
        student_found = any(s.id == s_id for s in self.students)
        if not student_found:
            print("Student not found")
            return

        b_id = input("Nhập mã sách muốn mượn: ").strip()
        for b in self.books:
            if b.id == b_id:
                if b.quantity > 0:
                    b.quantity -= 1
                    print("Mượn sách thành công!")
                else:
                    print("Sách đã hết!")
                return
        print("Book not found")

    def return_book(self):
        b_id = input("Nhập mã sách muốn trả: ").strip()
        for b in self.books:
            if b.id == b_id:
                b.quantity += 1
                print("Trả sách thành công!")
                return
        print("Book not found")