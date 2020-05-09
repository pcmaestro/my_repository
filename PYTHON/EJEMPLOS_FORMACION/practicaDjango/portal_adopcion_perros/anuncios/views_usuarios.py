from django.shortcuts import render, redirect
from . import models
import email

def registro_usuario(request):    
    return render(request, "registro-usuario.html")

def guardar_usuario(request):
    nombre = request.POST["nombre"]
    apellido_1 = request.POST["apellido1"]
    apellido_2 = request.POST["apellido2"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]  
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    if password1 == password2:
        password = password2
    comprobacion_mail = email    
    context = {}
    if len(models.Usuarios.objects.filter(email = comprobacion_mail)) == 1:        
        context = {"error_mail" : "El correo ya está registrado, debe indicar uno distinto"}
        return render(request,"registro-usuario.html", context)
    else:   
        nuevo_usuario = models.Usuarios(nombre = nombre, apellido_1 = apellido_1, apellido_2 = apellido_2, telefono = telefono, email = email, password = password)
        nuevo_usuario.save()
        context = {
            "nombre" : nombre + " " + apellido_1 + " " + apellido_2,
            }
    return render(request,"home.html", context)

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
    id_usuario = request.session["id_usuario"]
    usuario = models.Usuarios.objects.get(pk = id_usuario)    
    anuncios_usuario = models.Perros.objects.filter(usuario_id = usuario.id)
    context = {
        "nombre" : usuario.nombre + " " + usuario.apellido_1 +
         " " + usuario.apellido_2, "mis_anuncios" : anuncios_usuario
    }
    return render(request, "home.html", context)

def modificacion_usuario(request):
    id_usuario = request.session["id_usuario"]
    usuario = models.Usuarios.objects.get(pk = id_usuario)
    context = {
        "nombre":usuario.nombre, "apellido_1":usuario.apellido_1, "apellido_2":usuario.apellido_2,\
        "telefono":usuario.telefono, "email":usuario.email, "id_usuario":id_usuario
        }
    return render(request, "modificacion-usuario.html", context)

def guardar_usuario_modificado(request,id_usuario):
    nombre = request.POST["nombre"]
    apellido_1 = request.POST["apellido_1"]
    apellido_2 = request. POST["apellido_2"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    usuario = models.Usuarios.objects.get(pk = id_usuario)
    usuario.nombre = nombre
    usuario.apellido_1 = apellido_1
    usuario.apellido_2 = apellido_2
    usuario.telefono = telefono
    usuario.email = email
    usuario.save()
    return redirect("/anuncios/home-usuario")

def cerrar_sesion_usuario(request):
    request.session.clear()
    return render(request, "index.html")