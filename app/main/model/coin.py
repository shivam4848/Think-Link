from datetime import datetime

from .. import db


class CoinPrice(db.Model):
    __tablename__ = "coinPrice"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    coin = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"<Coin -> {self.coin} Price --> {self.price}>"
