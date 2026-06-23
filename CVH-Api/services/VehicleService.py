class VehicleService:
    def __init__(self, repository):
        self.repository = repository

    def create_vehicle(self, dto):
        vehicle = {
            "vehicle_number": dto.vehicle_number,
            "vehicle_type": dto.vehicle_type,
            "manufacturer": dto.manufacturer,
            "model": dto.model,
            "mileage_km": dto.mileage_km
        }

        return self.repository.add_vehicle(vehicle)

    def get_all_vehicles(self):
        return self.repository.get_all_vehicles()