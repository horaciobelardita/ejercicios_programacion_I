# leer novedad
# m(cod_vendedor, cod_sucursal) = mm(cod_vendedor, cod_sucursal) + (cantidad * importe)
# leer siguiente
# fin novedad
import numpy

def subir_vendedores(archivo):
    '''Recorre el archivo maestro de vendedores y lo
    almacena en un diccionario[cod_vendedor] = nombre_apellido'''
    vendedores = {}
    for linea in archivo:
        reg = linea.split(',')
        vendedores[reg[0]] = reg[1]
    return vendedores


def procesar(reg):
    global matriz
    matriz[int(reg[1]) - 1][int(reg[0]) - 1] += (int(reg[5]) * float(reg[4]))
    matriz[int(reg[1]) - 1][5] += (int(reg[5]) * float(reg[4]))
    matriz[5][int(reg[0]) - 1] += (int(reg[5]) * float(reg[4]))

def listado(vendedores, matriz):
    print "Informe de Vendedores"
    for cod, nombre in vendedores.items():
        print cod, nombre, matriz[int(cod)-1][0],  matriz[int(cod)-1][1], \
        matriz[int(cod)-1][2],  matriz[int(cod)-1][3],  matriz[int(cod)-1][4], \
        'Total: ', matriz[int(cod) - 1][5]
    print "Totales: ", matriz[5][0], matriz[5][1], matriz[5][2], \
    matriz[5][3], matriz[5][4]


# abro y leo la cantidad de vendedores
arch_vendedores = open('VENDEDORES.txt', 'r')
vendedores = subir_vendedores(arch_vendedores)
arch_vendedores.close()
# creo la matriz con una fila mas y una columna mas para los totales
matriz = numpy.zeros((len(vendedores) + 1, 6))
# apertura, recorrido y procesamiento del archivo de novedades
arch_novedad = open('NOVEDAD.txt', 'r')
linea = arch_novedad.readline()
while linea != '':
    reg = linea.split(',')
    procesar(reg)
    linea = arch_novedad.readline()
arch_novedad.close()
# informe de listado de vendedores
listado(vendedores, matriz)
