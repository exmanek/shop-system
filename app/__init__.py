from flask import Flask, request, jsonify, make_response
from app.models.client import Client
from app.models.product import Product
from app.models.cart import Cart
from app.models.order import Order

app = Flask(__name__)
app.json.sort_keys = False
cart = Cart()
products = []
clients = []
orders = []


## client routes

# create
@app.route('/client', methods=['POST'])
def create_client():
    client_id = len(clients) + 1
    name = request.json.get('name')

    if not name:
        return make_response(jsonify({"error": "Missing required fields."}), 400)

    client = Client(client_id,name)
    clients.append(client)

    response_data = {
        "success": True,
        "client":
            {
                "client_id": client.client_id,
                "name": client.name
            }
    }
    return make_response(jsonify(response_data), 201)

# get
@app.route('/client', methods=['GET'])
def get_clients():

    response_data = {
        "success": True,
        "clients": [client.to_json() for client in clients]
    }
    return make_response(jsonify(response_data), 200)

# get/id
@app.route('/client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    for client in clients:
        name = client.name

    response_data = {
        "success": True,
        "client": {"client_id": client_id, "name": name}
    }
    return make_response(jsonify(response_data), 200)


## cart routes

# get
@app.route('/cart', methods=['GET'])
def get_cart():
    return cart.get_products(products)

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
        "cart": cart.items
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

## product

# add
@app.route('/product', methods=['POST'])
def add_product():
    product_id = len(products) + 1
    name = request.json.get('name')
    price = request.json.get('price')

    if not name or not price:
        return make_response(jsonify({"error": "Missing required fields."}), 400)

    product = Product(product_id, name, price)
    products.append(product)

    response_data = {
        "success": True,
        "product": {"product_id": product.product_id, "name": product.name, "price": product.price}
    }
    return make_response(jsonify(response_data), 201)

# get all
@app.route('/product', methods=['GET'])
def get_all_products():
    response_data = {
        "success": True,
        "products": [product.to_json() for product in products]
    }
    return make_response(jsonify(response_data), 200)

# get/id
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):

    for product in products:
        name = product.name
        price = product.price
    response_data = {
        "success": True,
        "product": {"product_id": product_id, "name": name, "price": price}
    }
    return make_response(jsonify(response_data), 200)

# change price
@app.route('/product/<int:product_id>/price', methods=['PUT'])
def change_price(product_id):
    new_price = request.json.get('price')
    for product in products:
        if product.product_id == product_id:
            product.change_price(new_price)

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

    order_id = len(orders) + 1
    order = Order(order_id, client, cart)
    order.checkout(cart, products)
    orders.append(order)

    response_data = {
        "success": True,
        "order": {"order_id": order.order_id, "client": client.name, "total_price": order.cart.total_price(products)}
    }
    return make_response(jsonify(response_data), 201)


@app.route('/order/', methods=['GET'])
def get_orders():
    response_data = {
        "success": True,
        "orders": [
            {
                "order_id": order.order_id,
                "client": order.client.name,
                "total_price": order.cart.total_price(products),
            }
            for order in orders
        ]
    }
    return make_response(jsonify(response_data), 200)