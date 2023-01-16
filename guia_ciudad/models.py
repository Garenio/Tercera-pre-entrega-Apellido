from django.db import models

class Comercio(models.Model):
    nombre = models.CharField(max_length=128)
    categoria = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    horario = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre}, {self.categoria}, {self.direccion}, {self.horario}"

class Restaurant(models.Model):
    nombre = models.CharField(max_length=128)
    especialidad = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    horario = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre}, {self.especialidad}, {self.direccion}, {self.horario}"

class Propiedad(models.Model):
    tipo = models.CharField(max_length=128)
    operacion = models.CharField(max_length=128)
    habitaciones = models.IntegerField()
    precio = models.IntegerField()
    contacto = models.EmailField()

    def __str__(self):
        return f"{self.tipo}, {self.operacion}, {self.habitaciones}, {self.precio}, {self.contacto}"

class Clasificado(models.Model):
    producto = models.CharField(max_length=128)
    descripcion = models.TextField()
    precio = models.IntegerField()
    contacto = models.EmailField()

    def __str__(self):
        return f"{self.producto}, {self.descripcion}, {self.precio}, {self.contacto}"