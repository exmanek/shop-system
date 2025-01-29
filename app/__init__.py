from linecache import updatecache
from venv import create

from flask import Flask, request, jsonify, make_response
from app.models.client import Client
from app.models.product import Product
from app.models.cart import Cart
from app.models.order import Order

app = Flask(__name__)
cart = Cart()
products = []
clients = []


## client routes

# create
@app.route('/client', methods=['POST'])
def create_client():
    data = request.get_json()
    client = Client(client_id=data['client_id'], name=data['name'])
    response_data = {
        "success": True,
        "client": {"client_id": client.client_id, "name": client.name}
    }
    return make_response(jsonify(response_data), 201)

# get
@app.route('/client', methods=['GET'])
def get_clients():
    # In a real implementation, you would retrieve from a database
    response_data = {
        "success": True,
        "clients": []  # List of clients should be fetched from database
    }
    return make_response(jsonify(response_data), 200)

# get/id
@app.route('/client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    # In a real implementation, you would retrieve from a database
    response_data = {
        "success": True,
        "client": {"client_id": client_id, "name": "Client Name"}  # Example response
    }
    return make_response(jsonify(response_data), 200)


## cart routes

# get
@app.route('/cart', methods=['GET'])
def get_cart():
    response_data = {
        "success": True,
        "cart": cart.items
    }
    return make_response(jsonify(response_data), 200)

# add
@app.route('/cart/add', methods=['POST'])
def add_product_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    product = None
    for p in products:
        if p.product_id == product_id:
            product = p
            break
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    cart.add_product(product, quantity)

    response_data = {
        "success": True,
        "cart": cart.items  # Zwróć zawartość koszyka
    }
    return make_response(jsonify(response_data), 201)

# remove
@app.route('/cart/remove', methods=['POST'])
def remove_product_from_cart():
    data = request.get_json()
    product = Product(product_id=data['product_id'], name="", price=0)
    cart.remove_product(product)
    response_data = {
        "success": True,
        "cart": cart.items
    }
    return make_response(jsonify(response_data), 200)

#total
@app.route('/cart/total', methods=['GET'])
def total_price():
    response_data = {"success": True, "total_price": cart.total_price()}
    return make_response(jsonify(response_data), 200)

## product

# add
@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(product_id=data['product_id'], name=data['name'], price=data['price'])

    products.append(product)

    response_data = {
        "success": True,
        "product": {"product_id": product.product_id, "name": product.name, "price": product.price}
    }
    return make_response(jsonify(response_data), 201)

# get all
@app.route('/product', methods=['GET'])
def get_all_products():
    # In a real implementation, you would retrieve from a database
    response_data = {
        "success": True,
        "products": []  # List of products should be fetched from database
    }
    return make_response(jsonify(response_data), 200)

# get/id
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # In a real implementation, you would retrieve from a database
    response_data = {
        "success": True,
        "product": {"product_id": product_id, "name": "Product Name", "price": 100}
    }
    return make_response(jsonify(response_data), 200)

# change price
@app.route('/product/<int:product_id>/price', methods=['PUT'])
def change_price(product_id):
    data = request.get_json()
    new_price = data['price']

    response_data = {
        "success": True,
        "product": {"product_id": product_id, "new_price": new_price}
    }
    return make_response(jsonify(response_data), 200)

## order
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    client_id = data.get('client_id')

    client = None
    for c in clients:
        if c.client_id == client_id:
            client = c
            break

    order_id = len(client.orders) + 1
    order = Order(order_id, client=client, cart=cart)

    response_data = {
        "success": True,
        "order": {"order_id": order.order_id, "client": order.client.name, "total_price": order.cart.total_price()}
    }
    return make_response(jsonify(response_data), 201)