from app.db import db

class ClientDB(db.Model):
    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    orders = db.relationship('OrderDB', back_populates='client', lazy=True)

    @classmethod
    def get_from_db(cls):
        return cls.query.all()

    @classmethod
    def get_from_db_by_id(cls, client_id):
        return cls.query.filter_by(client_id=client_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {
            "client_id": self.client_id,
            "name": self.name
        }