from flask import Blueprint, request, jsonify, make_response, render_template
from app.db.product import ProductDB

product_bp = Blueprint('product', __name__)

# create
@product_bp.route('/product', methods=['POST'])
def add_product():
    name = request.json.get('name')
    price = request.json.get('price')

    if not name or not price:
        return make_response(jsonify({"error": "Missing required fields."}), 400)

    product = ProductDB(name=name, price=price)
    product.save_to_db()

    response_data = {
        "success": True,
        "product": product.to_json()
    }
    return make_response(jsonify(response_data), 201)

# get
@product_bp.route('/', methods=['GET'])
def get_all_products():
    products = ProductDB.get_from_db()

    response_data = {
        "success": True,
        "products": [product.to_json() for product in products]
    }
    return render_template('index.html', products=products)

# get/id
@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductDB.get_from_db_by_id(product_id)
    if not product:
        return make_response(jsonify({"error": "Product not found"}), 404)

    response_data = {
        "success": True,
        "product": product.to_json()
    }
    return make_response(jsonify(response_data), 200)

@product_bp.route('/product/<int:product_id>/delete', methods=['DELETE'])
def delete_product(product_id):
    product = ProductDB.get_from_db_by_id(product_id)
    if not product:
        return make_response(jsonify({"error": "Product not found"}), 404)
    product.delete_from_db()
    return make_response(jsonify({"success": True}), 200)