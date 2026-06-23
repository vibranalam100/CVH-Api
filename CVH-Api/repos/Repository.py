from models.VehicleModel import Vehicle
from models.SensorModel import SensorData


class SqlRepository:
    def __init__(self, db):
        self.db = db

    # -------------------------
    # Vehicle methods
    # -------------------------

    def get_all_vehicles(self):
        vehicles = Vehicle.query.all()
        return [vehicle.to_dict() for vehicle in vehicles]

    def get_vehicle_by_id(self, vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)

        if vehicle is None:
            return None

        return vehicle.to_dict()

    def add_vehicle(self, vehicle_data):
        new_vehicle = Vehicle(
            vehicle_number=vehicle_data["vehicle_number"],
            vehicle_type=vehicle_data["vehicle_type"],
            manufacturer=vehicle_data["manufacturer"],
            model=vehicle_data["model"],
            mileage_km=vehicle_data["mileage_km"]
        )

        self.db.session.add(new_vehicle)
        self.db.session.commit()

        return new_vehicle.to_dict()

    # -------------------------
    # Sensor data methods
    # -------------------------

    def get_all_sensor_data(self):
        sensor_records = SensorData.query.all()
        return [record.to_dict() for record in sensor_records]

    def add_sensor_data(self, sensor_data):
        new_sensor_data = SensorData(
            vehicle_id=sensor_data["vehicle_id"],
            engine_temperature=sensor_data["engine_temperature"],
            oil_pressure=sensor_data["oil_pressure"],
            battery_voltage=sensor_data["battery_voltage"],
            brake_wear=sensor_data["brake_wear"]
        )

        self.db.session.add(new_sensor_data)
        self.db.session.commit()

        return new_sensor_data.to_dict()

    def get_sensor_data_by_vehicle_id(self, vehicle_id):
        sensor_records = (
            SensorData.query
            .filter_by(vehicle_id=vehicle_id)
            .order_by(SensorData.id.asc())
            .all()
        )

        return [record.to_dict() for record in sensor_records]