class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_product(self, product, quantity):
        for item in self.items:
            if item['product'] == product:
                if item['quantity'] > quantity:
                    item['quantity'] -= quantity
                else:
                    self.items.remove(item)
                break

    def total_price(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)
