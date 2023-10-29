from vehicles import Bicycle, Car

class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand, model):
        pass

class ConcreteVehicleFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type, brand, model):
        if vehicle_type == "bicycle":
            return Bicycle(brand, model)
        elif vehicle_type == "car":
            return Car(brand, model)
        else:
            raise ValueError("Invalid vehicle type.")
