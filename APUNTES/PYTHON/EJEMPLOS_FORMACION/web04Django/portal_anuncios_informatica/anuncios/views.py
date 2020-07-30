from django.shortcuts import render
from . import models
#para poder ver las sql que lanza django:
import logging
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from . import utilidades
from django.utils import timezone

# esto es como el flask_app que teniamos antes pero solo para anuncios

def inicio(request):
    
    
    l = logging.getLogger('django.db.backends') 
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())
    
    
    #la siguiente linea recoge de base de datos todos los anuncios
    #ordenador por id de menor a mayor, fijarse en el menos de -id
    res = models.Anuncio.objects.order_by("-id").prefetch_related('categoria','usuario')
    
    #django emplea una ejecucion diferida de la sql, hasta que no usemos realmente 
    # un resutlado, podemos agregar filtrados sobre el mismo. 
    titulo_buscador = ""
    if "titulo" in request.GET:
        res = res.filter( titulo__contains = request.GET["titulo"])
        titulo_buscador = request.GET["titulo"]
    
    
        
    #parte de paginacion:
    resultados_por_pagina = 5
    comienzo = 0
    if "comienzo" in request.GET :
        comienzo = int(request.GET["comienzo"])
    res = res[comienzo:comienzo + resultados_por_pagina]
    total_resultados = models.Anuncio.objects.filter(titulo__contains = titulo_buscador).count()
    
    
    siguiente = comienzo + 5
    anterior = comienzo - 5
    context = {
            "anuncios" : res,
            "titulo_buscador" : titulo_buscador,
            "siguiente" : siguiente,
            "anterior" : anterior,
            "total_resultados": total_resultados
        }
    return render(request,"index.html",context)

def registrar_anuncio(request):
    
    res = models.Categoria.objects.order_by("id")
    context = {
            "categorias" : res
        }
    return render(request,"formulario-registro-anuncio.html",context)

def guarda_nuevo_anuncio(request):
    titulo_introducido = request.POST["titulo"]
    precio_introducido = request.POST["precio"].replace(",",".")
    categoria_id = request.POST["categoria_id"]
    
    categoria = models.Categoria.objects.get(pk = categoria_id)
    usuario = models.Usuario.objects.get(pk = request.session["id_usuario"])
    
    anuncio = models.Anuncio(titulo = titulo_introducido, precio = precio_introducido, email = usuario.email)
    anuncio.ip = utilidades.obtener_ip(request)
    anuncio.ultima_modificacion = timezone.now()
    anuncio.categoria_id = categoria_id
    anuncio.usuario = usuario
    anuncio.save()
    #despues de guardar el anuncio, vammos a guardar la imagen con un nombre 
    #igual al del id 
    id_anuncio = anuncio.id #django a metido la id generada en anuncioç
    ruta = "anuncios/static/imagenes/" + str(id_anuncio) + ".jpg"
    f = request.FILES["foto"]#name del input type file
    default_storage.save(ruta, ContentFile(f.read()))   
     
    return render(request,"registro-ok.html")


def registrar_usuario(request):
    
    return render(request,"formulario-registro-usuario.html")


def guardar_nuevo_usuario(request):
    
    nombre_insertado = request.POST["nombre"]
    email_insertado = request.POST["email"].lower().strip()
    clave_insertada = request.POST["clave"]
    
    res = models.Usuario.objects.filter(email = email_insertado)
     
    if len(res) == 1 :
        #email no disponible
        context = {
                "error_email" : "ya hay un usuario con ese email" 
            }
        return render(request,"formulario-registro-usuario.html",context)
    else:
        usuario = models.Usuario(nombre = nombre_insertado, email = email_insertado, clave = clave_insertada)
        usuario.save()
        return render(request,"registro-usuario-ok.html")



def login_usuario(request):
    return render(request,"login-usuario.html")

def identificar_usuario(request):
    
    email_insertado = request.POST["email"]
    clave_insertada = request.POST["clave"]
    
    res = models.Usuario.objects.filter(email = email_insertado, clave = clave_insertada)
    
    if len(res) == 0:
        context = {
            "error_login" : "email o contraseña incorrecta"
            }
        return render(request,"login-usuario.html",context)
    else:
        usuario = res[0]
        request.session["id_usuario"] = usuario.id
        
        context = {
            "nombre" : usuario.nombre
            }        
        return render(request,"login-ok.html", context)


def logout(request):
    request.session.clear()
    #para que vuelva a listar los anuncios paso la ejecucion a la funcion inicio
    # que ya hace eso
    return inicio(request)#redirect("/anuncios")


def mis_anuncios(request):
    usuario_actual = models.Usuario.objects.get(pk = request.session["id_usuario"])
    res = models.Anuncio.objects.filter(usuario = usuario_actual).order_by('-id')
    context = {
        "anuncios" : res
        }
    return render(request,"anuncios-usuario.html",context)


def borrar_anuncio(request):
    id = request.GET["id"]
    models.Anuncio.objects.get(pk = id).delete()
    return mis_anuncios(request)


def editar_anuncio(request):
    id = request.GET["id"]
    anuncio_a_editar = models.Anuncio.objects.get(pk = id)
    context = {
        "anuncio" : anuncio_a_editar,
        "categorias" : models.Categoria.objects.order_by("id")
        }
    return render(request,"editar-anuncio.html", context)
    
    
def guardar_cambios_anuncio(request):
    
    anuncio = models.Anuncio.objects.get(pk = request.POST["id_anuncio"])
    anuncio.titulo = request.POST["titulo"]
    anuncio.precio = request.POST["precio"].replace(",",".")
    categoria = models.Categoria.objects.get(pk = request.POST["categoria_id"])
    anuncio.categoria = categoria
    anuncio.ultima_modificacion = timezone.now()
    anuncio.save()
    
    #guardar imagen si la hay
    if "foto" in request.FILES:
        ruta = "anuncios/static/imagenes/" + str(anuncio.id) + ".jpg"
        f = request.FILES["foto"]#name del input type file
        default_storage.delete(ruta)
        default_storage.save(ruta, ContentFile(f.read()))   
    
    
    return mis_anuncios(request)
    
    
    
    
    
    
    
    


