from flask import Blueprint, request, jsonify

from dto.VehicleDto import CreateVehicleDTO
from dto.SensorDto import CreateSensorDataDTO
from Exceptions import ValidationError, NotFoundError


def create_routes(vehicle_service, health_service):
    api = Blueprint("api", __name__)

    @api.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Commercial Vehicle Health Monitoring API",
            "description": "REST API for monitoring commercial vehicle health using SQL"
        }), 200

    @api.route("/vehicles", methods=["POST"])
    def create_vehicle():
        try:
            dto = CreateVehicleDTO.from_dict(request.json)
            vehicle = vehicle_service.create_vehicle(dto)

            return jsonify({
                "message": "Vehicle created successfully",
                "vehicle": vehicle
            }), 201

        except ValidationError as error:
            return jsonify({
                "error": str(error)
            }), 400

    @api.route("/vehicles", methods=["GET"])
    def get_vehicles():
        vehicles = vehicle_service.get_all_vehicles()

        return jsonify({
            "vehicles": vehicles
        }), 200

    @api.route("/sensor-data", methods=["POST"])
    def add_sensor_data():
        try:
            dto = CreateSensorDataDTO.from_dict(request.json)
            sensor_data = health_service.add_sensor_data(dto)

            return jsonify({
                "message": "Sensor data added successfully",
                "sensor_data": sensor_data
            }), 201

        except ValidationError as error:
            return jsonify({
                "error": str(error)
            }), 400

        except NotFoundError as error:
            return jsonify({
                "error": str(error)
            }), 404

    @api.route("/vehicle-health/<int:vehicle_id>", methods=["GET"])
    def get_vehicle_health(vehicle_id):
        try:
            health_report = health_service.get_vehicle_health(vehicle_id)

            return jsonify(health_report), 200

        except NotFoundError as error:
            return jsonify({
                "error": str(error)
            }), 404

    return api