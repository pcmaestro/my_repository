from django.shortcuts import render, redirect
from . import models
from . import views_usuarios
import re

# Create your views here.

def inicio(request):
    lista = models.Perros.objects.all()   
    context = {
        "anuncios" : lista
        }    
    return render(request, "index.html", context)
    
def registro_anuncio(request):
    return render(request,"registro-anuncio.html")

def guardar_anuncio(request):
    patron_texto = r"^[a-zA-Z0-9]+\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*$"
    patron_edad = r"^[0-9]{1,2}$"
    
    validador_texto = re.compile(patron_texto)
    validador_edad = re.compile(patron_edad)
    
    nombre = request.POST["nombre"]
    raza = request.POST["raza"]
    edad = request.POST["edad"]
    color_pelo = request.POST["pelo"]
    defectos_fisicos = request.POST["defectos"]
    vacunado = request.POST["vacunado"]
    categoria = request.POST["categoria"]
    #Guardar foto en construcción
    
    validacion_nombre = validador_texto.match(nombre)
    validacion_raza = validador_texto.match(raza)
    validacion_edad = validador_edad.match(edad)
    validacion_color_pelo = validador_texto.match(color_pelo)
    
    #inicio de variable validacion_combos
    validacion_combos = True
    
    #inicio de variable validacion
    validacion = True
    
    if defectos_fisicos == "null" or vacunado == "null" or categoria == "null":
        validacion_combos = False       
    
    if validacion_nombre and validacion_raza and validacion_edad and validacion_color_pelo and validacion_combos:
        
        validacion = True
        
    else:
        validacion = False
        
    if validacion == True:
        
        id_usuario = request.session["id_usuario"]
        anuncio = models.Perros(nombre = nombre, raza = raza, edad = edad, color_pelo = color_pelo,\
                               defectos_fisicos = defectos_fisicos, vacunado = vacunado, \
                               categoria_id = categoria, usuario_id = id_usuario)
        anuncio.save()        
        return redirect("/anuncios/home-usuario")
    else:
        context = {
            "error_campo" : "Alguno de los campos es erróneo"
            }
        return render(request,"registro-anuncio.html", context)       


def modificacion_anuncio(request, id_anuncio):    
    anuncio = models.Perros.objects.get(pk = id_anuncio)
    context = {
        "nombre" : anuncio.nombre, "raza" : anuncio.raza, "edad" : anuncio.edad, \
        "pelo" : anuncio.color_pelo, "defectos" : anuncio.defectos_fisicos, \
        "vacunado" : anuncio.vacunado, "id_anuncio" : id_anuncio
        }
    return render(request, "modificacion-anuncio.html", context)

def guardar_anuncio_modificado(request, id_anuncio):    
    nombre = request.POST["nombre"]
    raza = request.POST["raza"]
    edad = request.POST["edad"]
    color_pelo = request.POST["pelo"]
    defectos_fisicos = request.POST["defectos"]
    vacunado = request.POST["vacunado"]
    anuncio = models.Perros.objects.get(pk = id_anuncio)
    anuncio.nombre = nombre
    anuncio.raza = raza
    anuncio.edad = edad
    anuncio.color_pelo = color_pelo
    anuncio.defectos_fisicos = defectos_fisicos
    anuncio.vacunado = vacunado
    anuncio.save()                           
                           
    return redirect("/anuncios/home-usuario")

def borrar_anuncio(request, id_anuncio):    
    anuncio = models.Perros.objects.get(pk = id_anuncio)
    anuncio.delete()
    return redirect("/anuncios/home-usuario")
