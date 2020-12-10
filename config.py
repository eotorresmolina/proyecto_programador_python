'''
Archivo de Configuración
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Programa creado para modificar y/o editar archivos de
configuración utilizados en este proyecto.
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


from configparser import ConfigParser


def config(section, filename='config.ini'):
    # Obtengo el analizador y leo el archivo de configuración
    # como si fuera un diccionario.
    parser = ConfigParser()
    parser.read(filename)

    config_param = {}

    # Si existe la sección creo una lista de tuplas con 
    # usando como keys y values, las opciones de esa
    # sección.
    # Luego lo guardo en un diccionario.
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_param[param[0]] = param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config_param