"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    letter_sums = {}

    with open('files/input/data.csv', mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 3:
                value = int(columns[1])
                letters = columns[3].split(',')
                for letter in letters:
                    if letter in letter_sums:
                        letter_sums[letter] += value
                    else:
                        letter_sums[letter] = value

    sorted_letter_sums = dict(sorted(letter_sums.items()))
    return sorted_letter_sums



"""
Retorne un diccionario que contengan la suma de la columna 2 para cada
letra de la columna 4, ordenadas alfabeticamente.

Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


"""
