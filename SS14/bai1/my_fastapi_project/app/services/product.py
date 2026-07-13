from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductService:
    
    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def create(db: Session, product_data: ProductCreate):
        db_product = Product(name=product_data.name, price=product_data.price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def update(db: Session, product_id: int, product_data: ProductCreate):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            db_product.name = product_data.name
            db_product.price = product_data.price
            db.commit()
            db.refresh(db_product)
        return db_product

    @staticmethod
    def delete(db: Session, product_id: int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            db.delete(db_product)
            db.commit()
            return True
        return False
