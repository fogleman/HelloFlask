from hello import db

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    def __init__(self, text, timestamp):
        self.text = text
        self.timestamp = timestamp
