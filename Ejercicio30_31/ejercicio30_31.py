import sys, os

ARCHIVO_BANCOS = 'maebancos.txt'
ARCHIVO_CUENTAS = 'maecuentas.txt'
ARCHIVO_MOVIMIENTOS = 'movimientos.txt'

bancos = {}
cuentas = {}
movimientos = {}

def subir_bancos():
    try:
        f = open(ARCHIVO_BANCOS, 'r')
        for linea in f.readlines():
            registro = linea.split(',')
            id = registro[0].strip()
            descripcion = registro[1].strip()
            bancos[id] = descripcion
        f.close()
    except IOError:
        return bancos

def buscar(id, colleccion):
    if id in colleccion:
        return colleccion[id]
    return None

def mostrar(id):
    banco = buscar(id, bancos)
    if banco:
        print "ID: {0} Descripcion: {1}".format(id, banco)
        pausa()
    else:
        print "El Banco no existe!!"
        pausa()

def banco_to_s(id, descripcion):
    return "{0},{1}\n".format(id, descripcion)

def guardar_bancos():
    f = open(ARCHIVO_BANCOS, 'w')
    for key, value in bancos.items():
        registro = banco_to_s(key, value)
        f.write(registro)
    f.close()

def agregar_banco(id):
    banco = buscar(id, bancos)
    if not banco:
        descripcion = raw_input("Descripcion: ")
        bancos[id] = descripcion
        guardar_bancos()
        print "{0} dado de alta con exito!!!".format(descripcion)
        pausa()
    else:
        print "El Banco ya ha sido dado de alta!!"
        pausa()

def baja_banco(id):
    banco = buscar(id, bancos)
    if banco:
        print "Codigo de banco: {0}\nDescripcion: {1}".format(id, banco)
        opc = raw_input("Baja (B) Cancelar (C)").upper()
        if opc == 'B':
            del bancos[id]
            guardar_bancos()
            print "{0} dado de baja con exito!!".format(banco)
            pausa()
    else:
        print "El banco no existe!!"
        pausa()

def modificacion_banco(id):
    banco = buscar(id, bancos)
    if banco:
        print "Codigo de banco: {0}\nDescripcion: {1}".format(id, banco)
        print "Anote el nuevo dato"
        descripcion = raw_input("Descripcion: ")
        bancos[id] = descripcion
        guardar_bancos()
        print "{0} modificado con exito!!!".format(banco)
        pausa()
    else:
        print "El banco no existe!!"
        pausa()

def subir_cuentas():
    try:
        f = open(ARCHIVO_CUENTAS, 'r')
        for linea in f.readlines():
            registro = linea.split(',')
            # id de cuenta
            id = registro[0].strip()
            # id de banco
            banco = registro[1].strip()
            # Descripcion de cuenta
            descripcion = registro[2].strip()
            cuentas[id] = {'id_banco': banco, 'descripcion': descripcion}
        f.close()
    except IOError:
        return cuentas

def cuenta_to_s(id_cuenta, id_banco, descripcion):
    return "{0},{1},{2}\n".format(id_cuenta, id_banco, descripcion)

def guardar_cuenta():
    fw = open(ARCHIVO_CUENTAS, 'w')
    for key, value in cuentas.items():
        registro = cuenta_to_s(key, value['id_banco'], value['descripcion'])
        fw.write(registro)
    fw.close()


def agregar_cuenta(id_banco):
    banco = buscar(id_banco, bancos)
    if banco:
        print banco
        id_cuenta = raw_input('Codigo de cuenta: ')
        if not buscar(id_cuenta, cuentas):
            descripcion = raw_input("Descripcion de la cuenta: ")
            cuentas[id_cuenta] = {'id_banco' : id_banco, 'descripcion': descripcion}
            guardar_cuenta()
            print "Cuenta dada de alta con exito!!"
            pausa()
        else:
            print "La cuenta ya existe!!"
            pausa()
    else:
        print "El Banco no existe!!"
        pausa()

def options():
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
                print "{0} opcion no valida!!".format(opt)
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

def movimiento_to_s(id_movimiento, id_cuenta, fecha,
                    numero_comprobante, tipo_comprobante, detalle, f_vto, importe):
    return "{0},{1},{2},{3},{4},{5},{6},{7}\n".format(id_movimiento,
                                            id_cuenta,
                                            fecha,
                                            numero_comprobante,
                                            tipo_comprobante,
                                            detalle,
                                            f_vto,
                                            importe)

def guardar_movimientos():
    with open(ARCHIVO_MOVIMIENTOS, 'a') as fw:
        for key, value in movimientos.items():
            registro = movimiento_to_s(key,
                                     value['id_cuenta'],
                                     value['fecha'],
                                     value['numero_comprobante'],
                                     value['tipo_comprobante'],
                                     value['detalle'],
                                     value['f_vto'],
                                     value['importe'])
            fw.write(registro)

