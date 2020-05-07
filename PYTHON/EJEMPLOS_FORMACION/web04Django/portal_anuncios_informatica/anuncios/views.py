from django.shortcuts import render
from django.http.response import HttpResponse
from . import models


# esto es como el flask_app que teniamos antes pero solo para anuncios

def inicio(request):
    #la siguiente linea recoge de base de datos todos los anuncios
    #ordenador por id de menor a mayor, fijarse en el menos de -id
    res = models.Anuncio.objects.order_by("-id")
    context = {
            "anuncios" : res
        }
    return render(request,"index.html",context)

def registrar_anuncio(request):
    
    res = models.Categoria.objects.order_by("id")
    context = {
            "categorias" : res
        }
    return render(request,"formulario-registro-anuncio.html",context)


def guarda_nuevo_anuncio(request):
    titulo_introducido = request.GET["titulo"]
    precio_introducido = request.GET["precio"].replace(",",".")
    categoria_id = request.GET["categoria_id"]
    
    categoria = models.Categoria.objects.get(pk = categoria_id)
    usuario = models.Usuario.objects.get(pk = request.session["id_usuario"])
    
    anuncio = models.Anuncio(titulo = titulo_introducido, precio = precio_introducido, email = usuario.email)
    anuncio.categoria = categoria
    anuncio.usuario = usuario
    anuncio.save()
     
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
    return inicio(request)

def mis_anuncios(request):
    return HttpResponse("Mostrar sólo los anuncios el usuario actual")

def mis_anuncios(request):
    usuario_actual = models.Usuario.objects.get(pk = request.session["id_usuario"])
    res = models.Anuncio.objects.filter(usuario = usuario_actual)
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
    anuncio.precio = request.POST["precio"].replace(",", ".")
    categoria = models.Categoria.objects.get(pk = request.POST["categoria_id"])
    anuncio.categoria = categoria
    anuncio.save()
    
    return mis_anuncios(request)


