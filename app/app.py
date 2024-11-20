from flask import Flask, render_template
import os


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
@app.route('/participar')
def participar():
    return render_template('participar.html')

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
    with app.test_request_context():
        
        os.makedirs("docs", exist_ok=True)  # Crear el directorio 'docs' si no existe
        routes = {
        "index": "/",  # Ruta para 'index.html'
        "ciencia-y-sociedad": "/ciencia-y-sociedad",  # Ruta para 'sociedad.html'
        "participar": "/participar",  # Ruta para 'participar.html'
        "recursos": "/recursos",  # Ruta para 'recursos.html'
        "sobre": "/sobre"  # Ruta para 'sobre.html'
    }
        

    for route, endpoint in routes.items():
        # Renderiza la página de la ruta especificada
        rendered = app.test_client().get(endpoint).data.decode("utf-8")
        
        # Guarda el contenido renderizado como un archivo HTML
        with open(f"docs/{route}.html", "w", encoding="utf-8") as f:
            f.write(rendered)

