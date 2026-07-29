class Book:
    def __init__(self, book_id, title, author, quantity):
        self.id = book_id
        self.title = title
        self.author = author
        self.quantity = int(quantity)

    def show_info(self):
        print(f"{self.id} | {self.title} | {self.author} | {self.quantity}")