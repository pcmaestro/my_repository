from flask import Flask, request
from flask.templating import render_template


#como la linea que poniamos en pyqt5 esta es una linea obligatoria 
#para usar flask 
app = Flask(__name__)

#decorador route
@app.route("/")
def raiz():
    return render_template("/index.html")

@app.route("/registro-anuncio")
def registro_anuncio():
    return render_template("/registro-anuncio.html")

@app.route("/guardar-anuncio")
def guardar_anuncio():
    email = request.args.get("email")
    telefono = request.args.get("telefono")
    texto = request.args.get("texto")
    mensaje = "voy a guardar en base de datos (por hacer): " + email + " "\
        + telefono + " " + texto
    return mensaje

Flask.debug = 1 #esto es para que cuango guarde desde eclipse no tenga
#que parar y arrancar la aplicacion, solo tendre que refrescar desde el 
#navegador web para ver los cambios
app.run()