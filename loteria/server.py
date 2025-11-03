from flask import Flask, render_template, request
import random

app = Flask(__name__)

cartas = ["1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas","6  La sirena", "7  La escalera","8  La botella",
              "9  El barril", "10 El árbol", "11 El melón", "12 El valiente","13 El gorrito","14 La muerte", "15 La pera", "16 La bandera",
              "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro", "21 La mano", "22 La bota", "23 La luna", "24 El cotorro",
              "25 El borracho", "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón", "31 Las jaras","32 El músico",
              "33 La araña", "34 El soldado", "35 La estrella", "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal","40 El alacrán",
              "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito","45 El venado", "46 El sol", "47 La corona","48 La chalupa",
              "49 El pino", "50 El pescado", "51 La palma","52 La maceta", "53 El arpa","54 La rana"]
    
colors = ['rosa', 'amarillo', 'azul']
patron = [0, 1, 2, 0] 

@app.route('/')
def index():    
    
    filas = 4
    columnas = 4
    grid = []
    index = 0

    cartas_seleccionadas = random.sample(cartas, filas * columnas)
    
    for i in range(filas):
        caja = []
        for j in range(columnas):
            color_index = (patron[j % len(patron)] + i) % 3
            carta = cartas_seleccionadas[index]
            caja.append({'color': colors[color_index], 'texto': carta})
            index += 1
        grid.append(caja)
    
    return render_template('index.html', grid=grid)

@app.route('/nivel2', methods=['GET','POST'])
def nivel2():
    filas =  4
    columnas = 4
    total_cartas = filas * columnas
    grid = []
    index = 0

    if request.method == 'GET':
        filas_patron = request.args.get('filas')
        if filas_patron:
            try:
                filas = int(filas_patron)
            except (ValueError, TypeError):
                filas = 4
                
    total_cartas_necesarias = filas * columnas
    
    cartas_seleccionadas = random.choices(cartas, k=total_cartas_necesarias)

    for i in range(filas):
        caja = []
    
        for j in range(columnas):
            color_index = (patron[j % len(patron)] + i) % 3
            carta = cartas_seleccionadas[index]
            caja.append({'color': colors[color_index], 'texto': carta})
            index += 1
        grid.append(caja)

    return render_template('nivel2.html', grid=grid, filas=filas)

@app.route('/nivel3', methods=['GET','POST'])
def nivel3():
    filas = 4
    columnas = 4
    total_cartas = filas*columnas
    grid = []
    index = 0
    patron = [0, 1, 2, 0, 1, 2] 

    if request.method == 'GET':
        filas_patron = request.args.get('filas')
        if filas_patron:
            try:
                filas = int(filas_patron)
            except (ValueError, TypeError):
                filas = 4
    
        columnas_patron = request.args.get('columnas')
        if columnas_patron:
            try:
                columnas = int(columnas_patron)
            except (ValueError, TypeError):
                columnas = 4

    #cartas_seleccionadas = random.sample(cartas, filas * columnas)
    total_cartas_necesarias = filas * columnas
    
    cartas_seleccionadas = random.choices(cartas, k=total_cartas_necesarias)
    for i in range(filas):
        caja = []
        for j in range(columnas):
            color_index = (patron[j % len(patron)] + i) % 3
            carta = cartas_seleccionadas[index]
            caja.append({'color': colors[color_index], 'texto': carta})
            index += 1
        grid.append(caja)
    
    return render_template('nivel3.html', grid=grid, filas=filas, columnas=columnas)

if __name__ == '__main__':
    app.run(debug=True)

