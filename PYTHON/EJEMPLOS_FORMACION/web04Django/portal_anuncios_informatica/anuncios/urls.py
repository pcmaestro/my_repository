from django.urls import path
# las funciones estan en views.py
# para importar todas esas funciones se pone:
from . import views

# aqui ponemos todas las rutas que debemos tener y que funcion
# se ejecuta ante cada una, esto es como cuando poniamos
# @app.route("/")
urlpatterns = [
    path("", views.inicio),
    path("registrar-anuncio", views.registrar_anuncio),
    path("guardar-nuevo-anuncio", views.guarda_nuevo_anuncio),



]