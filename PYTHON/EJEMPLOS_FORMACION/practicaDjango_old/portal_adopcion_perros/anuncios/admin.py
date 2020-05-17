from django.contrib import admin

from . import models

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido_1", "apellido_2", "telefono", "email")
    
    def __str__(self):
        return "Nombre : " + self.nombre + " Primer apellido : " + self.apellido_1 + " Segundo apellido : " + self.apellido_2 + " Tf : " + str(self.telefono) + " email : " + self.email

admin.site.register(models.Categorias)
admin.site.register(models.Usuarios, UsuariosAdmin)
admin.site.register(models.Perros)