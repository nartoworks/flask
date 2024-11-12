import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = 'True'

    ASSETS_ROOT = '/static/assets'

    SECRET_KEY = 'fl4sk-d3v'

    UPLOAD_DOKUMEN ='apps/static/uploads/dokumen'
    UPLOAD_FOTO ='apps/static/uploads/foto'
