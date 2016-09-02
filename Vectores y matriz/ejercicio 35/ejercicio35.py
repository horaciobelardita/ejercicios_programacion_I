# coding: utf-8

ARCHIVO_MAESTRO_BANCOS = 'maestro_bancos.txt'
ARCHIVO_MAESTRO_CUENTAS = 'maestro_cuentas.txt'
ARCHIVO_NOVEDAD = 'novedades.txt'

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz

def subir_bancos(filename):
    bancos = {}
    with open(filename) as f:
        for linea in f:
            reg = linea.split(',')
            bancos[reg[0]] = reg[1]
    return bancos

def subir_cuentas(filename):
    cuentas = {}
    bancos = subir_bancos(ARCHIVO_MAESTRO_BANCOS)
    for banco in bancos:
        cuentas[banco] = []
    with open(filename) as f:
        for linea in f:
            reg = linea.split(',')
            cuenta = [reg[1], reg[2]]
            cuentas[reg[0]].append(cuenta)
    return cuentas

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz

def informe():
    cod_banco = raw_input("Codigo Banco: ")
    cuentas = subir_cuentas(ARCHIVO_MAESTRO_CUENTAS)
    bancos = subir_bancos(ARCHIVO_MAESTRO_BANCOS)
    print bancos[cod_banco]
    filas = len(cuentas[cod_banco][0])
    novedades = crear_matriz(filas, 4)
    

informe()
