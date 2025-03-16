from notebook import db


class Note(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class Comment(db.Model):
    timestamp = db.Column(db.DateTime, primary_key=True)
    note = db.Column(db.String(120), db.ForeignKey('note.name'))
    comment = db.Column(db.String(255))
