"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_10(filepath):
    result = []

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 4:
                letter = columns[0]
                col4_count = len(columns[3].split(','))
                col5_count = len(columns[4].split(','))
                result.append((letter, col4_count, col5_count))

    return result

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_10(df))


"""
Retorne una lista de tuplas contengan por cada tupla, la letra de la
columna 1 y la cantidad de elementos de las columnas 4 y 5.

Rta/
[('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]


"""
