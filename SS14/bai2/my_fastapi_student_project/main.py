import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import student

# Tự động tạo bảng 'students' trong MySQL dựa vào cấu hình khai báo ở Model nếu bảng chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="Hệ thống API quản lý sinh viên sử dụng FastAPI, SQLAlchemy và MySQL",
    version="1.0.0"
)

# Đăng ký router sinh viên vào hệ thống chính
app.include_router(student.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
