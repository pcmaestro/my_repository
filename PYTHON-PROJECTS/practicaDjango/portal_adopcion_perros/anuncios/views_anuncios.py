from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from . import models
import re
import os
from django.utils import timezone
from . import utilities

# Create your views here.

def inicio(request):
    anuncios = models.Perros.objects.all().order_by("-ultima_modificacion" ,"-id").prefetch_related("categoria", "usuario")

    criterio = ""
    valor_en_buscador = ""
    filtrado = False

    if "criterio" in request.GET:
        criterio = request.GET["criterio"]
        filtrado = True
        if len(anuncios.filter(nombre__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower().title())) != 0:
            anuncios = anuncios.filter(nombre__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower().title())
        elif len(anuncios.filter(raza__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower().title())) != 0:
            anuncios = anuncios.filter(raza__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower().title())
        elif len(anuncios.filter(edad__contains=criterio)) != 0:
            anuncios = anuncios.filter(edad__contains=criterio)
        elif len(anuncios.filter(color_pelo__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower())) != 0:
            anuncios = anuncios.filter(color_pelo__contains=criterio.replace("áéíóúÁÉÍÓÚ", "aeiouAEIOU").lower())
        elif len(anuncios.filter(defectos_fisicos__contains=criterio)) != 0:
            anuncios = anuncios.filter(defectos_fisicos__contains=criterio)
        elif len(anuncios.filter(vacunado__contains=criterio)) != 0:
            anuncios = anuncios.filter(vacunado__contains=criterio)
        else:
            categorias = models.Categorias.objects.filter(categoria__contains=criterio.replace("áéíóú", "aeiou").replace("ÁÉÍÓÚ", "AEIOU").lower().capitalize())
            anuncios_finales = []

            for c in categorias:
                anuncios_finales.extend(anuncios.filter(categoria=c))
            anuncios = anuncios_finales

    valor_en_buscador = criterio
    valor_buscado = criterio
    anuncios_totales = len(anuncios)
    comienzo = 0

    if "comienzo" in request.GET:
        comienzo = int(request.GET["comienzo"])

    paginacion = 5
    paginado = anuncios[comienzo:comienzo + paginacion]
    longitud_paginado = len(paginado)
    siguiente = comienzo + paginacion
    anterior = comienzo - paginacion

    context = {
        "anuncios" : paginado, 
        "anuncios_totales" : anuncios_totales, 
        "siguiente" : siguiente,
        "anterior": anterior,
        "valor_en_buscador": valor_en_buscador,
        "limpiar": "LIMPIAR BUSQUEDA",
        "filtrado": filtrado,
        "valor_buscado" : valor_buscado,
        "paginacion" : paginacion

        }    
    return render(request, "index.html", context)
    
def registro_anuncio(request):
    return render(request,"registro-anuncio.html")

def guardar_anuncio(request):
    patron_texto = r"^[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]+\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*$"
    patron_edad = r"^[0-9]{1,2}$"
    
    validador_texto = re.compile(patron_texto)
    validador_edad = re.compile(patron_edad)
    
    nombre = request.POST["nombre"].lower().title()
    raza = request.POST["raza"].lower().title()
    edad = request.POST["edad"]
    color_pelo = request.POST["pelo"].lower()
    defectos_fisicos = request.POST["defectos"]
    vacunado = request.POST["vacunado"]
    categoria = request.POST["categoria"]

    
    validacion_nombre = validador_texto.match(nombre)
    validacion_raza = validador_texto.match(raza)
    validacion_edad = validador_edad.match(edad)
    validacion_color_pelo = validador_texto.match(color_pelo)
    
    if "id_usuario" in request.session:
    
        #inicio de variable validacion_combos
        validacion_combos = True
        
        #inicio de variable validacion
        validacion = True
        
        if defectos_fisicos == "null" or vacunado == "null" or categoria == "null":
            validacion_combos = False       
        
        if validacion_nombre and validacion_raza and validacion_edad and validacion_color_pelo and validacion_combos:
            
            validacion = True
            
        else:
            validacion = False
            
        if validacion == True:
            
            id_usuario = request.session["id_usuario"]
            anuncio = models.Perros(nombre = nombre, 
                                    raza = raza, 
                                    edad = edad, 
                                    color_pelo = color_pelo,
                                    defectos_fisicos = defectos_fisicos, 
                                    vacunado = vacunado,
                                    categoria_id = categoria, 
                                    usuario_id = id_usuario,
                                    ultima_modificacion = timezone.now(),
                                    ip = utilities.obtener_ip(request)
                                    )
            anuncio.save()
            if "foto" in request.FILES:
                foto = request.FILES["foto"]
                id_anuncio = anuncio.id
                ruta = "anuncios/static/fotos/" + str(id_anuncio) + ".jpg"
                default_storage.save(ruta, ContentFile(foto.read()))
            return redirect("/anuncios/home-usuario")
        else:
            context = {
                "error_campo" : "Alguno de los campos es erróneo"
                }
            return render(request,"registro-anuncio.html", context)       
        
    else:
        return redirect("/anuncios/inicio-sesion-usuario")

