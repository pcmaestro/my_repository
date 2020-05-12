from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length = 100)

    def __str__(self):
        return "categoroa : " + self.categoria
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido_1 = models.CharField(max_length = 100)
    apellido_2 = models.CharField(max_length = 100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 10)  

    def __str__(self):
        return "Nombre : " + self.nombre + " Primer apellido : " + self.apellido_1 + " Segundo apellido : " + self.apellido_2 + " Tf : " + str(self.telefono) + " email : " + self.email + " password : " + self.password
    
    
class Perros(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 100)
    edad = models.IntegerField()
    color_pelo = models.CharField(max_length = 20)
    defectos_fisicos = models.BooleanField(default = False)
    vacunado = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)

    def __str__(self):
        return "Nombre : " + self.nombre + " raza : " + self.raza + " edad : " + str(self.edad) + " color de pelo : " + self.color_pelo + " defectos fisicos " + str(self.defectos_fisicos) + " vacunado : " + str(self.vacunado) + " categoria : " + str(self.categoria) + " usaurio de registro : " + str(self.usuario)
