from app.db import db, ClientDB

class Client:
    def __init__(self, name, client_id=None):
        self.name = name
        self.client_id = client_id
        self.orders = []

    def __repr__(self):
        return f"Client(client_id={self.client_id}, name='{self.name}', orders={len(self.orders)})"

    def add_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return self.orders