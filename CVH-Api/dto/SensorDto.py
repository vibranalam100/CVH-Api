from Exceptions import ValidationError


class CreateSensorDataDTO:
    def __init__(
        self,
        vehicle_id,
        engine_temperature,
        oil_pressure,
        battery_voltage,
        brake_wear
    ):
        self.vehicle_id = vehicle_id
        self.engine_temperature = engine_temperature
        self.oil_pressure = oil_pressure
        self.battery_voltage = battery_voltage
        self.brake_wear = brake_wear

    @staticmethod
    def from_dict(data):
        required_fields = [
            "vehicle_id",
            "engine_temperature",
            "oil_pressure",
            "battery_voltage",
            "brake_wear"
        ]

        for field in required_fields:
            if field not in data:
                raise ValidationError(f"{field} is required")

        if data["brake_wear"] < 0 or data["brake_wear"] > 100:
            raise ValidationError("brake_wear must be between 0 and 100")

        return CreateSensorDataDTO(
            vehicle_id=data["vehicle_id"],
            engine_temperature=data["engine_temperature"],
            oil_pressure=data["oil_pressure"],
            battery_voltage=data["battery_voltage"],
            brake_wear=data["brake_wear"]
        )