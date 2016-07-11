# coding: utf-8

# sumar los valores de las filas y guardar en un vector columna, sumar las columnas y guardar en un vector fila.

import random

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz

def cargar_matriz(filas, columnas):
    matriz = crear_matriz(filas, columnas)
    for fila in range(filas):
        for columna in range(columnas):
            # matriz[fila][columna] = input("Valor[{0}, {1}]: ".format(fila, columna))
            matriz[fila][columna] = random.randint(1, 100)
    return matriz

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            print  "{0} ".format(matriz[fila][columna]),
        print

def sumar_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    data = []
    for j in range(columnas):
        total = 0
        for i in range(filas):
            total += matriz[i][j]
        data.append(total)
    return data

def sumar_filas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    data = []
    for i in range(filas):
        total = 0
        for j in range(columnas):
            total += matriz[i][j]
        data.append(total)
    return data

def main():
    m = cargar_matriz(5, 7)
    mostrar_matriz(m)
    print
    columna = sumar_filas(m)
    print
    filas = sumar_columnas(m)
    print columna
    print filas
main()
