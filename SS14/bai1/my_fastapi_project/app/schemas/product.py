from pydantic import BaseModel

# Schema chung chứa các thuộc tính cơ bản
class ProductBase(BaseModel):
    name: str
    price: float

# Schema dùng khi thêm hoặc cập nhật sản phẩm (Client gửi lên)
class ProductCreate(ProductBase):
    pass

# Schema dùng khi trả thông tin sản phẩm về cho Client (Có thêm trường id)
class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
