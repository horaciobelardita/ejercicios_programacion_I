#abirir maaestroa cuenta, guardar cod cta y desc cta., comparar maestro bco, guardar desc bco, ir a nov y comparar cod bco & cod cta, mientras el año sea =  buscar mes dia e importe
#crear matrices
#leer arch
#informe cheque 2x2 y anioo
#informe dia_mes 32*13
def abro_arch(cuentas, banco, novedad):
    archcta = open(cuentas,'r+')
    archbco = open(banco,'r+')
    archnov = open(novedad,'r+')
    linea = archcta.readline()
    while linea != "":
        linea = linea.split(",")
        m=crear_matriz(2, 2)
        m[0][0] = int(linea[1])
        m[0][1] = int(linea[2])
        m[1][0] = int(linea[0])
        linea=archbco.readline()
        while linea != "":
            linea = linea.split("")
            if m[1][0] == int(linea[0]):
                m[1][1]=int(linea[1])
            linea=archbco.readline()
        while linea != "":
            linea = archnov.readline().split("")
            #importante recorrer todos los anios de dichos codigos
            if m[1][0] == int(linea[0]) and m[0][0] == int(linea[1]):
                anio = int(linea[2])
                anios = []
                while anio == int(linea[2]):
                    mat = crear_matriz(32, 13)
                    mat[int(linea[0])][mat[int(linea[1])]] = float(linea[8])
                    linea = archnov.readline().split("")
    linea=archcta.readline()


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas): #DEFINO FILAS
        matriz.append([0] * columnas) #DEFINO LAS COLUMNAS
    return matriz


def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(filas):
        for columna in range(columnas):
            print  "{0} ".format(matriz[fila][columna]),
        print

def leer_lineas(filename):
    _file = open(filename, 'r')
    data = _file.read().split('\n')
    _file.close()
    return data

def leer_datos(filename):
    matriz = []
    for columna in leer_lineas(filename):
        if columna:
            valores = columna.split(',')
            cod_banco = valores[0]
            desc = valores[1]
            matriz[fila][0] = cod_banco
            matriz[fila][1] = desc
            fila += 1
    return matriz

def main():
    cheques = abro_arch('cuentas.txt', 'maestro.txt', 'movimientos.txt')




main()
