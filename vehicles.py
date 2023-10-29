class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        pass

class Bicycle(Vehicle):
    def drive(self):
        return f"Riding the {self.brand} {self.model} bicycle."

class Car(Vehicle):
    def drive(self):
        return f"Driving the {self.brand} {self.model} car."
