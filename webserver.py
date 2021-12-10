from flask import Flask
app = Flask(__name__)

mi_pagina = ''' <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tutorial Flask: Miniblog</title>
</head>
<body>
    <form>  
        <label>Enter first name</label><br>  
        <input type="text" name="firstname"><br>  
        <label>Enter last name</label><br>  
        <input type="text" name="lastname"><br>  
        <p><strong>Note:</strong>The default maximum cahracter lenght is 20.</p>  
    </form>  
</body>
</html> '''

@app.route('/')
def hola_mundo():
    return mi_pagina

@app.route('/<name>')
def hola_nombre(name):
    return 'Hola %s!' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086)