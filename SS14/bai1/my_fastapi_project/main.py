import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import product

# Tự động tạo bảng 'products' trong MySQL dựa vào cấu hình khai báo ở Model nếu bảng chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Management API",
    description="Hệ thống API quản lý sản phẩm sử dụng FastAPI, SQLAlchemy và MySQL",
    version="1.0.0"
)

# Đăng ký router sản phẩm vào hệ thống chính
app.include_router(product.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
