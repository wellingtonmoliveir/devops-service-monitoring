from extensions import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(255))

class HealthCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer)
    status = db.Column(db.String(10))
    response_time = db.Column(db.Float)
