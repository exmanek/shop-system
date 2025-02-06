from flask import Blueprint, request, jsonify, make_response
from app.db.client import ClientDB

client_bp = Blueprint('client', __name__)

# create
@client_bp.route('/client', methods=['POST'])
def create_client():
    name = request.json.get('name')

    if not name:
        return make_response(jsonify({"error": "Missing required fields."}), 400)

    client = ClientDB(name=name)
    client.save_to_db()

    response_data = {
        "success": True,
        "client": client.to_json()
    }
    return make_response(jsonify(response_data), 201)

# get
@client_bp.route('/client', methods=['GET'])
def get_clients():
    clients = ClientDB.get_from_db()

    response_data = {
        "success": True,
        "clients": [client.to_json() for client in clients]
    }
    return make_response(jsonify(response_data), 200)

# get/id
@client_bp.route('/client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = ClientDB.get_from_db_by_id(client_id)
    if not client:
        return make_response(jsonify({"error": "Client not found"}), 404)

    response_data = {
        "success": True,
        "client": client.to_json()
    }
    return make_response(jsonify(response_data), 200)
