from flask_restx import Namespace, fields


class CoinPriceDto:
    api = Namespace('coin', description='coin related operations')
    coin_price = api.model('coinPrice', {
        'id': fields.Integer(required=True, description='Id'),
        'price': fields.Float(required=True, description='Price'),
        'coin': fields.String(required=True, description='Coin'),
        'timestamp': fields.DateTime(description='Timestamp')
    })
    coin_price_result = api.model('Result', {
        'count': fields.Integer(required=True, description='count'),
        'url': fields.String(description='previous'),
        'next': fields.String(description='next'),
        'data': fields.List(fields.Nested(coin_price))
    })
