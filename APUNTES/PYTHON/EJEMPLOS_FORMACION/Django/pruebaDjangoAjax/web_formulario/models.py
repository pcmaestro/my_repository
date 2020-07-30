from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length= 20)
    apellido_1 = models.CharField(max_length= 50)
    apellido_2 = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField(max_length= 100)
    publicidad = models.BooleanField()