def modificacion_anuncio(request, id_anuncio):  
    if "id_usuario" in request.session:
        id_usuario = request.session["id_usuario"]
        anuncio = models.Perros.objects.get(pk = id_anuncio)
        context = {
            "nombre" : anuncio.nombre, 
            "raza" : anuncio.raza, 
            "edad" : anuncio.edad,
            "pelo" : anuncio.color_pelo, 
            "defectos" : int(anuncio.defectos_fisicos),
            "vacunado" : anuncio.vacunado, 
            "id_anuncio" : id_anuncio,
            "id_usuario" : id_usuario
            }
        return render(request, "modificacion-anuncio.html", context)
    else:
        return redirect("/anuncios/inicio-sesion-usuario")

def guardar_anuncio_modificado(request, id_anuncio):
    patron_texto = r"^[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]+\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*$"
    patron_edad = r"^[0-9]{1,2}$"

    validador_texto = re.compile(patron_texto)
    validador_edad = re.compile(patron_edad)

    nombre = request.POST["nombre"].lower().title()
    raza = request.POST["raza"].lower().title()
    edad = request.POST["edad"]
    color_pelo = request.POST["pelo"].lower()
    defectos_fisicos = request.POST["defectos"]
    vacunado = request.POST["vacunado"]
    categoria = request.POST["categoria"]

    validacion_nombre = validador_texto.match(nombre)
    validacion_raza = validador_texto.match(raza)
    validacion_edad = validador_edad.match(edad)
    validacion_color_pelo = validador_texto.match(color_pelo)
    
    if "id_usuario" in request.session:

        # inicio de variable validacion_combos
        validacion_combos = True
    
        # inicio de variable validacion
        validacion = True
    
        if defectos_fisicos == "null" or vacunado == "null" or categoria == "null":
            validacion_combos = False
    
        if validacion_nombre and validacion_raza and validacion_edad and validacion_color_pelo and validacion_combos:
    
            validacion = True
    
        else:
            validacion = False
    
        if validacion == True:
    
            anuncio = models.Perros.objects.get(pk=id_anuncio)
            anuncio.nombre = nombre
            anuncio.raza = raza
            anuncio.edad = edad
            anuncio.color_pelo = color_pelo
            anuncio.defectos_fisicos = defectos_fisicos
            anuncio.vacunado = vacunado
            anuncio.categoria_id = categoria
            anuncio.ultima_modificacion = timezone.now()
            anuncio.save()
            if "foto" in request.FILES:
                existe_foto_anterior = os.path.isfile("anuncios/static/fotos/" + str(anuncio.id) + ".jpg")
                if existe_foto_anterior:
                    foto_anterior = "anuncios/static/fotos/" + str(anuncio.id) + ".jpg"
                    os.remove(foto_anterior)
                nueva_foto = request.FILES["foto"]
                ruta = "anuncios/static/fotos/" + str(anuncio.id) + ".jpg"
                default_storage.save(ruta, ContentFile(nueva_foto.read()))
            return redirect("/anuncios/home-usuario")
        else:
            context = {
                "error_campo": "Debe seleccionar alguna opción en los desplegables",
            }
            return render(request, "modificacion-anuncio.html", context)

    else:
        return redirect("/anuncios/inicio-sesion-usuario")

def borrar_anuncio(request, id_anuncio):
    if "id_usuario" in request.session:
        anuncio = models.Perros.objects.get(pk = id_anuncio)
        anuncio.delete()
        return redirect("/anuncios/home-usuario")
    else:
        return redirect("/anuncios/inicio-sesion-usuario")


