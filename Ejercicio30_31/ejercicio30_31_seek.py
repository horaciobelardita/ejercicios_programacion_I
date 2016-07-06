import sys, os

ARCHIVO_BANCOS = 'bancos.txt'
ARCHIVO_CUENTAS = 'cuentas.txt'
ARCHIVO_MOVIMIENTOS = 'movimientos.txt'


def pausa():
    raw_input("Oprima una tecla para continuar")


def ingreso_codigo():
    while True:
        try:
            codigo_banco = int(raw_input("Codigo Banco: "))
            return codigo_banco
        except ValueError:
            print "Presta atencion, solo digitos!!"

def limpiar_pantalla():
    import os
    os.system('cls') if os.name == 'nt' else os.system('clear')

def banco_to_s(codigo_banco, descripcion, existe):
    # longitud de la linea 38
    return "{0:4.4},{1:30.30},{2:1}\n".format(str(codigo_banco), descripcion, str(existe))


def buscar_banco(codigo_banco):
    pos = (codigo_banco * 38) - 38
    try:
        # existe el archivo
        f = open(ARCHIVO_BANCOS, 'r')
        f.seek(pos, 0)
        registro = f.read(38).split(',')
        f.close()
        if len(registro) > 1:
            return registro
        else:
            return None
    except IOError:
        # no existe el archivo entonces se crea
        f = open(ARCHIVO_BANCOS, 'w')
        f.close()
        return None


def guardar_banco(codigo_banco, descripcion, existe):
    registro = banco_to_s(codigo_banco, descripcion, existe)
    longitud = len(registro)
    pos = (codigo_banco * longitud) - longitud
    with open(ARCHIVO_BANCOS, 'r+') as f:
        f.seek(pos, 0)
        f.write(registro)

def existe_banco(codigo_banco):
    banco = buscar_banco(codigo_banco)
    # existe el banco
    if banco:
        # ademas no ha sido dado de baja
        if int(banco[2]) == 1:
            return True
    return False


def agregar_banco(codigo_banco):
    # no existe un banco con el codigo ingresado
    if not existe_banco(codigo_banco):
        descripcion = raw_input("Descripcion: ")
        guardar_banco(codigo_banco, descripcion, 1)
        print "{0}, dado de alta con exito!!".format(descripcion)
        pausa()
    # el banco ya existe
    else:
        print "El banco ya existe!!!"
        pausa()

def baja_banco(codigo_banco):
    if existe_banco(codigo_banco):
        banco = buscar_banco(codigo_banco)
        descripcion = banco[1].strip()
        print "Descripcion: {0}".format(descripcion)
        opc = raw_input("Baja (B) Cancelar (C): ").upper()
        if opc == 'B':
            guardar_banco(codigo_banco, descripcion, 0)
            print "{0} dado de baja con exito".format(descripcion)
            pausa()
    else:
        print "El Banco no existe!!"
        pausa()

def modificacion_banco(codigo_banco):
    if existe_banco(codigo_banco):
        banco = buscar_banco(codigo_banco)
        descripcion = banco[1].strip()
        print "Descripcion: {0}".format(descripcion)
        print "Anote el nuevo dato: "
        descr = raw_input("Descripcion: ")
        guardar_banco(codigo_banco, descr, 1)
        print "{0} modificado con exito!!".format(descripcion)
        pausa()
    else:
        print "El banco no existe!!"
        pausa()

def mostrar(codigo_banco):
    if existe_banco(codigo_banco):
        banco = buscar_banco(codigo_banco)
        print "ID: {0} Descripcion: {1}".format(codigo_banco, banco[1].strip())
    else:
        print "El banco no existe!!!"
    pausa()

def cuenta_to_s(codigo_cuenta, codigo_banco, descripcion_cuenta):
    # longitud del registro 42
    return "{0:5.5},{1:4.4},{2:30.30}\n".format(str(codigo_cuenta), str(codigo_banco), descripcion_cuenta)


