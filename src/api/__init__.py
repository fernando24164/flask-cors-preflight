from flask_restx import Api
from api.namespaces.api import api as cat_api

api = Api(title="test", version="1.0")

api.add_namespace(cat_api)
