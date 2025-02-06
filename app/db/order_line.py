from app.db import db



class OrderLineDB(db.Model):
    __tablename__ = 'orderlines'

    orderline_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    order = db.relationship('OrderDB', back_populates='orderlines')
    product = db.relationship('ProductDB', backref=db.backref('orderlines', lazy=True))