from flask import Blueprint, request, jsonify, make_response
from app.models.cart import Cart
from app.db.product import ProductDB
from app.db.client import ClientDB

cart_bp = Blueprint('cart', __name__)
cart = Cart()

# get
@cart_bp.route('/cart', methods=['GET'])
def get_cart():
    products = ProductDB.get_from_db()
    return cart.get_products(products)

# add
@cart_bp.route('/cart/add', methods=['POST'])
def add_product_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    product = ProductDB.get_from_db_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    cart.add_product(product, quantity)

    response_data = {
        "success": True,
        "cart": cart.items
    }
    return make_response(jsonify(response_data), 201)

# remove
@cart_bp.route('/cart/remove', methods=['POST'])
def remove_product_from_cart():
    data = request.get_json()
    product_id = data.get('product_id')

    product = ProductDB.get_from_db_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    return cart.remove_product(product)

@cart_bp.route('/cart/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    client_id = data.get('client_id')

    client = ClientDB.get_from_db_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    products = ProductDB.get_from_db()
    return cart.checkout(products)