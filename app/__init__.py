from flask import Blueprint
from flask_restx import Api

from .main.controller.coin_controller import api as coin_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Thinklink',
    version='1.0',
    description='Thinklink',
)

api.add_namespace(coin_ns, path='/coin')
