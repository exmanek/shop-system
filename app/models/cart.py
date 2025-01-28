from app.models.product import Product

class Cart:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return print(f"Cart(items={self.items})")

    def add_product(self, product: Product, quantity):
        for item in self.items:
            if item['product_id'] == product.product_id:
                item['quantity'] += quantity
                return

        self.items.append({
            'product_id': product.product_id,
            'product_name': product.name,
            'product_price': product.price,
            'quantity': quantity
        })

    def remove_product(self, product: Product):
        for item in self.items:
            if item['product_id'] == product.product_id:
                self.items.remove(item)
                print(f"Removed product with ID {product.product_id} from the cart.")
                return
        print("Product is not in cart")


    def total_price(self):
        return sum(item['product_price'] * item['quantity'] for item in self.items)
