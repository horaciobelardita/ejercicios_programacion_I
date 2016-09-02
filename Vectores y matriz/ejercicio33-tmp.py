def crear_matriz(fila, columna):
    matriz = []
    for i in range(fila):
        matriz.append([0] * columna)
    return matriz

def subir_maestro(filename):
    maestro = {}
    with open(filename, 'r') as f:
        for linea in f:
            reg = linea.split(',')
            maestro[reg[0]] = reg[1].strip()
    return maestro

def subir_cuentas(filename):
    cuentas = {}
    with open(filename, 'r') as f:
        for linea in f:
            reg = linea.split(',')
    return cuentas


print subir_maestro('maestro.txt')

print subir_cuentas('cuentas.txt')
