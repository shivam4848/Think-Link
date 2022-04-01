from flask import request, current_app, abort
from flask_restx import Resource

from ..service.coin_service import getCointPriceFromCoinNDate
from ..service.pagination import get_paginated_list
from ..util.dto import CoinPriceDto

api = CoinPriceDto.api
_coin_price = CoinPriceDto.coin_price_result


@api.route('/price/<coin>')
@api.param("coin", description="Coin Name")
class PriceList(Resource):
    @api.doc('list_of_all_coin_prices')
    @api.marshal_list_with(_coin_price)
    def get(self, coin):
        """List all coin prices"""
        try:
            args = request.args
            searched_date = args['date']
            offset = args.get('offset', 0)
            limit = args.get('limit', 0)
            data = getCointPriceFromCoinNDate(coin, searched_date)
            response = get_paginated_list(data, request.url, offset=offset, limit=limit)
            return response
        except Exception as error:
            current_app.logger.exception(f"Error in {request.url} --> {error}")
            abort(500)
