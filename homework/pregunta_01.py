"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_01():
    total = 0

    with open('/home/emmanuel/Documents/GitHub/2024-2-LAB-01-programacion-basica-en-python-EmmanuelCuartasG/files/input/data.csv', mode='r') as file:
        for line in file:
            columns = line.split('\t')
            if len(columns) > 1:
                total += int(columns[1])
    return total