def buscar_cuenta(codigo_cuenta):
    pos = (codigo_cuenta * 42) - 42
    try:
        # existe el archivo
        f = open(ARCHIVO_CUENTAS, 'r')
        f.seek(pos, 0)
        registro = f.read(42).split(',')
        f.close()
        if len(registro) > 1:
            return registro
        else:
            return None
    except IOError:
        # no existe el archivo entonces se crea
        f = open(ARCHIVO_CUENTAS, 'w')
        f.close()
        return None


def existe_cuenta(codigo_cuenta):
    cuenta = buscar_cuenta(codigo_cuenta)
    if cuenta:
        if int(cuenta[0].strip()) == codigo_cuenta:
            return True
    return False

def guardar_cuenta(codigo_cuenta, codigo_banco, descripcion_cuenta):
    registro = cuenta_to_s(codigo_cuenta, codigo_banco, descripcion_cuenta)
    longitud = len(registro)
    pos = (codigo_cuenta * longitud) - longitud
    with open(ARCHIVO_CUENTAS, 'r+') as f:
        f.seek(pos, 0)
        f.write(registro)

def agregar_cuenta(codigo_banco):
    if existe_banco(codigo_banco):
        banco = buscar_banco(codigo_banco)
        descripcion_banco = banco[1].strip()
        print "Descripcion Banco: {0}".format(descripcion_banco)
        codigo_cuenta = int(raw_input("Codigo de cuenta: "))
        if not existe_cuenta(codigo_cuenta):
            descripcion_cuenta = raw_input("Descripcion cuenta: ")
            guardar_cuenta(codigo_cuenta, codigo_banco, descripcion_cuenta)
            print "Cuenta creada con exito!!"
            pausa()
        else:
            print "La cuenta ya existe!!!"
            pausa()
    else:
        print "El Banco no existe!!"
        pausa()

def validar_tipo():
    comprobantes = ['Cheque', 'Boleta de Deposito', 'Nota de Debito', 'Nota de Credito']
    options = ''
    for k, comprobante in enumerate(comprobantes):
        options += "{0}) {1}\n".format(k+1, comprobante)
    options += "Elija una opcion: "
    while True:
        try:
            opt = int(raw_input(options))
            if 1 <= opt <= 4:
                return comprobantes[opt - 1]
            else:
                print "Presta atencion, opcion no valida!!!"
        except ValueError:
            print "Presta atencion, solo numeros!!!"

def obtener_id():
    count = 1
    if os.path.isfile(ARCHIVO_MOVIMIENTOS):
        with open(ARCHIVO_MOVIMIENTOS, 'r') as fr:
            for linea in fr:
                count += 1
        return count
    return count


def movimiento_to_s(id_movimiento,
                    codigo_cuenta,
                    fecha,
                    numero_comprobante,
                    tipo_comprobante,
                    detalle,
                    f_vto,
                    importe):
    # longitud del registro 80
    return "{0:5.5},{1:4.4},{2:8.8},{3:4.4},{4:15.15},{5:20.20},{6:8.8},{7:8.8}\n".format(str(id_movimiento),
                                                                                         str(codigo_cuenta),
                                                                                         fecha,
                                                                                         str(numero_comprobante),
                                                                                         tipo_comprobante,
                                                                                         detalle,
                                                                                         f_vto,
                                                                                         str(importe))


def guardar_movimiento(id_movimiento,
                       codigo_cuenta,
                       fecha,
                       numero_comprobante,
                       tipo_comprobante,
                       detalle,
                       f_vto,
                       importe):
    registro = movimiento_to_s(id_movimiento,
                               codigo_cuenta,
                               fecha,
                               numero_comprobante,
                               tipo_comprobante,
                               detalle,
                               f_vto,
                               importe)
    with open(ARCHIVO_MOVIMIENTOS, 'a') as f:
        f.write(registro)


