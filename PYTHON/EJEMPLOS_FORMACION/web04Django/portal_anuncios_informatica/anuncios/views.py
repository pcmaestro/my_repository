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
    return render(request, "formulario-registro-anuncio.html")


def guarda_nuevo_anuncio(request):
    titulo_introducido = request.GET["titulo"]
    precio_introducido = request.GET["precio"]
    email_introducido = request.GET["email"]

    anuncio = models.Anuncio(titulo=titulo_introducido, precio=precio_introducido, email=email_introducido)
    anuncio.save()

    return render(request, "registro-ok.html")