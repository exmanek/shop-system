from flask import make_response

class Order:
    def __init__(self, order_id, client, cart):
        self.order_id = order_id
        self.client = client
        self.cart = cart

    def __repr__(self):
        return f"Order(order_id={self.order_id}, client={self.client.name}, order_price={self.cart.total_price()}, status='{self.status}')"

    def checkout(self, cart, products):
        max_order_value = 30000
        if cart.total_price(products) > max_order_value:
            return make_response(f"Order declined, total value of order is higher than {max_order_value}")
