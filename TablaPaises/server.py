from flask import Flask, render_template, request
app = Flask(__name__)

paises = [
   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},
   {'pais': 'Brasil' , 'capital': 'Brasilia'},
   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},
   {'pais': 'Colombia' , 'capital': 'Bogotá'},
   {'pais': 'Costa Rica' , 'capital': 'San José'},
   {'pais': 'Paraguay' , 'capital': 'Asunción'},
   {'pais': 'Perú' , 'capital': 'Lima'}
]

@app.route('/', methods=['GET','POST'])

def index():

    return render_template('index.html', paises = paises)

if __name__ == '__main__':
    app.run(debug=True)
