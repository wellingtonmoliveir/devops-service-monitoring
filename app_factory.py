from flask import Flask
from extensions import db   # 🔥 IMPORTANTE

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dev:dev@db:5432/monitoring'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
