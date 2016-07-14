# coding: utf-8

def contar_lineas(filename):
    _file = open(filename, 'r')
    count = 0
    for linea in _file:
        count += 1
    _file.close()
    return count

def leer_lineas(filename):
    _file = open(filename, 'r')
    data = _file.read().split('\n')
    _file.close()
    return data

def leer_datos(filename):
    '''Retorna la matriz cargada con los
    datos leidos desde el archivo pasado por parametro'''
    filas = contar_lineas(filename)
    columnas = 2
    matriz = crear_matriz(filas, columnas)
    fila = 0 # fila
    for columna in leer_lineas(filename):
        if columna:
            valores = columna.split(',')
            cod_banco = valores[0]
            desc = valores[1]
            matriz[fila][0] = cod_banco
            matriz[fila][1] = desc
            fila += 1
    return matriz

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz

def informe(matriz):
    print "Codigo Banco\tDescripcion"
    for f in range(len(matriz)):
        print "{}\t\t{}".format(matriz[f][0], matriz[f][1])



def ordenamiento(matriz):
    '''Retorna la matriz ordenada por el metodo
    de la burbuja'''
    for i in range(1, len(matriz)):
        for j in range(len(matriz) - i):
            if matriz[j][1] > matriz[j+1][1]:
                temp = matriz[j][0], matriz[j][1]
                matriz[j][0], matriz[j][1] = matriz[j+1][0], matriz[j+1][1]
                matriz[j+1][0], matriz[j+1][1] = temp
    return matriz


def main():
    # lectura del archivo y carga en una matriz
    bancos = leer_datos('bancos.txt')
    bancos = ordenamiento(bancos)
    informe(bancos)


if __name__ == '__main__':
    main()
