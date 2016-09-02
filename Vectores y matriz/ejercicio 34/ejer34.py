import numpy

ARCHIVO_BANCOS = 'bancos.txt'
ARCHIVO_CUENTAS = 'cuentas.txt'
ARCHIVO_NOVEDAD = 'novedad.txt'

def subir_bancos():
    bancos = {}
    with open(ARCHIVO_BANCOS, 'r') as f:
        for line in f:
            reg = line.split(',')
            bancos[reg[0]] = reg[1]
    return bancos

def subir_cuentas():
    bancos = subir_bancos()
    cuentas = {}
    with open(ARCHIVO_CUENTAS, 'r') as f:
        for line in f:
            reg = line.split(',')
            cuentas[reg[0]] = reg[1]
    return bancos

mes = int(raw_input("Mes: "))
anio = int(raw_input("Anio: "))

print len(subir_bancos())
