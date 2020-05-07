from . import views_anuncios, views_usuarios
from django.urls import path


urlpatterns = [
    path("", views_anuncios.inicio),
    path("registro-usuario/", views_usuarios.registro_usuario),
    path("inicio-sesion-usuario/", views_usuarios.inicio_sesion_usuario),
    path("home-usuario/", views_usuarios.home_usuario),
    path("registro-anuncio/", views_anuncios.registro_anuncio),
    path("guardar-anuncio/", views_anuncios.guardar_anuncio),
    path("modificacion-anuncio/", views_anuncios.modificacion_anuncio),
    path("modificacion-usuario/", views_usuarios.modificacion_usuario),
    path("guardar-anuncio-modificado/", views_anuncios.guardar_anuncio_modificado),
    path("guardar-usuario-modificado/", views_usuarios.guardar_usuario_modificado),
    path("cerrar-sesion-usuario/", views_usuarios.cerrar_sesion_usuario),
    path("borrar-anuncio", views_anuncios.borrar_anuncio)
    
    ]