"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_07(filepath):
    value_letters = {}

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 1:
                letter = columns[0]
                value = int(columns[1])
                if value in value_letters:
                    value_letters[value].append(letter)
                else:
                    value_letters[value] = [letter]

    result = sorted(value_letters.items())
    return result

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_07(df))


"""
Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
contiene un valor posible de la columna 2 y una lista con todas las letras
asociadas (columna 1) a dicho valor de la columna 2.

Rta/
[(0, ['C']),
    (1, ['E', 'B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E', 'E', 'D']),
    (4, ['E', 'B']),
    (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
    (6, ['C', 'E', 'A', 'B']),
    (7, ['A', 'C', 'E', 'D']),
    (8, ['E', 'D', 'E', 'A', 'B']),
    (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

"""
