from . import views
from django.urls import path


urlpatterns = [
    path("", views.inicio),
    path("registro-anuncios/", views.registro_anuncios),
    path("guardar-anuncio/", views.guardar_anuncio),
    path("login-administracion/", views.login_administracion),
    path("administracion-anuncios/", views.administracion_anuncios),
    path("modificacion-anuncio/", views.modificacion_anuncio),
    ]