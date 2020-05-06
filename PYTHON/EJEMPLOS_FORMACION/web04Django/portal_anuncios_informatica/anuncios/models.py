from django.db import models

# Create your models here.

class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    email = models.CharField(max_length=150)