from goopho.model import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True) 
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(25))
    admin = db.Column(db.Boolean)
    