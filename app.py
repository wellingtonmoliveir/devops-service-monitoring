from app_factory import create_app
from extensions import db
from models import Service, HealthCheck
from flask import request, jsonify

app = create_app()

@app.route('/services', methods=['POST'])
def add_service():
    data = request.json
    service = Service(name=data['name'], url=data['url'])
    db.session.add(service)
    db.session.commit()
    return jsonify({'message': 'Service added'})

@app.route('/services', methods=['GET'])
def list_services():
    services = Service.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'url': s.url} for s in services])

@app.route('/metrics')
def metrics():
    checks = HealthCheck.query.all()
    return jsonify([{
        'service_id': c.service_id,
        'status': c.status,
        'response_time': c.response_time
    } for c in checks])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
