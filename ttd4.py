class Vehicle:
    def __init__(self, type: str, year: int, make: str, model: str, two_door: bool, has_sunroof: bool):
        self.vehicle_type = type
        self.year = year
        self.make = make
        self.model = model
        self.is_two_door = two_door
        self.has_sunroof = has_sunroof

    def __str__(self):
        return f"Vehicle Type: {self.vehicle_type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nDoors: {2 if self.is_two_door else 4}\nRoof Type: {'Sunroof' if self.has_sunroof else 'Solid roof'}"
    
print(Vehicle("Car", 2006, "Buick", "Lacrosse", False, False))