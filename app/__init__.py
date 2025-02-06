from flask import Flask
from app.db import db
from app.routes.cart import cart_bp
from app.routes.order import order_bp
from app.routes.client import client_bp
from app.routes.product import product_bp

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(product_bp)
    return app