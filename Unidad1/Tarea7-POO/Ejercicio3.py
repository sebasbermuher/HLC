# Cree una clase Bus que heredará todas las variables y métodos de la clase Vehicle
# Dado:
# class Vehicle:
# def __init__(self, name, max_speed, mileage):
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
# Resultado:
# Nombre del vehículo: Volvo Velocidad: 180 Kilometraje: 12

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


autobus = Bus("Volvo", "180", "12")
print("Nombre del vehiculo:", autobus.name, ", Velocidad:",
      autobus.max_speed, ", Kilometraje:", autobus.mileage)
