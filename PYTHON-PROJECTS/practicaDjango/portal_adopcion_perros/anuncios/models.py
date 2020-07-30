from django.db import models


# Create your models here.

class Categorias(models.Model):
    categoria = models.CharField(max_length = 100)

    def __str__(self):
        return self.categoria
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido_1 = models.CharField(max_length = 100)
    apellido_2 = models.CharField(max_length = 100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 10)
    email_validado = models.BooleanField(default = False)

    def __str__(self):
        return self.nombre + " " + self.apellido_1  + " " + self.apellido_2 + \
               " --Tf : " + str(self.telefono) + " --Email : " + self.email + " --Email validado : " + self.email.validado
    
    
class Perros(models.Model):
    nombre = models.CharField(max_length = 100)
    raza = models.CharField(max_length = 100)
    edad = models.IntegerField()
    color_pelo = models.CharField(max_length = 20)
    defectos_fisicos = models.BooleanField(default = False)
    vacunado = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    ultima_modificacion = models.DateTimeField("fecha ultima modificacion")
    ip = models.CharField(max_length= 100)

    def __str__(self):
        return "Nombre : " + self.nombre + " --Raza : " + \
               self.raza + " --Edad : " + str(self.edad) + \
               " --Color de pelo : " + self.color_pelo + \
               " --Defectos fisicos " + str(self.defectos_fisicos) +\
               " --Vacunado : " + str(self.vacunado) + " --Categoria : " + str(self.categoria) + \
               " --Usuario de registro : " + str(self.usuario)  + " --Ultima modificación " + str(self.ultima_modificacion)[0:16] + \
               " --IP usuario " + self.ip
