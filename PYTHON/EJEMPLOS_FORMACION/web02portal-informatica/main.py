from flask import Flask
from flask.templating import render_template
from flask.globals import request


from clases import modelo

from operaciones_bd import operaciones_bd_anuncios

app = Flask(__name__)

@app.route("/")
def inicio():
    anuncios = operaciones_bd_anuncios.obtener_anuncios()
    return render_template("index.html", var_anuncios = anuncios)

@app.route("/registrar-anuncio")
def registrar_anuncio():
    return render_template("formulario-registro-anuncio.html")

@app.route("/guardar-nuevo-anuncio") #Esta ruta es el action del form
def guardar_anuncio():
    nombre = request.args.get("nombre") #Este parametro es el name de los input type
    precio = request.args.get("precio")
    email = request.args.get("email")
    
    anuncio = modelo.Anuncio(nombre, precio, email)
    
    operaciones_bd_anuncios.registrar_anuncio(anuncio)
    
    return render_template("/registro-anuncion-ok.html")

Flask.debug = 1
app.run()