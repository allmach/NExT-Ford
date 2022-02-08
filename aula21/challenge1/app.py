from flask import Flask

from challenge1.ext import database
from challenge1.ext import config
from challenge1.ext import site
from challenge1.ext import api
from challenge1.ext import cli


app = Flask(__name__)
config.init_app(app)
database.init_app(app)
cli.init_app(app)
site.init_app(app)
api.init_app(app)
