from flask import Flask, redirect, render_template, request, session, url_for
import random

app = Flask(__name__)

app.secret_key ='codigosecreto'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar_data():
    nombre = request.form['nombre']
    lugar = request.form['lugar']
    numero = int(request.form['numero'])
    comida = request.form['comida']
    profesion = request.form['profesion']

    #sesiones
    session['nombre'] = nombre
    session['lugar'] = lugar
    session['numero'] = numero
    session['comida'] = comida
    session['profesion'] = profesion
    return redirect(url_for('futuro'))

@app.route('/futuro', methods=['GET'])
def futuro():
    if'nombre' not in session:
        return redirect(url_for('index'))
    nombre = session['nombre']
    lugar = session['lugar'] 
    numero = session['numero'] 
    comida = session['comida'] 
    profesion = session['profesion'] 

    if random.choice([True, False]):
        mensaje = (f" soy el adivino del Dojo, {nombre} tendrá un viaje muy largo "
                   f" dentro de {numero} años a {lugar} y estará el resto de sus días "
                   f" preparando {comida} para todas las personas que quiere. " 
                   f" Además, cambió de profesión y ahora es {profesion}.")
    else:
        mensaje = (f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, "
                   f"nunca conocerá {lugar} y jamas volvió a comer {comida}.")
    
    return render_template('futuro.html', mensaje = mensaje)

if __name__ =='__main__':
    app.run(debug=True)

