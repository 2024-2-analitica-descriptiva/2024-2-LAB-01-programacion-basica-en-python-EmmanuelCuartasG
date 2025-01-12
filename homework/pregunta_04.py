"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
cantidad de registros por cada mes, tal como se muestra a continuación.
Rta/
[('01', 3),
 ('02', 4),
 ('03', 2),
 ('04', 4),
 ('05', 3),
 ('06', 3),
 ('07', 5),
 ('08', 6),
 ('09', 3),
 ('10', 2),
 ('11', 2),
 ('12', 3)]

"""

def pregunta_04(filepath):
    month_counts = {str(i).zfill(2): 0 for i in range(1, 13)}

    with open(filepath, mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 2:
                date = columns[2]
                month = date.split('-')[1]
                if month in month_counts:
                    month_counts[month] += 1

    sorted_counts = sorted(month_counts.items())
    return sorted_counts

df = '/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv'
print(pregunta_04(df))