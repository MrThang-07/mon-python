from pydantic import BaseModel

# Schema chung chứa các thuộc tính cơ bản
class StudentBase(BaseModel):
    full_name: str
    email: str
    major: str
    gpa: float

# Schema dùng khi thêm hoặc cập nhật sinh viên (Client gửi lên)
class StudentCreate(StudentBase):
    pass

# Schema dùng khi trả thông tin sinh viên về cho Client (Có thêm trường id)
class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True
