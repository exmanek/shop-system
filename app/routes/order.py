from flask import Blueprint, jsonify, make_response
from app.models.order import Order
from app.db.client import ClientDB

order_bp = Blueprint('order', __name__)


# get
@order_bp.route('/order', methods=['GET'])
def get_orders():
    orders = Order.get_from_db()

    response_data = {
        "success": True,
        "orders": [
            {
                "order_id": order.order_id,
                "client": order.client.name
            }
            for order in orders
        ]
    }
    return make_response(jsonify(response_data), 200)


# get/id
@order_bp.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.get_from_db_by_id(order_id)
    if not order:
        return make_response(jsonify({"error": "Order not found"}), 404)

    response_data = {
        "success": True,
        "order": {
            "order_id": order.order_id,
            "client": order.client.name
        }
    }
    return make_response(jsonify(response_data), 200)