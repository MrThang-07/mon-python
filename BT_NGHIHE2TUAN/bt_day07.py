from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Library Management API - Mini Project 1", version="1.0.0")


class Book(BaseModel):
    id: int
    ten_sach: str
    tac_gia: str
    nam_xuat_ban: int
    so_luong: int


danh_sach_sach = [
    {
        "id": 1,
        "ten_sach": "Nhà Giả Kim",
        "tac_gia": "Paulo Coelho",
        "nam_xuat_ban": 1988,
        "so_luong": 5,
    },
    {
        "id": 2,
        "ten_sach": "Đắc Nhân Tâm",
        "tac_gia": "Dale Carnegie",
        "nam_xuat_ban": 1936,
        "so_luong": 10,
    },
    {
        "id": 3,
        "ten_sach": "Tuổi Trẻ Đáng Giá Bao Nhiêu",
        "tac_gia": "Rosie Nguyễn",
        "nam_xuat_ban": 2016,
        "so_luong": 8,
    },
]


@app.post("/api/v1/books", response_model=Book)
def create_book(book: Book):
    new_book = book.model_dump()
    danh_sach_sach.append(new_book)
    return new_book


@app.get("/api/v1/books", response_model=List[Book])
def get_all_books():
    return danh_sach_sach


@app.get("/api/v1/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    for book in danh_sach_sach:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy sách với id: {book_id}"
    )


@app.put("/api/v1/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(danh_sach_sach):
        if book["id"] == book_id:
            book_data = updated_book.model_dump()
            danh_sach_sach[index] = book_data
            return book_data
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy sách với id: {book_id}"
    )


@app.delete("/api/v1/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for book in danh_sach_sach:
        if book["id"] == book_id:
            danh_sach_sach.remove(book)
            return book
    raise HTTPException(
        status_code=404, detail=f"Không tìm thấy sách với id: {book_id}"
    )