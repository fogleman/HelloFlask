from flask import render_template, url_for, redirect
from forms import CommentForm
from hello import app, db
from models import Comment
import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            form.text.data,
            datetime.datetime.now()
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('index'))
    comments = Comment.query.order_by(db.desc(Comment.timestamp))
    return render_template('index.html', comments=comments, form=form)
