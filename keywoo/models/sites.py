from keywoo import db
from datetime import datetime

class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.Text)
    user = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime)

    def __init__(self, name=None, url=None, user=None):
        self.name = name
        self.url = url
        self.user = user
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} name:{} url:{} user:{}>'.format(self.id, self.name, self.url, self.user)