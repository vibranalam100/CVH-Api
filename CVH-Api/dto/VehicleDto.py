from Exceptions import ValidationError


class CreateVehicleDTO:
    def __init__(self, vehicle_number, vehicle_type, manufacturer, model, mileage_km):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.manufacturer = manufacturer
        self.model = model
        self.mileage_km = mileage_km

    @staticmethod
    def from_dict(data):
        required_fields = [
            "vehicle_number",
            "vehicle_type",
            "manufacturer",
            "model",
            "mileage_km"
        ]

        for field in required_fields:
            if field not in data:
                raise ValidationError(f"{field} is required")

        if data["mileage_km"] < 0:
            raise ValidationError("mileage_km cannot be negative")

        return CreateVehicleDTO(
            vehicle_number=data["vehicle_number"],
            vehicle_type=data["vehicle_type"],
            manufacturer=data["manufacturer"],
            model=data["model"],
            mileage_km=data["mileage_km"]
        )