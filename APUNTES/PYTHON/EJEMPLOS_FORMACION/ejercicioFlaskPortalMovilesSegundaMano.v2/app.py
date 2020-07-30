from flask import Flask
from flask.globals import request
from flask.templating import render_template
from operaciones_bd import operaciones
from clases.modelo import Anuncio
from flask_mail import Mail, Message
import string
import random
import re

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pedro.cast.curso.python@gmail.com'
app.config['MAIL_PASSWORD'] = 'xkavemhchrofovlr'
mail = Mail(app)

@app.route("/validar-anuncio")
def validar_anuncio():
    id = request.args.get("id")
    codigo = request.args.get("c")

    resultado = operaciones.comprobar_codigo_anuncio(id, codigo)

    if resultado == 0:
        return "Código o id no válidos, id = {} , código = {}".format(str(id), str(codigo))
    if resultado == 1:
        return "Anuncio validado , <a href = '/' > voler al listado de anuncios </a>"

@app.route("/")
def inicio_listado():
    anuncios = operaciones.listar()
    return render_template("index.html", var_anuncios = anuncios)

@app.route("/registrar-anuncio")
def nuevo_registro():
    return render_template("registrar-anuncio.html")

@app.route("/guardar-anuncio")
def guardar_anuncio():
    #Recogemos los datos de los formularios
    marca = request.args.get("marca")
    modelo = request.args.get("modelo")
    color = request.args.get("color")
    pantalla = request.args.get("pantalla")
    memoria = request.args.get("memoria")
    anyo = request.args.get("anyo")
    precio = request.args.get("precio")
    nombre = request.args.get("nombre")
    telefono = request.args.get("telefono")
    email = request.args.get("email")

    #Valicadiones
    regex_text = r"^[a-zA-Z0-9.]{2,10}$"
    regex_tf = r"^[6-9]{1}[0-9]{8}$"
    regex_mail = r"^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

    validador_marca = (re.compile(regex_text)).match(marca)
    validador_modelo = (re.compile(regex_text)).match(modelo)
    validador_color = (re.compile(regex_text)).match(color)
    validador_pantalla = pantalla.isdigit()
    validador_memoria = memoria.isdigit()
    validador_anyo = anyo.isdigit()
    validador_precio = precio.isdigit()
    validador_nombre = (re.compile(regex_text)).match(nombre)
    validador_telefono = (re.compile(regex_tf)).match(telefono)
    validador_email = (re.compile(regex_mail)).match(email)

    if validador_marca and validador_modelo and validador_color and validador_pantalla and validador_memoria and validador_anyo and validador_precio and validador_nombre and validador_telefono and validador_email:
        #Creamos el objeto anuncio
        anuncio = Anuncio(marca, modelo, color, pantalla, memoria, anyo, precio, nombre, telefono, email)
    else:
        return("Revisa que todos los datos sean correctos")

    #Creamos el código de validación
    letras = string.ascii_letters + string.digits
    codigo = ''.join(random.choices(letras, k = 100 ))

    #Registramos en la BD el anuncio y el código y guardamos el id generado
    id_generado = operaciones.registrar(anuncio, codigo)

    #Enviamos el email para la confirmación

    msg = Message("Confirmación de registro de anuncio", sender = "pedro.cast.curso.python@gmail.com", recipients = [email] )
    msg.html = "Para continuar con el proceso de registro es necesario pular en el siguiente enlace. <a href = 'http://pedrocastcursopython.pythonanywhere.com/validar-anuncio?id={}&c={}'> Por favor, pulse aqui </a>".format(str(id_generado), str(codigo))
    mail.send(msg)


    return render_template("anuncio-guardado.html")

Flask.debug = 1
app.run()