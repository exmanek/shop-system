from app.db import db

class ProductDB(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    @classmethod
    def get_from_db(cls):
        return cls.query.all()

    @classmethod
    def get_from_db_by_id(cls, product_id):
        return cls.query.filter_by(product_id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price
        }

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()