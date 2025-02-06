from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .client import ClientDB
from .order import OrderDB
from .order_line import OrderLineDB
from .product import ProductDB