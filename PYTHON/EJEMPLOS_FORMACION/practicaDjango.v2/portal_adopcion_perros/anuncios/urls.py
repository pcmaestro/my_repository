from . import views_anuncios, views_usuarios
from django.urls import path

urlpatterns = [
    path("", views_anuncios.inicio),
    path("registro-usuario", views_usuarios.registro_usuario),
    path("guardar-usuario", views_usuarios.guardar_usuario),
    path("inicio-sesion-usuario", views_usuarios.inicio_sesion_usuario),
    path("guardar-sesion-usuario", views_usuarios.guardar_sesion_usuario),
    path("home-usuario", views_usuarios.home_usuario),
    path("volver-home", views_usuarios.volver_a_home),
    path("registro-anuncio", views_anuncios.registro_anuncio),
    path("guardar-anuncio", views_anuncios.guardar_anuncio),
    path("modificacion-anuncio/<id_anuncio>", views_anuncios.modificacion_anuncio),
    path("modificacion-usuario", views_usuarios.modificacion_usuario),    
    path("guardar-usuario-modificado/<id_usuario>", views_usuarios.guardar_usuario_modificado),
    path("cerrar-sesion-usuario", views_usuarios.cerrar_sesion_usuario),
    path("borrar-anuncio/<id_anuncio>", views_anuncios.borrar_anuncio),
    path("modificacion-anuncio/guardar-anuncio-modificado/<id_anuncio>", views_anuncios.guardar_anuncio_modificado)
    
    ]