from celery import Celery
import requests
from app_factory import create_app
from extensions import db
from models import Service, HealthCheck

celery = Celery('tasks', broker='redis://redis:6379/0')

app = create_app()

@celery.task
def check_services():
    with app.app_context():
        services = Service.query.all()

        for s in services:
            try:
                r = requests.get(s.url, timeout=5)
                status = 'UP'
                response_time = r.elapsed.total_seconds()
            except:
                status = 'DOWN'
                response_time = 0

            db.session.add(HealthCheck(
                service_id=s.id,
                status=status,
                response_time=response_time
            ))

        db.session.commit()
