import logging
import os
from logging.handlers import RotatingFileHandler

from dynaconf import (FlaskDynaconf, settings)
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

levels = {"DEBUG": logging.DEBUG,
          "INFO": logging.INFO,
          "ERROR": logging.ERROR,
          "WARNING": logging.WARNING}


def logger_configuration(app):
    log_directory = settings.LOG_DIR
    log_file_location = log_directory + settings.LOG_FILE_NAME
    print("Log file", log_file_location)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    handler = RotatingFileHandler(log_file_location,
                                  maxBytes=10000,
                                  backupCount=1)
    handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
    app.logger.addHandler(handler)
    app.logger.setLevel(settings.LOG_LEVEL)


def create_app():
    app = Flask(__name__, static_folder='templates', static_url_path='')
    FlaskDynaconf(app)
    logger_configuration(app)
    return app


basedir = os.path.abspath(os.path.dirname(__file__))
static_folder = basedir + '/templates'
app = create_app()
CORS(app)
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
api = Api(app)
