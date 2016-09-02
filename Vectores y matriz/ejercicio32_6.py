# coding: utf-8

# informar el mayor de la suma del vector columna y el menor de la suma del vector fila.
# Una vez identificado en el vector fila el menor, indicar en que posición se encuentra.

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

def buscar(valor, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return (i, j)



def main():
    m = cargar_matriz(5, 7)
    mostrar_matriz(m)
    print
    columna = sumar_filas(m)
    print
    filas = sumar_columnas(m)
    print "Mayor del vector columna: {}".format(max(columna))
    menor = min(filas)
    print "Menor del vector filas: {}".format(menor)
    posicion = buscar(menor, m)
    print "Posicion del menor => {}, {}".format(posicion[0], posicion[1])
main()
