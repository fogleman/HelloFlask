from flaskext.wtf import Form, TextField, validators

class CommentForm(Form):
    text = TextField('Comment', [validators.Required()])
