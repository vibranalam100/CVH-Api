from datetime import datetime
from DB import db


class SensorData(db.Model):
    __tablename__ = "sensor_data"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(
        db.Integer,
        db.ForeignKey("vehicles.id"),
        nullable=False
    )

    engine_temperature = db.Column(db.Float, nullable=False)
    oil_pressure = db.Column(db.Float, nullable=False)
    battery_voltage = db.Column(db.Float, nullable=False)
    brake_wear = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_id": self.vehicle_id,
            "engine_temperature": self.engine_temperature,
            "oil_pressure": self.oil_pressure,
            "battery_voltage": self.battery_voltage,
            "brake_wear": self.brake_wear,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }