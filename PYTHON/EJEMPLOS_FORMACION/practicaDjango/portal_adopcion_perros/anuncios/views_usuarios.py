from django.shortcuts import render
from django.http.response import HttpResponse
from . import models


def registro_usuario(request):
    return render(request, "registro-usuario.html")

def inicio_sesion_usuario(request):
    return render(request, "login.html")

def home_usuario(request):
    return render(request, "home.html", context = None)

def modificacion_usuario(request):
    return render(request, "modificacion-usuario.html")

def guardar_usuario_modificado(request):
    return home_usuario(request)

def cerrar_sesion_usuario(request):
    return render(request, "index.html")