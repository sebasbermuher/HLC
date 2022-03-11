from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(
        max_length=60, verbose_name="Nombre completo del cliente")
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es {} y su precio es {}'.format(self.nombre, self.precio)


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
