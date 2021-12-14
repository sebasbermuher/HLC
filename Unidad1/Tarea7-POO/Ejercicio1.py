# Crear una clase con atributos de instancia.
# Escribir un programa Python para crear una clase Vehicle con max_speedy y mileage
# como atributos.

class Vehicle:
    def __init__(self, max_speedy, mileage):
        self.max_speedy = max_speedy
        self.mileage = mileage


mivehiculo = Vehicle(120, 500)

print("La velocidad maxima de mi vehiculo es", mivehiculo.max_speedy)
print("El kilometraje de mi vehiculo es", mivehiculo.mileage)
