from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Thay đổi username, password, host, port và db_name phù hợp với cấu hình MySQL của bạn
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency để cung cấp DB session cho các request và tự động đóng sau khi xong
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
