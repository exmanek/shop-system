from app.db import db

class OrderDB(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)

    client = db.relationship('ClientDB', back_populates='orders')
    orderlines = db.relationship('OrderLineDB', back_populates='order', lazy=True)

    @classmethod
    def get_from_db(cls):
        return cls.query.all()

    @classmethod
    def get_from_db_by_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()