from flask import make_response
from app.db import OrderDB, db
from app.models.client import Client
from app.models.cart import Cart

class Order:
    def __init__(self, order_id=None, client=None, cart=None):
        self.order_id = order_id
        self.client = client
        self.cart = cart

    def __repr__(self):
        return f"Order(order_id={self.order_id}, client={self.client.name}, order_price={self.cart.total_price()})"

    def to_json(self):
        return {
            "order_id": self.order_id,
            "client": self.client.to_json(),
            "cart": self.cart.to_json()
        }
