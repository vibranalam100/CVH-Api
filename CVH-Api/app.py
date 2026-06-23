from flask import Flask

from Config import Config
from DB import db

from models.VehicleModel import Vehicle
from models.SensorModel import SensorData

from repos.Repository import SqlRepository
from services.VehicleService import VehicleService
from services.HealthService import HealthService
from routes.Routes import create_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    repository = SqlRepository(db)

    vehicle_service = VehicleService(repository)
    health_service = HealthService(repository)

    api_routes = create_routes(
        vehicle_service=vehicle_service,
        health_service=health_service
    )

    app.register_blueprint(api_routes)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)