from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate

class StudentService:
    
    @staticmethod
    def get_all(db: Session):
        return db.query(Student).all()

    @staticmethod
    def get_by_id(db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def create(db: Session, student_data: StudentCreate):
        db_student = Student(
            full_name=student_data.full_name,
            email=student_data.email,
            major=student_data.major,
            gpa=student_data.gpa
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    @staticmethod
    def update(db: Session, student_id: int, student_data: StudentCreate):
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if db_student:
            db_student.full_name = student_data.full_name
            db_student.email = student_data.email
            db_student.major = student_data.major
            db_student.gpa = student_data.gpa
            db.commit()
            db.refresh(db_student)
        return db_student

    @staticmethod
    def delete(db: Session, student_id: int):
        db_student = db.query(Student).filter(Student.id == student_id).first()
        if db_student:
            db.delete(db_student)
            db.commit()
            return True
        return False
