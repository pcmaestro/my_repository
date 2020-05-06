from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# Create your views here.

def inicio(request):
    lista = models.Perros.objects.all()
    context = {"anuncios" : lista}    
    return render(request, "index.html", context)

def registro_anuncios(request):
    return render(request,"registro-anuncios.html")

def guardar_anuncio(request):
    OK = True    
    if OK:
        return render(request, "registro-anuncio-ok.html")
    if not OK:
        return render(request, "registro-anuncio-ko.html")

def login_administracion(request):
    return render(request, "login-administracion.html")

def administracion_anuncios(request):
    return render(request, "administracion-anuncios.html")

def modificacion_anuncio(request):
    return render(request, "modificacion-anuncio.html")

def guardar_anuncio_modificado(request):
    return render(request, "modificacion-ok.html")

