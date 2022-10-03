from primer_app import app

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'