def agregar_movimiento(id_cuenta):
    limpiar_pantalla()
    cuenta = buscar(id_cuenta, cuentas)
    if cuenta:
        print "Descripcion de cuenta: {0}".format(cuenta['descripcion'])
        id_banco = cuenta['id_banco']
        banco = buscar(id_banco, bancos)
        print "Codigo Banco: {0}".format(id_banco)
        print "Descripcion Banco: {0}".format(banco)
        fecha = raw_input("Fecha: ")
        numero_comprobante = int(raw_input("Numero de comprobante: "))
        tipo_comprobante = options()
        detalle = raw_input('Detalle: ')
        f_vto = raw_input("Fecha de vencimiento: ")
        importe = float(raw_input("Importe: "))
        id_movimiento = obtener_id()
        movimientos[id_movimiento] = {'id_cuenta': id_cuenta,
                                        'fecha' : fecha,
                                        'numero_comprobante' : numero_comprobante,
                                        'tipo_comprobante' : tipo_comprobante,
                                        'detalle' : detalle,
                                        'f_vto' : f_vto,
                                        'importe' : importe}
        guardar_movimientos()
        print "Movimiento guardado con exito!!!"
        pausa()
    else:
        print "La cuenta no existe!!"
        pausa()

def subir_movimientos():
    try:
        f = open(ARCHIVO_MOVIMIENTOS, 'r')
        for linea in f.readlines():
            registro = linea.split(',')
            # id de cuenta
            id_cuenta = registro[1]
            if id_cuenta not in movimientos:
                movimientos[id_cuenta] = []
            cuenta = buscar(id_cuenta, cuentas)
            # id de banco
            id_banco = cuenta['id_banco']
            # descripcion del banco
            descripcion = buscar(id_banco, bancos)
            # fecha
            fecha = registro[2]
            # numero de comprobante
            numero_comprobante = registro[3]
            # tipo de comprobante
            tipo_comprobante = registro[4]
            # Detalle
            detalle = registro[5]
            # fecha de vencimiento
            f_vto = registro[6]
            importe = float(registro[7])
            movimientos[id_cuenta].append({'id_banco': id_banco,
                                            'descripcion': descripcion,
                                            'fecha': fecha,
                                            'detalle' : detalle,
                                            'numero_comprobante':numero_comprobante,
                                             'tipo_comprobante' : tipo_comprobante,
                                             'f_vto' : f_vto,
                                             'importe' : importe})
        f.close()
    except IOError:
        return cuentas

def es_debe(tipo_comprobante):
    if tipo_comprobante == "Cheque" or tipo_comprobante == "Nota de Debito":
        return True
    return False


def informe(id_cuenta):
    subir_movimientos()
    cuenta = buscar(id_cuenta, cuentas)
    if cuenta:
        total_debe = 0
        total_haber = 0
        saldo = 0
        print "Descripcion de cuenta: {0}".format(cuenta['descripcion'])
        id_banco = cuenta['id_banco']
        banco = buscar(id_banco, bancos)
        print "Codigo Banco: {0}".format(id_banco)
        print "Descripcion Banco: {0}".format(banco)
        for item in movimientos[id_cuenta]:
            print "Fecha: {0}".format(item['fecha'])
            print "Detalle: {0}".format(item['detalle'])
            print "Nro comprobante: {0}".format(item['numero_comprobante'])
            print "Tipo comprobante: {0}".format(item['tipo_comprobante'])
            if es_debe(item['tipo_comprobante']):
                print "Debe: ${0}".format(item['importe'])
                total_debe += item['importe']
                saldo += item['importe']
                print "Haber: $0"
            else:
                print "Debe: $0"
                total_haber += item['importe']
                saldo -= item['importe']
                print "Haber : ${0}".format(item['importe'])
            print "Fecha Vencimiento: {0}".format(item['f_vto'])
            print "-" * 50
        print "Total Debe: ${0}".format(total_debe)
        print "Total Haber: ${0}".format(total_haber)
        print "Total Saldo: ${0}".format(saldo)
        pausa()
    else:
        print "La cuenta no existe!!!"
        pausa()

def pausa():
    raw_input("Oprima una tecla para continuar")


def ingreso_codigo():
    while True:
        try:
            codigo_banco = raw_input("Codigo Banco: ")
            return codigo_banco
        except ValueError:
            print "Presta atencion, solo digitos!!"

def limpiar_pantalla():
    import os
    os.system('cls') if os.name == 'nt' else os.system('clear')

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
        else:
            print "{0}, opcion no valida..".format(opc)
            pausa()

def menu():
    while True:
        limpiar_pantalla()
        subir_bancos()
        subir_cuentas()
        prompt = "1)ABM Banco\n2)Alta de Cuenta\n3)Carga libro banco\n"
        prompt += "4) Informe Libro Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            sub_menu()
        elif opc == 2:
            id_banco = raw_input("Codigo de banco: ")
            agregar_cuenta(id_banco)
        elif opc == 3:
            id_cuenta = raw_input("Codigo de cuenta: ")
            agregar_movimiento(id_cuenta)
        elif opc == 4:
            id_cuenta = raw_input("Codigo de cuenta: ")
            informe(id_cuenta)
        elif opc == 5:
            sys.exit()
        else:
            print "{0}, opcion no valida..".format(opc)
            pausa()
menu()
