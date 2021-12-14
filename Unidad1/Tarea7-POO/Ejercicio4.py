# Cree una clase Bus que herede de la clase de Vehicle. Proporcione al atributo capacidad
# mediante Bus.seating_capacity() un valor predeterminado de 50.

# Utilice el siguiente código para su clase Vehicle.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"La capacidad de asientos del autobús {self.name} es de {capacity} pasajeros"
# Resultado:

# La capacidad de asientos del autobús Socibus es de 50 pasajeros.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"La capacidad de asientos del autobús {self.name} es de {capacity} pasajeros"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


autobus = Bus("Socibus", 180, 12)
print(autobus.seating_capacity())
