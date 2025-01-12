"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12(filepath):
    letter_sums = {}

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 4:
                letter = columns[0]
                dict_entries = columns[4].split(',')
                total_value = sum(int(entry.split(':')[1]) for entry in dict_entries)
                if letter in letter_sums:
                    letter_sums[letter] += total_value
                else:
                    letter_sums[letter] = total_value

    sorted_letter_sums = dict(sorted(letter_sums.items()))
    return sorted_letter_sums

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_12(df))


"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 5 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""
