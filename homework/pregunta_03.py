"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
Retorne la suma de la columna 2 por cada letra de la primera columna como
una lista de tuplas (letra, suma) ordendas alfabeticamente.

Rta/
[('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

"""

def pregunta_03(filepath):
    letter_sums = {}

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 1:
                letter = columns[0]
                value = int(columns[1])
                if letter in letter_sums:
                    letter_sums[letter] += value
                else:
                    letter_sums[letter] = value

    sorted_sums = sorted(letter_sums.items())
    return sorted_sums

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_03(df))
