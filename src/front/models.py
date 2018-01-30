from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento')

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField('Fecha de nacimiento')
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='mascotas')
