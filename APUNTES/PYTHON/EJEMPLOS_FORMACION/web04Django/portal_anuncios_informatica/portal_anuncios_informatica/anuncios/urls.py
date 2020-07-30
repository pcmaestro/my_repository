from django.urls import path
#las funciones estan en views.py
#para importar todas esas funciones se pone:
from . import views

#aqui ponemos todas las rutas que debemos tener y que funcion
#se ejecuta ante cada una, esto es como cuando poniamos
#@app.route("/")
urlpatterns = [
    path("",views.inicio),
    path("registrar-anuncio", views.registrar_anuncio),
    path("guardar-nuevo-anuncio", views.guarda_nuevo_anuncio),
    path("registrar-usuario",views.registrar_usuario),
    path("guardar-nuevo-usuario",views.guardar_nuevo_usuario),
    path("login-usuario",views.login_usuario),
    path("identificar-usuario",views.identificar_usuario),
    path("logout",views.logout),
    path("mis-anuncios",views.mis_anuncios),
    path("borrar-anuncio",views.borrar_anuncio),
    path("editar-anuncio",views.editar_anuncio),
    path("guardar-cambios-anuncio",views.guardar_cambios_anuncio)
    ]

