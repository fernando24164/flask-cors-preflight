from flask import Blueprint, Response

cat_options = Blueprint('cats', __name__)

@cat_options.route('/cats', methods=["OPTIONS"])
def cats():
    return Response(status=200, headers=[('Access-Control-Allow-Origin', '*')])
