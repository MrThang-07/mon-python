class Book:
    def __init__(self, book_id, title, author, quantity):
        self.id = book_id
        self.title = title
        self.author = author
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Số lượng không được âm!")
        self.__quantity = value

    def show_info(self):
        return f"{self.id} | {self.title} | {self.author} | {self.__quantity}"