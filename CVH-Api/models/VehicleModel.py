from DB import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(50), nullable=False, unique=True)
    vehicle_type = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    mileage_km = db.Column(db.Float, nullable=False)

    sensor_data = db.relationship(
        "SensorData",
        backref="vehicle",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_number": self.vehicle_number,
            "vehicle_type": self.vehicle_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "mileage_km": self.mileage_km
        }