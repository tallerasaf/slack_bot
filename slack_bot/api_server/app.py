from flask import Flask
from flask_restful import Api

from .routes import add_routes

app = Flask(__name__)
api = Api(app)


def run():
    add_routes(api)
    app.run(debug=True, host='localhost', port=8081)
