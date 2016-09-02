

def crear_registro_banco(cod_banco, descripcion, posini, posfin):
    # longitud del registro 40
    return "{0:4.4},{1:30.30},{2:1},{3:1}\n".format(str(cod_banco), descripcion, posini, posfin)

def guardar_banco(cod_banco, descripcion, posini, posfin):
    with open()

def carga_banco(filename):
    cod_banco = input("Codigo Banco: ")
    descripcion = raw_input("Descripcion Banco: ")
    guardar_banco(cod_banco, descripcion, 0, 0)




def mostrar_menu():
    print """
    MENU
    1. Carga Banco
    2. Carga Cuenta
    3. Carga Movimientos
    4. Mostrar Movimientos
    5. Salir
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


print len(crear_registro_banco(1,"Banco Macro",0,0))
