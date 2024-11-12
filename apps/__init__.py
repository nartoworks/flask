import os

from flask import Flask, Blueprint, url_for, redirect
# from flask_mail import Mail
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os
from apps.config import Config

def create_app(config_class=Config):
    static_folder = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'apps/static')
    template_folder = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'apps/templates')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder, static_url_path='/static')
    app.config.from_object(Config)

    from apps.main.views import main

    app.register_blueprint(main)

    @app.route('/')
    def home():
        return ['Running']

    return app