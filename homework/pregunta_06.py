"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


#def pregunta_06():
"""
La columna 5 codifica un diccionario donde cada cadena de tres letras
corresponde a una clave y el valor despues del caracter `:` corresponde al
valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
pequeño y el valor asociado mas grande computados sobre todo el archivo.

Rta/
[('aaa', 1, 9),
 ('bbb', 1, 9),
 ('ccc', 1, 10),
 ('ddd', 0, 9),
 ('eee', 1, 7),
 ('fff', 0, 9),
 ('ggg', 3, 10),
 ('hhh', 0, 9),
 ('iii', 0, 9),
 ('jjj', 5, 17)]

"""

def pregunta_06(filepath):
    key_values = {}

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 4:
                dict_entries = columns[4].split(',')
                for entry in dict_entries:
                    key, value = entry.split(':')
                    value = int(value)
                    if key in key_values:
                        key_values[key].append(value)
                    else:
                        key_values[key] = [value]

    result = [(key, min(values), max(values)) for key, values in key_values.items()]
    result.sort()
    return result

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_06(df))