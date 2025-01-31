from app.models.product import Product
from flask import make_response, jsonify

class Cart:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Cart(items={self.items})"

    def add_product(self, product: Product, quantity):
        for item in self.items:
            if item['product_id'] == product.product_id:
                item['quantity'] += quantity
                return

        self.items.append({
            'product_id': product.product_id,
            'quantity': quantity
        })

    def remove_product(self, product: Product):
        for item in self.items:
            if item['product_id'] == product.product_id:
                self.items.remove(item)
                return make_response(f"Removed product with ID {product.product_id} from the cart.")
        return make_response("Product is not in cart")

    def get_products(self, products_list):
        cart_products = []
        cart_price = 0

        for item in self.items:
            product = None
            for p in products_list:
                if p.product_id == item["product_id"]:
                    product = p
                    break

            if product:
                total_price = product.price * item["quantity"]
                cart_price += total_price
                cart_products.append({
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": product.price,
                    "quantity": item["quantity"],
                    "total_price": total_price
                })

        response_data = {
            "success": True,
            "cart_price": cart_price,
            "products": cart_products
        }
        return make_response(jsonify(response_data), 200)

    def total_price(self,products):
        cart_price = 0
        for item in self.items:
            product = None
            for p in products:
                if p.product_id == item["product_id"]:
                    product = p
                    break
            if product:
                total_price = item["quantity"] * product.price
                cart_price += total_price
        return cart_price
