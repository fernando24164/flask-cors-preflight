from flask import Flask
from api import api
from api.blueprints import cat_options

app = Flask(__name__)
app.register_blueprint(cat_options)
api.init_app(app)

app.run(debug=True)