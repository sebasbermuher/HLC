# Cree una clase hija Bus que herede de la clase Vehicle. El cargo por tarifa predeterminada
# de cualquier vehículo es la capacidad de asientos * 100. Si el vehículo es una instancia
# de Bus, debemos agregar un 10% adicional a la tarifa completa como cargo de mantenimiento.
# Por lo tanto, la tarifa total por instancia de autobús se convertirá en el monto
# final = tarifa total + 10% de la tarifa total.

# Nota: La capacidad de asientos del autobús es 50, por lo que el monto final de la tarifa
# debe ser 5500. Debe anular el método tarifa() de la clase de Vehicle en la clase Bus.

# Utilice el siguiente código para su clase de Vehicle principal. Necesitamos acceder a la
# clase principal desde dentro de un método de una clase hija.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def tarifa(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     pass

# School_bus = Bus("Volvo", 12, 50)
# print("La tarifa total del bus es:", School_bus.tarifa())
# Resultado:

# La tarifa total del bus es: 5500.0

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def tarifa(self):
        return self.capacity * 100


class Bus(Vehicle):
    def tarifa(self):
        super().tarifa()
        return self.capacity * 100 + 0.01 * self.capacity


School_bus = Bus("Volvo", 12, 50)
print("La tarifa total del bus es:", School_bus.tarifa())
