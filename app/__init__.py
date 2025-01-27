from app.models.client import Client
from app.models.product import Product
from app.models.cart import Cart
from app.models.order import Order

def run():
    szymon = Client(1,"Szymon")
    laptop = Product(1, "Laptop", 3000)
    telefon = Product(2, "Smartphone", 1500)

    cart = Cart()
    cart.add_product(laptop, 10)
    cart.add_product(telefon, 2)
    print(f"Total price: {cart.total_price()}")

    order = Order(1, szymon, cart)
    order2 = order = Order(2, szymon, cart)
    szymon.add_order(order)
    szymon.add_order(order2)

    order.checkout(cart)
    order2.checkout(cart)
    print(f"Order history: {szymon.get_order_history()}")
    return