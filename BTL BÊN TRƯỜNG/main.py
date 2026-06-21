from library import Library

def main():
    lib = Library()

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

        choice = input("Choice: ").strip()

        if choice == "1":
            try:
                b_id = input("Mã sách: ").strip()
                title = input("Tên sách: ").strip()
                author = input("Tác giả: ").strip()
                qty = int(input("Số lượng: ").strip())
                lib.add_book(b_id, title, author, qty)
                print("Thêm sách thành công!")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Nhập sai kiểu dữ liệu!")
                else:
                    print(e)

        elif choice == "2":
            lib.view_books()

        elif choice == "3":
            b_id = input("Nhập mã sách: ").strip()
            book = lib.search_book(b_id)
            if book:
                print("Đã tìm thấy sách")
                print(book.show_info())
            else:
                print("Không tìm thấy sách!")

        elif choice == "4":
            b_id = input("Nhập mã sách cần xóa: ").strip()
            if lib.delete_book(b_id):
                print("Xóa sách thành công!")
            else:
                print("Không tìm thấy sách!")

        elif choice == "5":
            s_id = input("Mã sinh viên: ").strip()
            name = input("Họ tên: ").strip()
            class_name = input("Lớp: ").strip()
            lib.add_student(s_id, name, class_name)
            print("Thêm sinh viên thành công!")

        elif choice == "6":
            lib.view_students()

        elif choice == "7":
            s_id = input("Nhập mã sinh viên: ").strip()
            student = lib.search_student(s_id)
            if student:
                print("Đã tìm thấy sinh viên")
                print(student.show_info())
            else:
                print("Không tìm thấy sinh viên!")

        elif choice == "8":
            s_id = input("Nhập mã sinh viên cần xóa: ").strip()
            if lib.delete_student(s_id):
                print("Xóa sinh viên thành công!")
            else:
                print("Không tìm thấy sinh viên!")

        elif choice == "9":
            try:
                s_id = input("Mã sinh viên: ").strip()
                b_id = input("Mã sách: ").strip()
                if lib.borrow_book(s_id, b_id):
                    print("Mượn sách thành công!")
                else:
                    print("Sách đã hết!")
            except Exception as e:
                print(e)

        elif choice == "10":
            try:
                s_id = input("Mã sinh viên: ").strip()
                b_id = input("Mã sách: ").strip()
                if lib.return_book(s_id, b_id):
                    print("Trả sách thành công!")
            except Exception as e:
                print(e)

        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()