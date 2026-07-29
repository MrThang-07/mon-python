from library import Library
from book import Book
from student import Student

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