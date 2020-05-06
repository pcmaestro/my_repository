from django.contrib import admin

from django.urls import path

from django.urls.conf import include


# aqui ponemos todas las rutas que debemos tener y que funcion
# se ejecuta ante cada una, esto es como cuando poniamos
# @app.route("/")
urlpatterns = [
    path('anuncios/',include("anuncios.urls")),
    path('admin/', admin.site.urls),
]