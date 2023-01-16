from django.db import models

class Comercio(models.Model):
    nombre = models.CharField(max_length=128)
    categoria = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    horario = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre}, {self.categoria}, {self.direccion}, {self.horario}"


