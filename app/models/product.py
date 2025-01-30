class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def to_json(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price
        }

    def __repr__(self):
        return f"Product(product_id={self.product_id}, name='{self.name}', price={self.price})"

    def change_price(self, price):
        self.price = price