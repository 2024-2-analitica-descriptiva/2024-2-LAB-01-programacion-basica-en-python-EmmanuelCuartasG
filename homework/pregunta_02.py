"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
Retorne la cantidad de registros por cada letra de la primera columna como
la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""

import csv

def pregunta_02(filepath):
    letter_counts = {}

    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            first_letter = row[0][0]
            if first_letter in letter_counts:
                letter_counts[first_letter] += 1
            else:
                letter_counts[first_letter] = 1

    sorted_counts = sorted(letter_counts.items())
    return sorted_counts

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_02(df))
