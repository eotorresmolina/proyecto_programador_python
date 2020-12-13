'''
Programa Principal del Proyecto
Programador Python.
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Programa principal que crea un servidor
y levanta todas las funciones necesarias
para aplicar en una API y/o WebApp.
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


# Importo librerías nativas, propias y de 3ros.
import os
import traceback
from flask import Flask, Response, render_template, request, jsonify, session, url_for, redirect
from datetime import datetime
from matplotlib import pyplot as plt

from config import config
import diabetes
import analytics
import logging


# Creo los path de los archivos para utilizar en este programa:
script_path = os.path.dirname(os.path.realpath(__file__))
config_path_name = os.path.join(script_path, 'config.ini')

endpoint = config('endpoints', filename=config_path_name)
templates = config('templates', filename=config_path_name)
server = config('server', filename=config_path_name)


# Desarrollo de la API - WebApp:

# logging.basicConfig(filename='myapp.log', 
#                     format='%(asctime)s - %(levelname)s - %(message)s', 
#                     level=logging.INFO)

# logger = logging.getLogger('app')

# Creo el Server:
app = Flask(__name__)


# Creo una clave secreta para encriptar los datos:
app.secret_key = 'flask_session_key_secret'


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000
@app.route(endpoint['index'])
def index():
    try:
        return render_template(templates['index'])

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/reset
@app.route(endpoint['reset'])
def reset():
    try:

        # Pregunto si el usuario todavía no está logueado.
        if (session.get('username') is None or session.get('pswrd') is None):
            return redirect(url_for('login'))

        # Entra únicamente si el usuario se logueó como administrador
        if ((session.get('username') == 'user123456') and (session.get('pswrd') == 'jilguero123')):
            
            # Borro y/o Re-genero la DB
            diabetes.create_schema()
            
            result = '<h1> Bienvenido/a: Usted está Logueado como Administrador!</h1>'
            result += '<h1>Usted está Logueado como Administrador!</h1>'
            result += '<h1><b>ATENCIÓN:</b> Base de Datos (DB) Borrada y/o Regenerada Correctamente.!</h1>'
            result += '<h3>No se olvide de Desloguearse accediendo al endpoint: "/logout"'
            
            return result

        else:
            
            # Elimino la sesión ya que el usuario no es el administrador.
            session.clear()

            return Response("<h1>Error al Intentar Loguearse</h1>", status=401, mimetype='text') 

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/login
@app.route(endpoint['login'], methods=['GET', 'POST'])
def login():
    try:
        # Entro, en este caso, cuando soy redirigido por '/reset'
        if request.method == 'GET':
            return render_template(templates['login'])

        elif request.method == 'POST':
            username = str(request.form.get('username'))
            pswrd = str(request.form.get('password'))

            # Si no se ingresaron datos
            if (username is None or pswrd is None):
                return Response('Usted no se ha Logueado', status=400, mimetype='text')

            session['username'] = username
            session['pswrd'] = pswrd

            return redirect(url_for('reset'))

    except:
            return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/logout           
@app.route(endpoint['logout'])
def logout():
    try:
        # Cierro la Sesión Iniciada.
        # Sucede únicamente si el administrador fue logueado.
        session.clear()
        
        return redirect(url_for('.index'))

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/formulario
@app.route(endpoint['formulario'], methods=['GET', 'POST'])
def registro():

    # Entra únicamente cuando es cargada la página.
    if request.method == 'GET':
        try:
            return render_template(templates['formulario'])
    
        except:
            return jsonify({'trace': traceback.format_exc()})
        
    # Entra cuando es Enviado el Formulario con los Datos.
    if request.method == 'POST':
        try:
            # Obtengo los datos del HTTP POST
            name = str(request.form.get('name'))
            dni = str(request.form.get('dni'))
            age = str(request.form.get('age'))
            sugarlevel = str(request.form.get('sugarlevel'))

            if (name is None or dni is None or dni.isdigit() is False
                or age.isdigit() is False or sugarlevel is None
                or sugarlevel.isdigit() is False):

                # Retorno un Código de Estado 400
                return Response(status=400)
                
            # Inserto los valores a la DB dentro de la tabla "registro"
            diabetes.insert_registro(int(dni))

            # Obtengo la fecha y hora del registro.
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Inserto los valores a la DB dentro de la tabla "persona"
            item = (name, int(age), int(sugarlevel), date, int(dni))
            diabetes.insert_persona(item)

            # Retorno una página HTML
            return render_template(templates['registro'])

        except:
            return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/niveles/api
@app.route(endpoint['niveles_api'])
def niveles_api():
    try:
        data_json = diabetes.report(dict_format=True)
        return jsonify(data_json)

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/niveles/tabla
@app.route(endpoint['niveles_tabla'])
def niveles_tabla():
    try:
        # Obtengo los Datos en formato tupla
        rows = diabetes.report(dict_format=False)

        c1 = [value[0] for value in rows]   # Obtengo el id
        c2 = [value[1] for value in rows]   # Obtengo la edad
        c3 = [value[2] for value in rows]   # Obtengo el Valor de Azúcar
        c4 = [value[3] for value in rows]   # Obtengo le fecha y hora del Registro

        return render_template(templates['tabla_niveles'], row=zip(c1, c2, c3, c4))

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/niveles/{dni}/chart
# En este caso usamos una query string con "paramétros estáticos"
@app.route(endpoint['niveles_dni_chart'])
def niveles_dni_chart(dni):
    try:
        # Obtengo los valores de azúcar de una determinada persona
        values = diabetes.extractfdb_person(int(dni))

        # Separo los valores para luego poder graficarlos.
        x, y = analytics.chart(values)

        title = 'Histórico del Nivel de Glucosa en Sangre Medido en Ayuna.'

        # Realizo un gráfico tipo "plot" de los valores de azúcar
        fig = analytics.plot_xy(x, y, color='darkblue', title=title, ylabel='$[mg/dl]$')

        # Convierto el gráfico en una imagen para enviarla por HTTP
        output = analytics.plot_to_canvas(fig)

        # Cierro la imagen así no hay consumo de memoria del sistema.
        plt.close(fig)  
        
        # Retorno la imagen con el gráfico
        return Response(output.getvalue(), mimetype='image/png')

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/niveles/{dni}/tabla
# En este caso usamos una query string con "paramétros estáticos"
@app.route(endpoint['niveles_dni_tabla'])
def niveles_dni_tabla(dni):
    try:
        values = diabetes.fill_name(dni)
        if values == []:
            result = '<h1><b>El DNI Ingresado no ha sido Registrado.</b></h1>'
            result += '<h2>Compruebe que lo Haya Escrito Correctamente.</h2>'
            
            return result

        val = diabetes.fill_avg_count_value(dni)
        avg = val[0]
        count = val[1]

        name = values[0][0]     # Obtengo el Nombre de la Persona
        c1 = [value[1] for value in values]     # Obtengo el nivel de azúcar
        c2 = [value[2] for value in values]     # Obtengo la fecha y hora del registro.

        return render_template(templates['tabla_persona'], name=name, 
                                row=zip(c1, c2), avg=avg, count=count)

    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la Siguiente ULR: 127.0.0.1:5000/comparativa
@app.route(endpoint['comparativa'])
def comparativa():
    try:
        # Extraigo todas las edades junto con los ids
        ids_ages = diabetes.extract_ages()

        # Filtro los ids repetidos y me quedo sólo con las edades
        ages = analytics.filter_age(ids_ages)

        # Obtengo la cantidad de personas con diabetes por grupo etario
        # en formato diccionario
        age_group = analytics.create_age_group(ages)

        # Obtengo la cantidad de los grupos utilizando compresión de listas
        values = age_group.values()
        y = [value for value in values]

        x = ['Bebés: [0:5]', 'Infantes: [6:12]', 'Adolescentes: [13:19]',
                'Jóvenes Adultos: [20:35]', 'Adultos: [36:60]', 
                'Adultos Mayores: +60']

        title = 'Comparativa de la Cantidad de Personas con Diabetes Registradas por Grupo Etario'
        ylabel = 'Cant. de Personas'

        # Realizo el gráfico de barras
        fig = analytics.bar_plot(x, y, title, color='darkblue', ylabel=ylabel)
        
        # Convierto el gráfico de Barras en una imagen para enviar por HTTP
        output = analytics.plot_to_canvas(fig)

        # Cierro la imagen así no hay consumo de memoria del sistema.
        plt.close(fig)  
        
        # Retorno la imagen con el gráfico
        return Response(output.getvalue(), mimetype='image/png')
    
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route(endpoint['info'])
def info():
    try:
        pass

    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == "__main__":
    
    # Lanzo el Server:
    app.run(
            host=server['host'],
            port=server['port'],
            debug=True
    )