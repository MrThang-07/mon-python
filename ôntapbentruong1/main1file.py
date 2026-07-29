# ==========================================
# 1. CLASS BOOK (QUẢN LÝ SÁCH)
# ==========================================
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.id = book_id
        self.title = title
        self.author = author
        self.quantity = int(quantity)

    def show_info(self):
        print(f"{self.id} | {self.title} | {self.author} | {self.quantity}")


# ==========================================
# 2. CLASS STUDENT (QUẢN LÝ SINH VIÊN)
# ==========================================
class Student:
    def __init__(self, student_id, name, class_name):
        self.id = student_id
        self.name = name
        self.class_name = class_name

    def show_info(self):
        print(f"{self.id} | {self.name} | {self.class_name}")


# ==========================================
# 3. CLASS LIBRARY (QUẢN LÝ THƯ VIỆN)
# ==========================================
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


# ==========================================
# 4. HÀM MAIN (ĐIỀU HƯỚNG MENU)
# ==========================================
def main():
    lib = Library()

    # Dữ liệu mẫu test nhanh
    lib.books = [
        Book("B01", "Python Basic", "Nguyễn Văn A", 10),
        Book("B02", "OOP Python", "Trần Văn B", 5)
    ]
    lib.students = [
        Student("SV01", "Lê Văn C", "CNTT1")
    ]

    while True:
        print("\n========== LIBRARY MANAGEMENT ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Add Student")
        print("6. View Students")
        print("7. Search Student")
        print("8. Delete Student")
        print("9. Borrow Book")
        print("10. Return Book")
        print("0. Exit")
        print("========================================")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case '1':
                lib.add_book()
            case '2':
                lib.view_books()
            case '3':
                lib.search_book()
            case '4':
                lib.delete_book()
            case '5':
                lib.add_student()
            case '6':
                lib.view_students()
            case '7':
                lib.search_student()
            case '8':
                lib.delete_student()
            case '9':
                lib.borrow_book()
            case '10':
                lib.return_book()
            case '0':
                print("Cảm ơn bạn đã sử dụng hệ thống thư viện!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()