'''
Programa que Contiene funciones 
utilizadas en el Proyecto de
Programador Python.
---------------------------
Autor: Torres Molina Emmanuel O.
Version: 1.1
Descripción:
Programa que se encarga principalmente
de crear la DB (Base de Datos) y todas
las funciones que permiten la manipulación
y carga de datos en la misma.
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import sqlite3
import os
from config import config


# Obtengo los path
script_path = os.path.dirname(os.path.realpath(__file__))
config_path_name = os.path.join(script_path, 'config.ini')

db = config('db', filename=config_path_name)


def create_schema():
    '''
    Función que genera el schema de mi DB.
    '''

    # Me conecto a la DB.
    conn = sqlite3.connect(db['database'])

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    schema_path_name = os.path.join(script_path, db['schema'])

    # Creo el schema de la DB desde el archivo.
    c.executescript(open(schema_path_name, 'r').read())

    # Realizo el commit para salvar todas las modificaciones realizadas.
    conn.commit()

    # Cierro la DB
    conn.close()


def insert_registro(dni):
    '''
    Función que se conecta a la DB
    para poder insertar una tupla de valores
    que corresponden a la tabla "registro",
    pasados como argumentos a través
    de una query(consulta) a la misma.
    '''
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")
    c = conn.cursor()

    c.execute(
            """ SELECT dni FROM registro
                WHERE dni = ?;""", (dni,))
    
    query_result = c.fetchone()

    if query_result is not None:
        c.execute(
            """ UPDATE registro
                SET dni = (?)
                WHERE dni = ?;""", (dni, query_result[0]))

    else:     
        c.execute(
            """
            INSERT INTO registro (dni)
            VALUES (?);""", (dni,))

    conn.commit()
    conn.close()


def insert_persona(item: tuple):
    '''
    Función que se conecta a la DB
    para poder insertar los valores
    que corresponden a la tabla "persona",
    pasados como argumentos a través
    de una query(consulta) a la misma.
    '''
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")
    c = conn.cursor()

    try:
        c.execute(
            """
            INSERT INTO persona (name, age, gender, value, datetime, fk_registro_id)
            SELECT ?, ?, ?, ?, ?, r.id
            FROM registro AS r
            WHERE r.dni = ?; """, item)

    except sqlite3.Error as err:
        print('\n{}\n'.format(err))

    conn.commit()
    conn.close()


def dict_factory(cursor, row):
    '''
    Función que permite a la DB
    devolver los datos en formato
    diccionario.
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def report(dict_format=False):
    """
    Función que Busca en la DB
    y extrae todos los datos
    en formato JSON si 
    dict_format= True a través de la
    función "dict_factory"
    De lo contrario lo devuelve
    como una lista de tuplas.
    """
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")
    if dict_format is True:
        conn.row_factory = dict_factory

    c = conn.cursor()

    query = """ SELECT fk_registro_id AS id, age, value, datetime
                FROM persona
                ORDER BY fk_registro_id;"""

    c.execute(query)
    query_result = c.fetchall()
    conn.close()

    return query_result


def fill_name(dni):
    '''
    Función que extrae de la DB
    el nombre y los datos de la persona
    cuyo dni sea pasado como
    parámetro.
    '''
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")

    c = conn.cursor()

    c.execute("""
                SELECT p.name, p.value, p.datetime
                FROM persona AS p
                INNER JOIN registro AS r ON r.id = p.fk_registro_id
                WHERE r.dni = ?;""", (dni,))

    query_result = c.fetchall()

    # Retorno una Lista Vacía en caso de que el
    # DNI Ingresado no se encuentre en la DB.
    if query_result is None:
        conn.close()
        return []

    conn.close()

    return query_result


def fill_avg_count_value(dni):
    '''
    Función que devuelve el promedio
    del nivel de azúcar de la persona
    cuyo dni es pasado como parámetro.
    '''
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")
    c = conn.cursor()

    c.execute(
        """SELECT AVG(p.value), COUNT(p.datetime)
           FROM persona AS p
           INNER JOIN registro AS r
           ON p.fk_registro_id = r.id
           WHERE r.dni = ?;""", (dni,))

    query_result = c.fetchone()
    conn.close()

    return query_result


def extract_ages_gender():
    """
    Función que realiza una consulta
    a la DB y extrae el id junto con la edad
    de la persona y el sexo biológico.
    """
    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")
    c = conn.cursor()

    c.execute(
        """ SELECT p.fk_registro_id, p.age, p.gender
            FROM persona AS p
            INNER JOIN registro AS r
            ON r.id = p.fk_registro_id
            WHERE r.dni IN (SELECT r.dni FROM registro AS r);"""
    )

    ages = c.fetchall()

    conn.close()

    return ages


def extractfdb_person(dni):
    """
    Función que Busca en la DB
    (Base de Datos) y Extrae y
    Retorna los datos de la 
    persona según el DNI pasado 
    como parámetro.
    """

    conn = sqlite3.connect(db['database'])
    conn.execute("""PRAGMA foreign_keys = 1;""")

    c = conn.cursor()

    c.execute(       
        """ SELECT (p.value)
            FROM persona AS p
            INNER JOIN registro AS r ON  p.fk_registro_id = r.id
            WHERE r.dni = ?; """, (dni,))

    # Obtengo los Datos extraídos de la query
    query_result = c.fetchall()

    # Retorno una Lista Vacía en caso de que el
    # DNI Ingresado no se encuentre en la DB.
    if query_result is None:
        conn.close()
        return []

    # Cierro la Conexión con la DB.
    conn.close()
    return query_result

    