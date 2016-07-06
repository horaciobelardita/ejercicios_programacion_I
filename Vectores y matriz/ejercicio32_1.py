# 1. Ingresar numeros en un vector de 10 elementos.

def cargar_vector():
    vector = []
    for i in range(10):
        numero = input("Ingrese un valor: ")
        vector.append(numero)
    return vector

def mostrar_vector(vector):
    for pos, item in enumerate(vector):
        print "Vector[{0}] => {1}".format(pos, item)

def menu():
    while True:
        prompt = "1) Cargar Vector\n2) Mostrar Vector\n3) Salir\nElija una opcion: "
        opc = input(prompt)
        if opc == 1:
            vector = cargar_vector()
        elif opc == 2:
            mostrar_vector(vector)
        else:
            break
menu()
