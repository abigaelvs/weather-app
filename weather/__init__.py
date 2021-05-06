from flask import Flask
from decouple import config

from .views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY')

    app.register_blueprint(views, url_prefix='/')

    return app
    