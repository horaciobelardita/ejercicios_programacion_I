import numpy

ARCHIVO = 'datos.txt'

def procesar():
    mat = numpy.zeros((4, 4))
    with open(ARCHIVO, 'r') as f:
        for line in f:
            reg = line.split(',')
            mat[int(reg[2]) - 1][int(reg[1]) - 1] += 1
            mat[3][int(reg[1]) - 1] += 1
            mat[int(reg[2]) - 1][3] += 1
    # calcular el total de la ultima columna
    tot = 0
    for i in range(3):
        tot += mat[i][3]
    mat[3][3] = tot 
    return mat

print procesar()
