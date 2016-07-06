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

def main():
    m = cargar_matriz(4, 3)
    mostrar_matriz(m)

main()
