'''
Programa que Contiene funciones 
utilizadas en el Proyecto de
Programador Python.
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Programa que se encarga principalmente
de la parte analítica como así también
la parte gráfica de los datos.
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import numpy as np
import io
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')   # For multi thread, non-interactive backend (avoid run in main loop
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import diabetes


def chart(values):
    """
    Función que toma los valores
    Ingresados por Parámetro y 
    los devuelve dejándolos listo
    para realizar un gráfico con
    ellos.
    """

    # Obtengo una lista de numeros dependiendo del tamaño de values
    x = [[num] for num in range(len(values))]

     # Hago esto para convertirlo en un array de 2 dimensiones
    x = np.asanyarray(x)

    # Convierto la tupla en un array de 2 dimensiones.
    y = np.asanyarray(values)

    return x, y


def plot_xy (x, y, color, title, ylabel):
    '''
    Función que Realiza un gráfico plot
    y retorna la figura.
    '''
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_title(title, fontsize=19)
    ax.plot(x, y, color=color)
    ax.set_facecolor('lightcyan')
    ax.set_ylabel(ylabel, fontsize=20)

    # Oculto el Eje x
    ax.get_xaxis().set_visible(False)

    plt.grid('True')

    return fig


def plot_to_canvas(fig):
    """
    Convierte un gráfico en una imagen 
    para enviar por HTTPy mostrar 
    en el HTML.
    Recibe como parámetro la figura que 
    contiene el gráfico.
    """
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output


def filter_age(personas):
    """
    Función encargada de obtener los
    id junto con las edades y filtrar
    aquellos id repetidos.
    Retorna una nueva lista con las
    edades filtradas.
    """

    # Creo una Lista Vacía donde se van a almacenar las edades.
    ages =[]
    
    d = {}

    # Recorro la lista e inserto en una nueva lista
    # aquellas edades cuyos ids no estén repetidos.
    for persona in personas:
        id = persona[0]
        if d.get(str(id)) is None:
            d[str(id)] = persona[1]
            ages.append(d[str(id)])

    return ages
        
    
def create_age_group(ages):
    """
    Función encargada de separar
    las edades en distintos grupos
    etarios y calcular la cantidad
    de personas en cada grupo.
    Retorna un diccionario con los
    grupos etarios.
    """
    
    # Inicializo el diccionario
    age_group={'bebes': 0, 'infantes': 0, 'adolescentes': 0,
                'adultos_jovenes': 0, 'adultos': 0,
                'adultos_mayores': 0}

    for age in ages:
        if 0<=age<=5:   # [0: 5]
            age_group['bebes'] += 1 
        elif 6<=age<=12:    # [6: 12]
            age_group['infantes'] += 1
        elif 13<=age<=19:   # [13: 19]
            age_group['adolescentes'] += 1
        elif 20<=age<=35:   # [20: 35]
            age_group['adultos_jovenes'] += 1
        elif 36<=age<=60:   # [36: 60]
            age_group['adultos'] += 1
        else:   # [60: inf)
            age_group['adultos_mayores'] += 1
    
    return age_group


def bar_plot(x, y, title, color, ylabel):
    '''
    Función que realiza un gráfico de barras.
    '''
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_title(title, fontsize=19)
    ax.bar(x, y, color=color)
    ax.set_facecolor('lightyellow')
    ax.set_ylabel(ylabel, fontsize=19)

    plt.grid('True')

    return fig