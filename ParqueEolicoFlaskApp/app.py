from flask import Flask
from flask import Flask, render_template,request

import parque_eolico_AG

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/resultados",methods=['POST'])
def resultados():
    if request.method == 'POST':
        aerogenerador = request.form['groupAerogeneradores']
        velocidad_viento = float(request.form['groupZona'])
        cantidad_aerogeneradores = int(request.form['cantidad_aerogeneradores'])
        #tamano_terreno = int(request.form['tamano_terreno'])
        parque_optimo, potencia_generada, tabla_resultados = parque_eolico_AG.programa_principal(velocidad_viento,aerogenerador,cantidad_aerogeneradores)
        tabla_minimos = []
        tabla_maximos = []
        tabla_promedios = []
        for i in range(len(tabla_resultados)):
            tabla_minimos.append({ "label": i+1, "y": tabla_resultados[i][0]})
            tabla_maximos.append({ "label": i+1, "y":  tabla_resultados[i][1]})
            tabla_promedios.append({ "label": i+1, "y": tabla_resultados[i][2]})
         
    return render_template('resultados.html',
                            parque_optimo=parque_optimo, 
                            potencia_generada=potencia_generada, 
                            tabla_maximos=tabla_maximos,
                            tabla_minimos=tabla_minimos,
                            tabla_promedios=tabla_promedios)

if __name__ == "__main__":
    app.run()    