import config

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app():

    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)
    CORS(app)
    jwt = JWTManager(app)

    from models import db

    db.init_app(app)

    with app.app_context():
        db.create_all()
        import routes.auth
        import routes.stories
        import routes.generate_images

        return app