def carga_datos(codigo_cuenta):
    id_movimiento = obtener_id()
    fecha = raw_input("Fecha: ")
    numero_comprobante = raw_input("Numero comprobante: ")
    tipo_comprobante = validar_tipo()
    detalle = raw_input("Detalle: ")
    f_vto = raw_input("Fecha de vencimiento: ")
    importe = raw_input("Importe: ")
    opc = raw_input("Grabar(G) Cancelar(C): ").upper()
    if opc == 'G':
        guardar_movimiento(id_movimiento,
                          codigo_cuenta,
                          fecha,
                          numero_comprobante,
                          tipo_comprobante,
                          detalle,
                          f_vto,
                          importe)
        print "Guardado con exito!!"

def mostrar_encabezado(codigo_cuenta):
    cuenta = buscar_cuenta(codigo_cuenta)
    descripcion_cuenta = cuenta[2].strip()
    codigo_banco = int(cuenta[1].strip())
    banco = buscar_banco(codigo_banco)
    codigo_banco = banco[0].strip()
    descripcion_banco = banco[1].strip()
    print "Descripcion Cuenta: {0}".format(descripcion_cuenta)
    print "Codigo Banco: {0}".format(codigo_banco)
    print "Descripcion Banco: {0}".format(descripcion_banco)



def agregar_movimiento(codigo_cuenta):
    if existe_cuenta(codigo_cuenta):
        mostrar_encabezado(codigo_cuenta)
        carga_datos(codigo_cuenta)
        pausa()
    else:
        print "La cuenta no existe!!"
        pausa()

def es_debe(tipo):
    if tipo == 'Cheque' or tipo == 'Nota de Debito':
        return True
    return False

def mostrar_lineas(codigo_cuenta):
    saldo = 0
    total_debe = 0
    total_haber = 0
    with open(ARCHIVO_MOVIMIENTOS, 'r') as f:
        for linea in f.readlines():
            registro = linea.split(',')
            if int(registro[1]) == codigo_cuenta:
                print "Fecha: {0}".format(registro[2])
                print "Detalle: {0}".format(registro[5])
                print "Numero comprobante: {0}".format(registro[3])
                tipo_comprobante = registro[4].strip()
                print "Tipo: {0}".format(tipo_comprobante)
                importe = float(registro[7])
                if es_debe(tipo_comprobante):
                    total_debe += importe
                    saldo += importe
                    print "Debe: ${0}".format(importe)
                    print "Haber: $0"
                else:
                    total_haber += importe
                    saldo -= importe
                    print "Debe: $0"
                    print "Haber: ${0}".format(importe)
                print "Saldo: ${0}".format(saldo)
                print "Fecha Vto: {0}".format(registro[6])
                print "-" * 50
    print "Total Debe: ${0}".format(total_debe)
    print "Total Haber: ${0}".format(total_haber)
    print "Total Saldo: ${0}".format(saldo)

def informe(codigo_cuenta):
    if existe_cuenta(codigo_cuenta):
        mostrar_encabezado(codigo_cuenta)
        mostrar_lineas(codigo_cuenta)
        pausa()
    else:
        print "La cuenta no registra ningun movimiento!!"
        pausa()

def sub_menu():
    while True:
        limpiar_pantalla()
        prompt = "1)Alta de Banco\n2)Baja de Banco\n3)Modificacion de Banco\n"
        prompt += "4)Ver Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            agregar_banco(ingreso_codigo())
        elif opc == 2:
            baja_banco(ingreso_codigo())
        elif opc == 3:
            modificacion_banco(ingreso_codigo())
        elif opc == 4:
            id = ingreso_codigo()
            mostrar(id)
        elif opc == 5:
            menu()

def menu():
    while True:
        limpiar_pantalla()
        prompt = "1)ABM Banco\n2)Alta de Cuenta\n3)Carga libro banco\n"
        prompt += "4) Informe Libro Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            sub_menu()
        elif opc == 2:
            id_banco = input("Codigo de banco: ")
            agregar_cuenta(id_banco)
        elif opc == 3:
            id_cuenta = input("Codigo de cuenta: ")
            agregar_movimiento(id_cuenta)
        elif opc == 4:
            id_cuenta = input("Codigo de cuenta: ")
            informe(id_cuenta)
        elif opc == 5:
            sys.exit()

menu()
