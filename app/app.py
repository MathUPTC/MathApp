from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la sección "Sobre el Proyecto"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Ruta para la sección "Código de Conducta"
@app.route('/codigo-de-conducta')
def codigo_de_conducta():
    return render_template('codigo_de_conducta.html')

# Ruta para la sección "Recursos"
@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

#Ruta para ciencia y sociedad
@app.route('/ciencia_y_sociedad')
def sociedad():
    return render_template('sociedad.html')


# Ruta para la sección "Contacto"
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)
