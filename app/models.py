from . import db

class Temperature(db.Model):
    __tablename__ = 'Temperature'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(20))
    temperature = db.Column(db.Float)
    duration = db.Column(db.Float)

class Log(db.Model):
    __tablename__ = 'Log'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(50))
    ip = db.Column(db.String(16))
    timestamp = db.Column(db.BigInteger)
    params = db.Column(db.String(500))