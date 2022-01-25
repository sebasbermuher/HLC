# Defina una propiedad que debe tener el mismo valor para cada instancia de clase (objeto).
# Defina un atributo de clase color con un valor predeterminado blanco.
# Es decir, todos los vehículos deben ser blancos.

# Utilice el siguiente código para este ejercicio.

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass
# Resultado:

# Color: Blanco, Nombre del vehículo: Volvo, Velocidad: 180, Kilometraje: 12
# Color: Blanco, Nombre del vehículo: Audi Q5, Velocidad: 240, Kilometraje: 18

class Vehicle:
    color = "Blanco"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


autobus = Bus("Volvo", 180, 12)
coche = Car("Audi Q5", 240, 18)
print("Color:", autobus.color,
      ", Nombre del vehículo:", autobus.name, ", Velocidad:", autobus.max_speed, ", Kilometraje:", autobus.mileage)
print("Color:", coche.color, ", Nombre del vehículo:", coche.name,
      ", Velocidad:", coche.max_speed, ", Kilometraje:", coche.mileage)
