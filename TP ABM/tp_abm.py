import os


def crear_registro(cod_empleado, edad, nomyape, sueldo, existe):
    return "{0:3},{1:3},{2:30},{3:4},{4:1}\n".format(cod_empleado, edad, nomyape, sueldo, existe)  # longitud 48


def limpiar_pantalla():
        os.system('cls' if os.name =='nt' else 'clear')


def existe(cod_empleado, archivo):
    pos  = (cod_empleado * 48) - 48
    archivo.seek(pos, 0)
    try:
        linea = archivo.readline()
        cod = int(linea.split(',')[0].strip())
        baja_logica = int(linea.split(',')[4].strip())
        if cod == cod_empleado and baja_logica == 1:
            return True
        else:
            return False
    except:
        return False


def grabar(cod_empleado, nom_ape, edad, sueldo, existe, archivo):
    registro = crear_registro(cod_empleado, edad, nom_ape, sueldo, existe)
    pos = (cod_empleado * 48) - 48
    archivo.seek(pos, 0)
    archivo.write(registro)
    archivo.close()


def alta(filename):
    limpiar_pantalla()
    print "Alta de registros de empleado"
    try:
        archivo = open(filename, 'r+') # intento abrir el archivo en modo lectura / escritura
    except:
        archivo = open(filename, 'w') # creo el archivo en caso de no existir
    codigo = validator(int, "Ingrese codigo de empleado: ", "Presta Atencion, solo se permiten valores numericos")
    if existe(codigo, archivo):
        print "No se puede dar de alta, clave ya existe"
        raw_input("<< Presione una tecla para continuar >>")
        archivo.close()
        return
    nom_ape = raw_input("Nombre y apellido: ")
    edad = validator(int, "Edad: ", "Presta atencion, solo valores numericos")
    sueldo = validator(float, "Sueldo basico: ", "Presta atencion, solo valores numericos")
    grabar(codigo, nom_ape, edad, sueldo, 1, archivo)
    print "Empleado registrado"
    raw_input("<< Presione una tecla para continuar >>")


def validar_opcion(msg, low, high):
    while True:
        try:
            opcion = int(raw_input(msg))
            if opcion >= low and opcion <= high:
                return opcion
        except:
            print "Error, Ingrese un digito como opcion ({}-{})".format(low, high)

def baja(filename):
    limpiar_pantalla()
    print "Baja logica de empleado"
    try:
        archivo = open(filename, 'r+')  # abro el archivo en modo lectura / escritura
    except IOError:
        print "No existe el archivo {}".format(filename)
        raw_input("<< Presione ENTER para continuar >>")
        return
    codigo = validator(int, "Ingrese codigo de empleado: ", "Presta Atencion, solo se permiten valores numericos")
    # leo el registro
    pos = (codigo * 48) - 48
    archivo.seek(pos)
    linea = archivo.readline()
    try:
        cod = int(linea.split(',')[0].strip())
        # si existe un registro con el codigo ingresado
        if cod == codigo:
            # muestro el registro completo
            registro = linea.split(',')
            print "codigo\tedad\t nombre\tsueldo"
            print "-" * 50
            edad = registro[1]
            nyape = registro[2]
            sueldo = registro[3]
            print "{0}\t{1}\t{2}\t{3}".format(codigo, edad, nyape, sueldo)
            while True:
                opcion = raw_input("Esta seguro que desea borrarlo? [S/N]").upper()
                if opcion in ['N', 'S']:
                    break
                else:
                    print "Opcion no valida"
            if opcion == "S":
                grabar(codigo, nyape, edad, sueldo, 0, archivo)
                print "Registro eliminado!!!"
                raw_input("<< Oprima cualquier tecla para continuar >>")
                return
        else:
            # no existe el registro con el codigo ingresado
            print "No se puede modificar porque no existe"
            raw_input("<< Oprima cualquier tecla para continuar >>")
    except ValueError:
        # no existe el registro con el codigo ingresado
        print "No se puede modificar porque no existe"
        raw_input("<< Oprima cualquier tecla para continuar >>")


def validator(tipo, msg, error):
    while True:
        try:
            value = tipo(raw_input(msg))
            return  value
        except ValueError:
            print error

def modificacion(filename):
    limpiar_pantalla()
    print "Modificacion de empleado"
    try:
        archivo = open(filename, 'r+') # abro el archivo en modo lectura / escritura
    except IOError:
        print "No existe el archivo {}".format(filename)
        raw_input("<< Presione ENTER para continuar >>")
        return
    codigo = validator(int, "Ingrese codigo de empleado: ", "Presta Atencion, solo se permiten valores numericos")
    # leo el registro
    pos = (codigo * 48) - 48
    archivo.seek(pos)
    registro = archivo.readline().split(',')
    try:
        cod = int(registro[0].strip())
        # si existe un registro con el codigo ingresado
        if cod == codigo:
            # muestro el registro completo
            print "codigo\tedad\t nombre\tsueldo"
            print "-" * 50
            print "{0}\t{1}\t{2}\t{3}".format(registro[0], registro[1], registro[2], registro[3])
           
            msg = "Campo a modificar\n"
            msg += "1) Edad\n"
            msg += "2) Nombre y apellido\n"
            msg += "3) Sueldo\n"
            msg += "Ingrese opcion: "
            opcion = validar_opcion(msg, 1, 3)
            print "Anote el nuevo dato: "
            if opcion == 1:
                edad = validator(int, "Edad: ", "Presta atencion, solo valores numericos")
                grabar(codigo, edad, registro[2], registro[3], 1, archivo)
            elif opcion == 2:            
                nyape = raw_input("Nombre y Apellido: ")
                grabar(codigo, registro[1], nyape, registro[3], 1, archivo)
            elif opcion == 3:
                sueldo = validator(float, "Sueldo basico: ", "Presta atencion, solo valores numericos o '.'")
                grabar(codigo, registro[1], registro[2], sueldo, 1, archivo)
            print "Registro modificado"
            raw_input("<< Oprima cualquier tecla para continuar >>")
            return
        else:
            # no existe el registro con el codigo ingresado
            print "No se puede modificar porque no existe"
            raw_input("<< Oprima cualquier tecla para continuar >>")
    except ValueError:
        # no existe el registro con el codigo ingresado
        print "No se puede modificar porque no existe"
        raw_input("<< Oprima cualquier tecla para continuar >>")

def menu():
    FILENAME = 'maemple.txt'
    while True:
        limpiar_pantalla()
        print "         // MENU // "
        print "     1-  Alta"
        print "     2 - Baja"
        print "     3 - Modificacion"
        print "     4 - Salir"
        print "----------------------------"
        opcion = validar_opcion("Ingrese opcion: ", 1, 4)
        if opcion == 1:
            alta(FILENAME)
        elif opcion == 2:
            baja(FILENAME)
        elif opcion == 3:
            modificacion(FILENAME)
        elif opcion == 4:
            break


menu()
