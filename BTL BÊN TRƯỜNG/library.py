from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book_id, title, author, quantity):
        if quantity < 0:
            raise ValueError("Số lượng không được âm!")
        new_book = Book(book_id, title, author, quantity)
        self.books.append(new_book)

    def view_books(self):
        for book in self.books:
            print(book.show_info())

    def search_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def delete_book(self, book_id):
        book = self.search_book(book_id)
        if book:
            self.books.remove(book)
            return True
        return False

    def add_student(self, student_id, name, class_name):
        new_student = Student(student_id, name, class_name)
        self.students.append(new_student)

    def view_students(self):
        for student in self.students:
            print(student.show_info())

    def search_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

    def borrow_book(self, student_id, book_id):
        student = self.search_student(student_id)
        if not student:
            raise Exception("Student not found")

        book = self.search_book(book_id)
        if not book:
            raise Exception("Book not found")

        if book.quantity > 0:
            book.quantity -= 1
            return True
        return False

    def return_book(self, student_id, book_id):
        student = self.search_student(student_id)
        if not student:
            raise Exception("Student not found")

        book = self.search_book(book_id)
        if not book:
            raise Exception("Book not found")

        book.quantity += 1
        return True