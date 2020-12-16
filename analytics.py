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
import seaborn as sns
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


def filtered_atrr(personas):
    """
    Función encargada de obtener los
    id junto con el atributo filtrando
    aquellos id repetidos.
    Retorna una nueva lista con los
    atributos filtrados.
    """

    # Creo una Lista Vacía donde se van a almacenar los atributos.
    attrs =[]
    
    d = {}

    # Recorro la lista personas e inserto en una nueva lista
    # aquellos atributos cuyos ids no estén repetidos.
    for persona in personas:
        id = persona[0]
        if d.get(str(id)) is None:
            d[str(id)] = persona[1]
            attrs.append(d[str(id)])

    return attrs
        
    
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


def create_gender_group(gender):
    """
    Función encargada de separar
    el sexo biológico en 2 grupos: femenino
    y masculino y calcular la cantidad
    de personas que pertenecen a cada grupo.
    Retorna un diccionario con los
    grupos.
    """
    gender_group = {'masculino': 0, 'femenino': 0}

    for gen in gender:
        if gen == 'm':
            gender_group['masculino'] += 1

        elif gen == 'f':
            gender_group['femenino'] += 1
 
    return gender_group


def bar_plot(x, y, titles, ylabel):
    '''
    Función que realiza un gráfico de barras,
    esta vez utilizando la biblioteca seaborn.
    '''
    fig, axs = plt.subplots(2,1, figsize=(16, 9))

    
    axs[0].set_title(titles[0], fontsize=16)
    sns.barplot(x=x[0], y=y[0], palette='muted', ax=axs[0])
    axs[0].set_facecolor('lightyellow')
    axs[0].set_ylabel(ylabel, fontsize=19)
    axs[0].grid('True')

    axs[1].set_title(titles[1], fontsize=16)
    sns.barplot(x=x[1], y=y[1], palette='dark', ax=axs[1])
    axs[1].set_facecolor('lightyellow')
    axs[1].set_ylabel(ylabel, fontsize=19)
    axs[1].grid('True')

    return fig