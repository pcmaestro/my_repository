from django.shortcuts import render
from django.http.response import HttpResponse
from . import models
from . import views_usuarios

# Create your views here.

def inicio(request):
    lista = models.Perros.objects.all()
    context = {"anuncios" : lista}    
    return render(request, "index.html", context)

def registro_anuncio(request):
    return render(request,"registro-anuncio.html")

def guardar_anuncio(request):
    return views_usuarios.home_usuario(request)


def modificacion_anuncio(request):
    return render(request, "modificacion-anuncio.html")

def guardar_anuncio_modificado(request):
    return views_usuarios.home_usuario(request)

def borrar_anuncio(request):
    return views_usuarios.home_usuario(request)
