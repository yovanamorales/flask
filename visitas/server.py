from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'clavesecreta'

# Página principal
@app.route('/')
def index():
    # Incrementar visitas solo si no viene de un redirect
    session['visitas'] = session.get('visitas', 0) + 1
    session['reinicios'] = session.get('reinicios',0)
    contador_visitas = session['visitas']
    contador_reinicios = session['reinicios']
    return render_template('index.html', 
                         contador_visitas=session['visitas'],
                         contador_reinicios=contador_reinicios)

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['reinicios'] = session.get('reinicios', 0) + 1
    session['visitas'] = 0
    return redirect(url_for('index'))

@app.route('/aumentar_visitas')
def aumentar_visitas():
    session['visitas'] = session.get('visitas', 0) + 1
    return redirect(url_for('index'))

@app.route('/enviar_formulario', methods=['POST'])
def enviar_formulario():
    if request.method == 'POST':
        aumento = int(request.form.get('aumento', 0))
        session['visitas'] = session.get('visitas', 0) + (aumento-1)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)