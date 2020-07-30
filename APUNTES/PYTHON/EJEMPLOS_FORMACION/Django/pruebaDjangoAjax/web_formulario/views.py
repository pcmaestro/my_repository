import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import  forms
from . import  regexp
from . import models
import re

# Create your views here.

def inicio(request):
    formulario = forms.FormularioUsuario()
    context = {"formulario":formulario}
    return render(request, "index.html", context)

def guardar_formulario(request):
    context = {}
    if request.method == "POST":
        formulario = forms.FormularioUsuario(request.POST)
        publicidad = False
        if "publicidad" in request.POST:
            publicidad = True
        if formulario.is_valid():
            usuario = models.Usuario(nombre = formulario.clean_nombre(),
                                     apellido_1 = formulario.clean_apellido_1(),
                                     apellido_2 = formulario.clean_apellido_2(),
                                     telefono = formulario.clean_telefono(),
                                     email = formulario.clean_email(),
                                     publicidad = publicidad
                                     )
            usuario.save()
            formulario = forms.FormularioUsuario()

            context = {
                "formulario":formulario
            }
            return render(request, "index.html", context)
    else:
        formulario = forms.FormularioUsuario()
        context = {
            "formulario":formulario,
        }


    return render(request, "index.html", context)









