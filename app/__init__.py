from flask import Flask
from .routes import main

def start_app():
    app = Flask(__name__)

    app.register_blueprint(main)

    return app
