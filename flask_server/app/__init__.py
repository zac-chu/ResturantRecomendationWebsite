from flask import Flask

from .api import api as api_blueprint
from .db import init_db

def create_app(config):
    
    app = Flask(__name__)

    app.config.from_object(config)

    with app.app_context():
        try:
            init_db()
        except:
            print("INITIALIZING DB AGAIN")

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app