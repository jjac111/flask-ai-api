from flask import Flask
from flask_cors import CORS
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    from app.routes import api
    app.register_blueprint(api)

    return app
