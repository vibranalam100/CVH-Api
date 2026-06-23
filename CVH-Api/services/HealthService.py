from Exceptions import NotFoundError


class HealthService:
    def __init__(self, repository):
        self.repository = repository

    def add_sensor_data(self, dto):
        vehicle = self.repository.get_vehicle_by_id(dto.vehicle_id)

        if vehicle is None:
            raise NotFoundError("Vehicle not found")

        sensor_data = {
            "vehicle_id": dto.vehicle_id,
            "engine_temperature": dto.engine_temperature,
            "oil_pressure": dto.oil_pressure,
            "battery_voltage": dto.battery_voltage,
            "brake_wear": dto.brake_wear
        }

        return self.repository.add_sensor_data(sensor_data)

    def get_vehicle_health(self, vehicle_id):
        vehicle = self.repository.get_vehicle_by_id(vehicle_id)

        if vehicle is None:
            raise NotFoundError("Vehicle not found")

        sensor_records = self.repository.get_sensor_data_by_vehicle_id(vehicle_id)

        if not sensor_records:
            raise NotFoundError("No sensor data found for this vehicle")

        latest_data = sensor_records[-1]

        issues = []
        status = "Healthy"

        if latest_data["engine_temperature"] > 105:
            issues.append("Engine temperature is too high")
            status = "Warning"

        if latest_data["oil_pressure"] < 20:
            issues.append("Oil pressure is too low")
            status = "Critical"

        if latest_data["battery_voltage"] < 11.8:
            issues.append("Battery voltage is low")
            if status != "Critical":
                status = "Warning"

        if latest_data["brake_wear"] > 80:
            issues.append("Brake wear is too high")
            status = "Critical"

        return {
            "vehicle": vehicle,
            "status": status,
            "issues": issues,
            "latest_sensor_data": latest_data,
            "recommendation": self._get_recommendation(status)
        }

    def _get_recommendation(self, status):
        if status == "Critical":
            return "Immediate inspection required"

        if status == "Warning":
            return "Vehicle should be checked soon"

        return "Vehicle condition is normal"