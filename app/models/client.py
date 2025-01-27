class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.order_history = []

    def add_order(self,order):
        self.order_history.append(order)

    def get_order_history(self):
        return self.order_history