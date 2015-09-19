# -*- coding: utf-8 -*-

"""Akira-labs demo server"""


from collections import namedtuple


v_info = namedtuple(
    'v_info', ('major', 'minor', 'patch')
)

VERSION = v_info(0, 1, 0)
__version__ = "{0.major}.{0.minor}.{0.patch}".format(VERSION)
__author__ = "m4dz"
__contact__ = "code@m4dz.net"
__homepage__ = "https://github.com/m4dz/backend"

# -eof meta-


#### Flask app init

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
