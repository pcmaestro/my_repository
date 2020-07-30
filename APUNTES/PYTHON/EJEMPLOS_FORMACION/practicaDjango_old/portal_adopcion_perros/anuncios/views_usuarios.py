from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
import email
from . import views_anuncios
import re
from django.utils import timezone
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import JsonResponse


def registro_usuario(request):    
    return render(request, "registro-usuario.html")

def guardar_usuario(request):
    if request.method == "POST":
        patron_texto = r"^[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]+\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*$"
        patron_telefono = r"^[6-9]{1}[0-9]{8}$"
        patron_mail = r"^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        patron_password = r"[a-zñA-ZÑ0-9_-]{4,8}$"
        
        validador_texto = re.compile(patron_texto)
        validador_telefono = re.compile(patron_telefono)
        validador_mail = re.compile(patron_mail)
        validador_password = re.compile(patron_password)   
        
        nombre = request.POST["nombre"].lower().title()
        apellido_1 = request.POST["apellido_1"].lower().title()
        apellido_2 = request.POST["apellido_2"].lower().title()
        telefono = request.POST["telefono"]
        email = request.POST["email"]  
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]        
            
        if password1 == password2:
            password = password2
        
        #Variable para comprobar en la BD si el mail ya está registrado    
        comprobacion_mail = email
        
        validacion_nombre = validador_texto.match(nombre)
        validacion_apellido_1 = validador_texto.match(apellido_1)
        validacion_apellido_2 = validador_texto.match(apellido_2)
        validacion_telefono = validador_telefono.match(telefono)
        validacion_mail = validador_mail.match(email)
        validacion_password = validador_password.match(password)
        validacion_email_duplicado = len(models.Usuarios.objects.filter(email = comprobacion_mail))
        
        validacion = True
        
        if validacion_nombre and validacion_apellido_1 and validacion_apellido_2 and validacion_telefono and validacion_mail and validacion_password:
            validacion1 = True
        else:
            validacion1 = False

        if validacion_email_duplicado == 0:
            validacion2 = True
        else:
            validacion2 = False


        if validacion1 == True and validacion2 == True:
            nuevo_usuario = models.Usuarios(nombre = nombre,
                                            apellido_1 = apellido_1,
                                            apellido_2 = apellido_2,
                                            telefono = telefono,
                                            email = email,
                                            password = password
                                            )
            nuevo_usuario.save()
            usuario = models.Usuarios.objects.get(email = email)
            request.session["id_usuario"] = usuario.id

            template = get_template("correo.html")
            context = {"id_usuario" : usuario.id}
            content = template.render(context)

            mailing = EmailMultiAlternatives(
                "Bienvenido al portal de adopción de perros",
                "Bienvenido al portal de adopción de perros",
                settings.EMAIL_HOST_USER,
                [usuario.email]
            )

            mailing.attach_alternative(content, "text/html")

            mailing.send()

            return render(request,"gracias.html")

        elif validacion1 == False and validacion2 == False:
            errores_registro = '''
            Revise que todos los campos son correctos:

                Los campos de nombre y apellidos sólo pueden contender texto sin acentos.

                El campo Telefono debe contener un número español de 9 dígitos.

                El campo Email debe contener una dirección de correo válida que no se encentre ya registrada en el sistema.

                El campo Contraseña debe contener numeros o letras entre 4 y 8 digitos.
            '''
            mail = request.POST["email"]
            context = {
                "errores_registro" : errores_registro,
                "mail_duplicado": "La dirección " + mail + " ya está registrada en el sistema"
                    }

            return render(request, "registro-usuario.html", context)

        elif validacion1 == False:
            errores_registro = '''
            Revise que todos los campos son correctos:
            
                Los campos de nombre y apellidos sólo pueden contender texto sin acentos.
            
                El campo Telefono debe contener un número español de 9 dígitos.
            
                El campo Email debe contener una dirección de correo válida que no se encentre ya registrada en el sistema.
            
                El campo Contraseña debe contener numeros o letras entre 4 y 8 digitos.
            '''
            context = { "errores_registro" : errores_registro}
            return render(request, "registro-usuario.html", context)

        elif validacion2 == False:
            mail = request.POST["email"]
            context = {"mail_duplicado": "La dirección " + mail + " ya está registrada en el sistema"}
            return render(request, "registro-usuario.html", context)



def inicio_sesion_usuario(request):    
    return render(request, "login.html")

def guardar_sesion_usuario(request):
    email = request.POST["email"]
    password = request.POST["password"]
    comprobacion = models.Usuarios.objects.filter(email = email, password = password)
    context = {}    
    if len(comprobacion) == 1:
        usuario = comprobacion[0] 
        anuncios_usuario = models.Perros.objects.filter(usuario_id = usuario.id)    
        request.session["id_usuario"] = usuario.id
        context = {
            "nombre" : usuario.nombre + " " + usuario.apellido_1 +
            " " + usuario.apellido_2, "mis_anuncios" : anuncios_usuario
            }
        return render(request,"home.html", context)
    else:
        context = {"error_login" : "El usuario o la contraseña son incorrectos"}
        return render(request, "login.html", context)


