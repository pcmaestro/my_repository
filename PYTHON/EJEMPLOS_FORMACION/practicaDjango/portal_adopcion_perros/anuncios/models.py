from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length = 100)
    
class Perros(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 100)
    edad = models.IntegerField()
    color_pelo = models.CharField(max_length = 20)
    defectos_fisicos = models.BooleanField(default = False)
    vacunado = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categorias, on_delete = models.DO_NOTHING)
    
