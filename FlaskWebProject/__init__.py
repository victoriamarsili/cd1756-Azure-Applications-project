"""
The flask application package.
"""

import logging
import sys

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


app = Flask(__name__)
app.config.from_object(Config)

# Configure application logging
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s"
)
stream_handler.setFormatter(formatter)

app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

Session(app)
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"

from FlaskWebProject.models import User


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


import FlaskWebProject.views