from django.db import models

class aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=11, unique=True,primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
