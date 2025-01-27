class Order:
    def __init__(self, order_id, client, cart):
        self.order_id = order_id
        self.client = client
        self.cart = cart

    def checkout(self, cart):
        max_order_value = 30000
        if cart.total_price() > max_order_value:
            return print(f"Order declined, total value of order is higher than {max_order_value}")

    def __repr__(self):
        return f"Order ID: {self.order_id}, Total Price: {self.cart.total_price()}"