ARCHIVO_BANCOS = 'bancos.txt'
ARCHIVO_CUENTAS = 'cuentas.txt'
ARCHIVO_NOVEDAD = 'novedad.txt'

def buscar_cuenta(cdo_cuenta):
    with open(ARCHIVO_CUENTAS, 'r') as f:
        for line in f:
            reg = line.split(',')
            if reg[1] == cdo_cuenta:
                return reg
    return None

def buscar_banco(cod_banco):
    with open(ARCHIVO_BANCOS, 'r') as f:
        for line in f:
            reg = line.split(',')
            if reg[0] == cod_banco:
                return reg[1]

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz

def generar_totales(cod_banco, cod_cuenta, anio):
    matriz = crear_matriz(32, 13)
    with open(ARCHIVO_NOVEDAD, 'r') as f:
        for line in f:
            reg = line.split(',')
            if reg[0] == cod_banco and reg[1] == cod_cuenta and reg[2] == anio:
                matriz[int(reg[4]) - 1][int(reg[3]) - 1] = matriz[int(reg[4]) - 1][int(reg[3]) - 1] + float(reg[8])
                matriz[31][int(reg[3]) - 1] = matriz[31][int(reg[3]) - 1] + float(reg[8])
    return matriz

cdo_cuenta = raw_input("Codigo de cuenta: ")
cuenta = buscar_cuenta(cdo_cuenta)
if cuenta:
    cod_cuenta = cuenta[1]
    print "Descricion de cuenta: ", cuenta[2]
    banco = buscar_banco(cuenta[0])
    cod_banco = cuenta[0]
    print "Codigo Banco: ", cod_banco,"Descricion Banco: ",  banco
    anio = raw_input("Anio: ")
    totales = generar_totales(cod_banco, cod_cuenta, anio)
    # impresion de dias / mes
    for i in range(31):
        print "Dia {}".format(i + 1)
        for j in range(13):
            print "Mes {}: {}".format(j+1, totales[i][j]),
        print
    print "Totales"
    # impresion de los totales
    for j in range(13):
        print "Mes {}: {}".format(j+1, totales[31][j]),
else:
    print "La cuenta no existe!!"
# importe == cdo_cuenta == cdo_banco == dia == mes == Anio
