from flask import current_app as app
from flask_restful import Resource
from utils.exception_handler import handle_exceptions, handle_authorization
from functionality.product_info import get_product_info
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields as f
from models import session


class ProductGetSchema(Schema):
    product_id = f.Str(required=False)

    class Meta:
        strict = True


class Product(Resource):
    decorators = [handle_exceptions, handle_authorization]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    @use_kwargs(ProductGetSchema)
    def get(self, *args, **kwargs):
        app.logger.info('In get method of product info')
        response = get_product_info(kwargs.get('product_id'))
        return response

