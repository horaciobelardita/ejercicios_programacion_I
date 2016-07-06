# 2. Con los datos ingresados del ejercicio anterior,   sumar los valores y determinar la  posicion del numero mayor.
def cargar_vector():
    vector = []
    for i in range(4):
        numero = input("Ingrese un valor: ")
        vector.append(numero)
    return vector

def sumar_valores(vector):
    suma = 0
    for item in vector:
        suma += item
    return suma

def buscar_mayor(vector):
    mayor = vector[0]
    i = 1
    while i < len(vector):
        if vector[i] > mayor:
            mayor = vector[i]
        i += 1
    return mayor

def menu():
    while True:
        prompt = "1) Cargar Vector\n2) Mostrar Suma Valores\n3) Mostrar Mayor\
        \n4) Salir\nElija una opcion: "
        opc = input(prompt)
        if opc == 1:
            vector = cargar_vector()
        elif opc == 2:
            print "Suma Total: {0}".format(sumar_valores(vector))
            # version corta
            # print sum(vector)
        elif opc == 3:
            print "Mayor: {0}".format(buscar_mayor(vector))
            # version corta
            # print max(vector)
        else:
            break
menu()
