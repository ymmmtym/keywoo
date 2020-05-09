from keywoo import db
from datetime import datetime

class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(50), unique=True)
    url = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, site=None, url=None):
        self.site = site
        self.url = url
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} site:{} url:{}>'.format(self.id, self.site, self.url)