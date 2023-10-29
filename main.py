from vehicle_factory import ConcreteVehicleFactory

if __name__ == "__main__":
    vehicle_factory = ConcreteVehicleFactory()

    bicycle = vehicle_factory.create_vehicle("bicycle", "Trek", "FX3")
    car = vehicle_factory.create_vehicle("car", "Toyota", "Camry")

    print(bicycle.drive())
    print(car.drive())
