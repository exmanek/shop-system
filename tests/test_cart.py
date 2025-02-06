from app.models.cart import Cart
from app.models.product import Product

def test_add_product_to_cart():
    # Arrange
    cart = Cart()
    laptop = Product(product_id=1, name="laptop", price=1000.0)

    # Act
    cart.add_product(laptop, 2)

    # Assert
    assert len(cart.items) == 1
    assert cart.items[0]['product_id'] == laptop.product_id
    assert cart.items[0]['quantity'] == 2