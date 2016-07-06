# 4. Generar una matriz de 5 filas y 7 columnas, sumar los valores de las filas y los valores de las columnas.

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
    for j in range(columnas):
        total = 0
        for i in range(filas):
            total += matriz[i][j]
        print "Valor columna {0}: {1}".format(j, total)

def sumar_filas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        total = 0
        for j in range(columnas):
            total += matriz[i][j]
        print "Valor Fila {0} : {1}".format(i, total)

def main():
    m = cargar_matriz(5, 7)
    mostrar_matriz(m)
    print
    sumar_columnas(m)
    print
    sumar_filas(m)

main()
