from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def start_app():
    app = Flask(__name__)

    app.secret_key = os.getenv('SECRET_KEY')

    from .routes import main
    from .login_session_routes_clients import login_client
    from .login_session_routes_team import login_team
    app.register_blueprint(main)
    app.register_blueprint(login_client)
    app.register_blueprint(login_team)

    return app
