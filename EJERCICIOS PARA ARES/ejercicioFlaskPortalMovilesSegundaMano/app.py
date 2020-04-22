from flask import Flask
from flask.globals import request
from flask.templating import render_template
from operaciones_bd import operaciones
from clases.modelo import Anuncio

if __name__ == "__main__":
    
    app = Flask(__name__)
    
    @app.route("/")
    def inicio_listado():
        anuncios = operaciones.listar()
        return render_template("index.html", var_anuncios = anuncios)
    
    @app.route("/registrar-anuncio")
    def nuevo_registro():    
        return render_template("registrar-anuncio.html")
    
    @app.route("/guardar-anuncio")
    def guardar_anuncio():
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
    
        anuncio = Anuncio(marca, modelo, color, pantalla, memoria, anyo, precio, nombre, telefono, email)
        
        operaciones.registrar(anuncio)
    
        return render_template("anuncio-guardado.html")
    
    Flask.debug = 1
    app.run()