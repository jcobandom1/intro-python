from flask import Flask

app = Flask(__name__)

mi_pagina = '''
<html>
<body>
<h1>Hola Mundo!</h1>
<h2>Soy Bluky</h2>
<img src='imagenes/Bluky.jpg'>
</body>
</html>
'''

@app.route('/')
def hola_mundo():
    return mi_pagina

@app.route('/<name>')
def hola_nombre(name):
    return 'Hola Mundo es un gusto saludarte %s!' % name

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8085)