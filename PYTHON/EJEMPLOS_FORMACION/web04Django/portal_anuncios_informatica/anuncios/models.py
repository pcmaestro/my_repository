from django.db import models

# Create your models here.

class Categoria(models.Model):
    texto = models.CharField(max_length = 150)
    descripcion = models.CharField(max_length = 2000)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length = 150)
    clave = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150, unique = True)
    

class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    email = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE )
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE )
    

    
    

    