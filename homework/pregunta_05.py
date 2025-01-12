"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
por cada letra de la columa 1.

Rta/
[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""

def pregunta_05():
    letter_values = {}

    with open('/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv', mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 1:
                letter = columns[0]
                value = int(columns[1])
                if letter in letter_values:
                    letter_values[letter].append(value)
                else:
                    letter_values[letter] = [value]

    result = [(letter, max(values), min(values)) for letter, values in letter_values.items()]
    result.sort()
    return result