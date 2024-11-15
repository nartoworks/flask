import os

from flask import Flask, Blueprint, url_for, redirect
# from flask_mail import Mail
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.proxy_fix import ProxyFix
import os
from apps.config import Config

class ReverseProxied(object):
    def __init__(self, app, script_name):
        self.app = app
        self.script_name = script_name

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = self.script_name
        return self.app(environ, start_response)

def create_app(config_class=Config):
    static_folder = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'apps/static')
    template_folder = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'apps/templates')
    #static_folder = '/var/www/flask/static'
    #template_folder = '/var/www/flask/templates'
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder, static_url_path='/flask/static')
    app.config.from_object(Config)
    app.wsgi_app = ReverseProxied(app.wsgi_app, script_name='/flask')
    #app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
    #app.config["APPLICATION_ROOT"] = '/flask'

    from apps.main.views import main

    app.register_blueprint(main)

    @app.route('/')
    def home():
        return ['Running']


    return app