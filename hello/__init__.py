from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hello.config')

db = SQLAlchemy(app)

import hooks
import models
import views
