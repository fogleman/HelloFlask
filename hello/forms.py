from flask.ext.wtf import Form
from wtforms import TextField, validators

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])
