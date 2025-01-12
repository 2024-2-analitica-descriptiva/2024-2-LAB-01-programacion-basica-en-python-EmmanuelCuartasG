"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    key_counts = {}

    with open('/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv', mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 4:
                dict_entries = columns[4].split(',')
                for entry in dict_entries:
                    key = entry.split(':')[0]
                    if key in key_counts:
                        key_counts[key] += 1
                    else:
                        key_counts[key] = 1

    sorted_key_counts = dict(sorted(key_counts.items()))
    return sorted_key_counts


"""
Retorne un diccionario que contenga la cantidad de registros en que
aparece cada clave de la columna 5.

Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

"""
