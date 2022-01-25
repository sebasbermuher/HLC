# Determine si School_bus también es una instancia de la clase Vehicle
# Dado:

# class Vehicle:
# def __init__(self, name, mileage, capacity):
# self.name = name
# self.mileage = mileage
# self.capacity = capacity

# class Bus(Vehicle):
#    pass

# School_bus = Bus("Volvo", 12, 50)


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))

if isinstance(School_bus, Vehicle) == True:
    print("School_bus es una instancia de Vehicle")
