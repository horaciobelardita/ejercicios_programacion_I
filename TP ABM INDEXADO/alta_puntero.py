import sys

def CargaCliente(FileCargaCli):
    nombrecli = raw_input('\n Ingrese nombre Cliente \n')
    archivo = open(FileCargaCli, 'a+')
    linea = archivo.readline()
    if linea == "":
            cod = 1         #Si encuentro vacio el arch arranco en codigo 1
    else:
        while linea != "":
            linea = linea.split(",")
            cod = int(linea[0])         #Autoincremento de la clave codigo
            cod = cod+1
            linea = archivo.readline()
    posini = 0
    posfin = 0
    registro = crear_registro(cod, nombrecli, posini, posfin)
    archivo.write(registro)
    archivo.close()
    print 'Cliente cargado \n'

def crear_registro(cod, nombrecli, posini, posfin):
    return "{0:4.4},{1:30.30},{2:1},{3:1}\n".format(str(cod), nombrecli, posini, posfin) #40 espacios

def crear_registro_mov(codcli, fecha, NumFactura, importe, RegSig, RegAnt):
    return "{0:4.4},{1:8.8},{2:4.4},{3:8.8},{4:1},{5:1}\n".format(str(codcli), fecha, str(NumFactura), str(importe), RegSig, RegAnt) #32

def CargaMov(FileCargaMov, FileCargaCli):
    archcli = open(FileCargaCli, 'r+')
    try:
        # existe el archivo
        archmov = open(FileCargaMov, 'r+')
    except IOError:
        # no existe el archivo por lo tanto se crea
        archmov = open(FileCargaMov, 'w+')
    codcli = input("Ingrese codigo cliente \n")
    fecha = raw_input("Ingrese la fecha actual \n")
    importe = input("Ingrese importe total \n")
    linea = archmov.readline()
    if linea == "":
        NumFactura = 1
        RegSig = 0                  #Arranco predeterminado el archivo con  num fact en 1 y los punteros en 0
        RegAnt = 0
        posini = 1                  #Pos Inici 1 xq abre nuevo el .txt
        posfin = 1
        registromov = crear_registro_mov(codcli, fecha, NumFactura, importe, RegSig, RegAnt)
        archmov.write(registromov)
        pos = (codcli * 40) - 40
        archcli.seek(pos, 0)
        registrocli = archcli.readline().split(',')
        nombrecli = registrocli[1]
        registrocli = crear_registro(codcli, nombrecli, posini, posfin)
        archcli.seek(pos, 0)
        archcli.write(registrocli)
    else:                                   #En caso que el archivo ya este creado
        while linea.strip() != "":
            linea = linea.split(",")
            NumFactura = int(linea[2])      #Autoincremento de num factura
            NumFactura = NumFactura + 1
            linea = archmov.readline()
        print NumFactura
        pos = (codcli * 40) - 40
        archcli.seek(pos, 0)                   #Busco el num d cliente y verifico las posiciones iniciales
        registrocli = archcli.readline()
        registrocli = registrocli.split(',')
        posini = int(registrocli[2])
        nombrecli = registrocli[1]
        if posini == 0:             #Si la pos ini es 0 significa que es nuevo en el registro de mov
            posini = NumFactura
            posfin = NumFactura
            RegAnt = 0
            RegSig = 0
            registrocli = crear_registro(codcli, nombrecli, posini, posfin)
            pos = (codcli * 40) - 40
            archcli.seek(pos, 0)
            archcli.write(registrocli)
            registromov = crear_registro_mov(codcli, fecha, NumFactura, importe, RegSig, RegAnt)
            # guardar al final del archivo
            archmov.seek(0, 2)
            archmov.write(registromov)
        else:
            RegAnt = int(registrocli[3])     #sino se verifica cual es su pos final y se actualizan los punteros
            RegSig = 0
            posfin = NumFactura         #actrualizo la pos final del cli con el nuevo mov
            registrocli = crear_registro(codcli, nombrecli, posini, posfin)
            pos = (codcli * 40) - 40
            archcli.seek(pos, 0)
            archcli.write(registrocli)
            registromov = crear_registro_mov(codcli, fecha, NumFactura, importe, RegSig, RegAnt)
            longitud = len(registromov)
            archmov.seek(0, 2)
            archmov.write(registromov)
            RegSig = NumFactura #Actualizo el RegSig del anterior movimiento de esta cuenta
            # lectura del registro anterior
            pos = (RegAnt * longitud) - longitud
            archmov.seek(pos, 0)
            registromov = archmov.readline().split(',')
            fecha = registromov[1]
            NumFactura = registromov[2]
            importe = registromov[3]
            RegAnt = registromov[5].strip()
            registromov = crear_registro_mov(codcli, fecha, NumFactura, importe, RegSig, RegAnt)
            # escritura del registro anterior
            archmov.seek(pos, 0)
            archmov.write(registromov)
    archmov.close()
    archcli.close()
    print "Movimiento cargado con exito!!!"
    raw_input("Oprima una tecla para continuar")

def buscar_cliente(cod, nombre_archivo):
    '''Dado un codigo de cliente y un archivo lo busca en el mismo'''
    pos = (cod * 40) - 40
    with open(nombre_archivo, 'r') as f:
        f.seek(pos, 0)
        linea = f.readline()
        if len(linea.strip()) > 0:
            registro = linea.split(',')
            cod_cli = int(registro[0])
            if cod == cod_cli:
                return registro
    return None

def mostrar_movimientos(registro, FileCargaMov):
    '''Muesta linea por linea los registros de movimientos'''
    posini = int(registro[2])
    posfin = int(registro[3])
    archmov = open(FileCargaMov, 'r')
    # leer el primer registro
    pos = (posini * 32) - 32
    archmov.seek(pos, 0)
    registromov = archmov.readline().split(',')
    print "Fecha: {0}".format(registromov[1])
    print "Numero Factura: {0}".format(registromov[2])
    print "Importe: ${0}".format(registromov[3])
    print "-" * 50
    reg_sig = int(registromov[4])
    # leer los demas registros del cliente
    while reg_sig != 0:
        pos = (reg_sig * 32) - 32
        archmov.seek(pos, 0)
        registromov = archmov.readline().split(',')
        print "Fecha: {0}".format(registromov[1])
        print "Numero Factura: {0}".format(registromov[2])
        print "Importe: ${0}".format(registromov[3])
        print "-" * 50
        reg_sig = int(registromov[4])
    archmov.close()

def Movivimientos(FileCargaCli, FileCargaMov):
    '''Dado un codigo de cliente muestra todos sus Movimientos
    registrados en el archivo de Movimientos'''
    codcli = input("Codigo de cliente: ")
    registro = buscar_cliente(codcli, FileCargaCli)
    # existe el cliente
    if registro:
        print "Movimientos"
        mostrar_movimientos(registro, FileCargaMov)
    else:
        print "El cliente no existe!!!"
    raw_input("<< Presione una tecla para continuar >>")


def mostrar_menu():
    print """
    MENU
    1. Carga Cliente
    2. Carga Movimiento
    3. Mostrar Movimientos
    4. Salir
    """
def salir():
    print "Gracias por usar este programa!!!"
    sys.exit(0)


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ")
        if opcion == 1:
            CargaCliente("cargacliLista.txt")
        elif opcion == 2:
            CargaMov("cargamovLista.txt", "cargacliLista.txt")
        elif opcion == 3:
            Movivimientos("cargacliLista.txt", "cargamovLista.txt")
        elif opcion == 4:
            salir()
        else:
            print "{0}, opcion no valida.".format(opcion)


main()
