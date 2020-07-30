from flask import Flask
from flask.templating import render_template
from flask.globals import request, session
from clases import modelo
from operaciones_bd import operaciones_bd_anuncios
from flask_mail import Mail, Message
import string
import random
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aresdesancho@gmail.com'
app.config['MAIL_PASSWORD'] = 'xzlqnofmpjnauohn'
mail = Mail(app)


#lo siguiente es obligatorio para poder usar la sesion
app.secret_key = "ejemplo_clave_secreta"

@app.route("/admin/")
def inicio_administracion():
    return render_template("admin/login.html", error_login = "")

@app.route("/admin/<string:ruta>",methods=["POST","GET"])
def administracion(ruta):
    if ruta == "login-admin":
        pass_introducido = request.form.get("clave")
        if pass_introducido == "1234" :
             session["identificado"] = "ok"
             listado_anuncios = operaciones_bd_anuncios.obtener_anuncios()
             return render_template("admin/listado-anuncios-admin.html", anuncios = listado_anuncios)
        else:
             return render_template("admin/login.html", error_login = "pass incorrecto")

    if not "identificado" in session :
        return "te has colado, indentificate de nuevo"

    if ruta == "borrar-anuncio":
        id = request.args.get("id")
        operaciones_bd_anuncios.borrar_anuncio(id)
        try:
            #borramos la foto y si no existe, se ejecuta el except que no hace nada
            os.remove("mysite/static/fotos/" + str(id) + ".jpg")
        except:
            pass
        listado_anuncios = operaciones_bd_anuncios.obtener_anuncios()
        return render_template("admin/listado-anuncios-admin.html", anuncios = listado_anuncios)
    if ruta == "editar-anuncio":
        id = request.args.get("id")
        anuncio_a_editar = operaciones_bd_anuncios.obtener_anuncio_por_id(id)
        return render_template("admin/editar-anuncio.html",anuncio = anuncio_a_editar)
    if ruta == "guardar-cambios-anuncio":
        #asi obtengo los datos del formulario, incluido el hidden
        id = request.form.get("id")
        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        email = request.form.get("email")
        email_valido = request.form.get("email-valido")

        #asi preparo el objeto a mandar a guardar_cambios_anuncio para guardar cambios en la bd
        anuncio_guardar_cambios =  modelo.Anuncio()#forma mas directa: modelo.Anuncio(id=id, nombre = nombre, precio = precio, email = email, email_valido = email_valido)
        anuncio_guardar_cambios.id = id
        anuncio_guardar_cambios.nombre = nombre
        anuncio_guardar_cambios.precio = precio
        anuncio_guardar_cambios.email = email
        anuncio_guardar_cambios.email_valido = email_valido

        #finalmente actualizamos el anuncio en base de datos y volvemos a mostrar listado
        operaciones_bd_anuncios.guardar_cambios_anuncio(anuncio_guardar_cambios)

        #si el usuario subio una nuevo foto, la pisamos con la anterior:
        if "foto" in request.files:
            foto = request.files["foto"]
            foto.save("mysite/static/fotos/" + str(id) + ".jpg")

        listado_anuncios = operaciones_bd_anuncios.obtener_anuncios()
        return render_template("admin/listado-anuncios-admin.html", anuncios = listado_anuncios)

    if ruta == "cerrar-sesion":
        session.clear()
        return render_template("admin/login.html",error_login = "")


##### ruta para validar el anuncio por email
@app.route("/validar-anuncio")
def validar_anuncio():
    id = request.args.get("id")
    codigo = request.args.get("c")

    resultado = operaciones_bd_anuncios.comprobar_codigo_anuncio(id,codigo)
    if resultado == 0:
        return "codigo o id no validos id: " + str(id) + " codigo: " + str(codigo)
    if resultado == 1 :
        operaciones_bd_anuncios.validar_email_anuncio(id)
        return "anuncio validado <a href='/'>volver al listado de anuncios</a>"

@app.route("/")
def inicio():
    anuncios = operaciones_bd_anuncios.obtener_anuncios()
    return render_template("index.html", var_anuncios = anuncios)

@app.route("/registrar-anuncio")
def registrar_anuncio():
    categorias = operaciones_bd_anuncios.obtener_categorias()
    return render_template("formulario-registro-anuncio.html", listado_categorias = categorias)

@app.route("/guardar-nuevo-anuncio",methods=["POST"])#esta ruta es el action del form
def guardar_anuncio():
    nombre = request.form.get("nombre")
    precio = request.form.get("precio").replace("," , ".")
    email = request.form.get("email")

    #para recoger el id de categoria seleccionado
    id_categoria = request.form.get("id_categoria")
    anuncio = modelo.Anuncio(nombre, precio, email)
    anuncio.id_categoria = id_categoria

    #coy a generar un codigo de comprobacion para validar el anuncio
    letras = string.ascii_letters + "0123456789"
    codigo = ''.join(random.choices(letras, k = 60 ))

    id_generado = operaciones_bd_anuncios.registrar_anuncio(anuncio, codigo)

    #guardar el archivo de imagen insertado:
    foto = request.files["foto"]
    foto.save("mysite/static/fotos/" + str(id_generado) + ".jpg")

    #enviar un email
    msg = Message(
        "gracias por registrar tu producto informatico",
        sender = "aresdesancho@gmail.com",
        recipients= [email]
    )

    #asi mandamos texto plano en el email
    #msg.body = "Muchas gracias por registrar tu anuncio \n saludos desde el portal de ARES"
    msg.html = "Muchas gracias por registrar tu anuncio en el portal de ARES <br/> <a href='http://arespython.pythonanywhere.com/validar-anuncio?id=" + str(id_generado) + "&c=" + codigo + "'>pincha en este enlace para validar tu anuncio</a>"

    mail.send(msg)


    return render_template("registro-anuncio-ok.html")




























