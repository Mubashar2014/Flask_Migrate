from project import db
from project import app
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    def __init__(self, name, fname,description):
        self.name = name
        self.fname = fname
        self.description=description

with app.app_context():
    db.create_all()
