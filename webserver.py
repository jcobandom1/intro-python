from flask import Flask

app = Flask(__name__)

mi_pagina =''''''

@app.route('/')
def hola_mundo():
    return 'Hola Mundo soy Juan Carlos gusto saludarlo, gracias por su visita!'

@app.route('/<name>')
def hola_nombre(name):
    return 'Hola Mundo es un gusto saludarte %s!' % name

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8085)