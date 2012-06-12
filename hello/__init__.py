from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hello.config')

db = SQLAlchemy(app)

import hooks
import models
import views
