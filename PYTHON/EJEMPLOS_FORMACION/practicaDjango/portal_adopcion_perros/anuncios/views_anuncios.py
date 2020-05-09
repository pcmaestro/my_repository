from django.shortcuts import render, redirect
from . import models
from . import views_usuarios

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
    nombre = request.POST["nombre"]
    raza = request.POST["raza"]
    edad = request.POST["edad"]
    color_pelo = request.POST["pelo"]
    defectos_fisicos = request.POST["defectos"]
    vacunado = request.POST["vacunado"]
    categoria = request.POST["categoria"]
    #Guardar foto en construcción
    id_usuario = request.session["id_usuario"]
    anuncio = models.Perros(nombre = nombre, raza = raza, edad = edad, color_pelo = color_pelo,\
                           defectos_fisicos = defectos_fisicos, vacunado = vacunado, \
                           categoria_id = categoria, usuario_id = id_usuario)
    anuncio.save()
    #return views_usuarios.home_usuario(request)
    return redirect("/anuncios/home-usuario")


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
