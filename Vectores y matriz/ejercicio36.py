# coding: utf-8

ARCHIVO_MAESTRO = 'maestro_vendedores.txt'
ARCHIVO_NOVEDAD = 'novedades.txt'

def crear_matriz(filas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * 6)
    return matriz

def subir_vendedores(filename):
    vendedores = {}
    with open(filename) as f:
        for linea in f:
            reg = linea.split(',')
            vendedores[reg[0]] = crear_matriz(1)
            vendedores[reg[0]][0][0] = reg[1]
    return vendedores



def subir_novedades():
    vendedores = subir_vendedores(ARCHIVO_MAESTRO)
    with open(ARCHIVO_NOVEDAD, 'r') as f:
        for linea in f:
            reg = linea.split(',')
            vendedores[reg[1]][0][int(reg[0])] += float(reg[4])
    return vendedores


def informe():
    print "Informe por vendedores"
    vendedores = subir_novedades()
    total_suc_1 = 0
    total_suc_2 = 0
    total_suc_3 = 0
    total_suc_4 = 0
    total_suc_5 = 0
    for clave, valor in vendedores.items():
        total = valor[0][1] + valor[0][2] + valor[0][3] +  valor[0][4] + valor[0][5]
        linea = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\tTotal: {7}".format(clave, valor[0][0].strip(), valor[0][1], valor[0][2], valor[0][3], valor[0][4], valor[0][5], total)
        total_suc_1 += valor[0][1]
        total_suc_2 += valor[0][2]
        total_suc_3 += valor[0][3]
        total_suc_4 += valor[0][4]
        total_suc_5 += valor[0][5]
        print linea
    totales = "\tTotales: {0}\t{1}\t{2}\t{3}\t{4}".format(total_suc_1, total_suc_2, total_suc_3, total_suc_4, total_suc_5)
    print totales

informe()
