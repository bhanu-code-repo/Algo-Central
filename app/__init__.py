from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from .routes.binary_search_api import binary_search_bp
    app.register_blueprint(binary_search_bp)

    return app