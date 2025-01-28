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
    cart.__repr__()
    print(f"Total price: {cart.total_price()}")

    order1 = Order(1, szymon, cart)
    szymon.add_order(order1)
    order1.checkout(cart)

    cart.add_product(telefon,20)
    print(f"Total price: {cart.total_price()}")

    order2 = Order(2, szymon, cart)
    szymon.add_order(order2)
    order2.checkout(cart)

    cart.remove_product(laptop)
    cart.remove_product(telefon)
    cart.add_product(telefon,2)
    print(f"Total price: {cart.total_price()}")
    cart.__repr__()

    order2 = Order(3, szymon, cart)
    szymon.add_order(order2)
    order2.checkout(cart)

    szymon.get_order_history()

    laptop.change_price(1100)
    szymon.get_order_history()
    return