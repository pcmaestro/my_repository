from flask import Flask
from flask.templating import render_template
from flask.globals import request
from operaciones_bd import operaciones_bd_mensajes
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


#comienzo del servicio rest
@app.route("/registrar-mensaje",methods=["GET","POST"])
def registrar_mensaje():
    nombre = request.args["n"]
    mensaje = request.args["m"]
    operaciones_bd_mensajes.registrar_mensaje(nombre, mensaje)
    return "ok"

@app.route("/obtener-mensajes")
def obtener_mensajes():
    mensajes = operaciones_bd_mensajes.obtener_mensajes()
    return jsonify(mensajes)


Flask.debug = 1
app.run()