def home_usuario(request):
    if "id_usuario" in request.session:
        id_usuario = request.session["id_usuario"]
        usuario = models.Usuarios.objects.get(pk = id_usuario)    
        anuncios_usuario = models.Perros.objects.filter(usuario_id = usuario.id).order_by("-ultima_modificacion","-id").prefetch_related("categoria", "usuario")
        email_ok = False
        if usuario.email_validado == True:
            email_ok = True
        context = {
            "nombre" : usuario.nombre + " " + usuario.apellido_1 + " " + usuario.apellido_2,
            "mis_anuncios" : anuncios_usuario,
            "email_validado": email_ok,
        }
        return render(request, "home.html", context)
    else:
        return redirect("/anuncios/inicio-sesion-usuario")


def validar_correo(request):
    id_usuario = request.GET["id_usuario"]
    usuario = models.Usuarios.objects.get(pk = id_usuario)
    usuario.email_validado = True
    usuario.save()
    return render(request, "email_validado.html")

def modificacion_usuario(request):
    if "id_usuario" in request.session:
        id_usuario = request.session["id_usuario"]
        usuario = models.Usuarios.objects.get(pk = id_usuario)
        context = {
            "nombre":usuario.nombre, "apellido_1":usuario.apellido_1, "apellido_2":usuario.apellido_2,\
            "telefono":usuario.telefono, "email":usuario.email, "id_usuario":id_usuario
            }
        return render(request, "modificacion-usuario.html", context)
    else:
        return redirect("/anuncios/inicio-sesion-usuario")

def guardar_usuario_modificado(request,id_usuario):
    patron_texto = r"^[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]+\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*\s?[a-zñA-ZÑáéíóúÁÉÍÓÚ0-9]*$"
    patron_telefono = r"^[6-9]{1}[0-9]{8}$"
    patron_mail = r"^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    patron_password = r"[a-zñÑ0-9_-]{4,8}$"
    
    validador_texto = re.compile(patron_texto)
    validador_telefono = re.compile(patron_telefono)
    validador_mail = re.compile(patron_mail)
    validador_password = re.compile(patron_password)  
    
    nuevo_nombre = request.POST["nuevo_nombre"]
    nuevo_apellido_1 = request.POST["apellido_1"]
    nuevo_apellido_2 = request. POST["apellido_2"]
    nuevo_telefono = request.POST["telefono"]
    nuevo_email = request.POST["email"]
    password_actual = request.POST["current_password"]
    nueva_password_1 = request.POST["new_password_1"]
    nueva_password_2 = request.POST["new_password_2"]
    
    if "id_usuario" in request.session:
    
        usuario = models.Usuarios.objects.get(pk = id_usuario)
        
        #inicio de la variable validacion_pass_actual
        validacion_pass_actual = True    
        
        if password_actual == usuario.password:
            validacion_pass_actual = True
        else:
            validacion_pass_actual = False
            context = {
                "error_pass_actual" : "La contraseña actual no es correcta"
                }
            return render(request, "modificacion-usuario.html", context)     
        
            
        if nueva_password_1 == nueva_password_2:
            nueva_password = nueva_password_2
            
        else:
            context = {
                "pass_no_match" : "Las campos de contraseña no son iguales"
                }
            return render(request, "modificacion-usuario.html", context)
        
        validacion_nuevo_nombre = validador_texto.match(nuevo_nombre)
        validacion_nuevo_apellido_1 = validador_texto.match(nuevo_apellido_1)
        validacion_nuevo_apellido_2 = validador_texto.match(nuevo_apellido_2)
        validacion_nuevo_telefono = validador_telefono.match(nuevo_telefono)
        validacion_nuevo_email = validador_mail.match(nuevo_email)
        validacion_nueva_password = validador_password.match(nueva_password)
        
        validacion = True
        
        if validacion_nuevo_nombre and validacion_nuevo_apellido_1 and validacion_nuevo_apellido_2 and validacion_nuevo_telefono and validacion_nuevo_email and validacion_nueva_password:
            validacion = True
        else:
            validacion = False
        
        if validacion == True:
        
            usuario.nombre = nuevo_nombre
            usuario.apellido_1 = nuevo_apellido_1
            usuario.apellido_2 = nuevo_apellido_2
            usuario.telefono = nuevo_telefono
            usuario.email = nuevo_email
            usuario.password = nueva_password
            usuario.save()
            return redirect("/anuncios/home-usuario")
        
        else:
            context = {
                "error_campo" : "Algún campo no es correcto",
                "nombre": usuario.nombre,
                "apellido_1" : usuario.apellido_1,
                "apellido_2" : usuario.apellido_2,
                "telefono" : usuario.telefono,
                "email" : usuario.email
                }
            return render(request, "modificacion-usuario.html", context)
     
    else:
        return redirect("/anuncios/inicio-sesion-usuario")
        
def volver_a_home(request):
    return redirect("/anuncios/home-usuario")

def cerrar_sesion_usuario(request):
    request.session.clear()
    return redirect("/anuncios")

def panel_administracion(request):
    return redirect("/admin")

