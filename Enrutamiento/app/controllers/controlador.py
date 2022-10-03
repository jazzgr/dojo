from app import app
from flask import render_template

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente 
def hola_mundo():                   # y a menos que no indiquemos otro metodo de consulta, es por default GET
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta


@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<nombre>')
def hola_nombre(nombre):
    return render_template("index.html", nombre=nombre)

@app.route('/repeat/<int:numero>/<palabra>')
def repeat_words(numero, palabra):
    return (palabra + "\n") * numero
#No logre que se tiarara la palabra hacia abajo:(

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404
    #return render_template('404.html'), 404

