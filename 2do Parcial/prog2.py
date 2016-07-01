import sys

# Funciones
def registro_a_cadena(nom_apell, sueldo, sexo, categoria):
    if sexo == 1:
        str_sexo = "Varon"
    else:
        str_sexo = "Mujer"
    if categoria == 1:
        str_categoria = "Administrativo"
    elif categoria == 2:
        str_categoria = "Mecanico"
    else:
        str_categoria = "Chofer"
    str_reg = "{0}\t\t {1}\t\t {2}\t {3}\t".format(nom_apell, sueldo, str_sexo, str_categoria)
    return str_reg




try:
    archivo = open("emple.txt", "r")
except IOError:
    # si no encuentra el archivo finaliza el programa
	print("Error, No se ha encontrado el archivo emple.txt")
	raw_input("Presione <ENTER> para continuar")
	sys.exit()

# contadores
cant_personas = 0
total_sueldo = 0
total_sueldo_mecanico = 0
total_sueldo_admin = 0
total_sueldo_chofer = 0
cant_personas_20_40 = 0
cant_personas_25_30_admin = 0
cant_mecanicos_sueldo_500_2000 = 0
cant_persona_pepe = 0
cant_persona_jose = 0
cant_mujeres = 0
cant_persona_maria = 0
cant_varones_20_40 = 0

# encabezado
print "################### Padron de empleados ################"
print "Nombre Y Apellido\t Sueldo Basico\t  sexo\t  Categoria\t"
nro_linea = 0

linea = archivo.readline()
while linea != "":

    registro = linea.split(',')
    edad = int(registro[0])
    nom_apell = registro[1]
    sueldo = float(registro[2])
    sexo = int(registro[3])
    categoria = int(registro[4])

    # generar para imprimir el registro
    str_reg = registro_a_cadena(nom_apell, sueldo, sexo, categoria)
    print str_reg
	
    nro_linea += 1
    if nro_linea == 20:
		# encabezado
		print "################### Padron de empleados ################"
		print "Nombre Y Apellido\t Sueldo Basico\t  sexo\t  Categoria\t"
		nro_linea = 1
    # proceso
    cant_personas += 1
    total_sueldo += sueldo
    # acumular sueldo Administrativo
    if categoria == 1:
        total_sueldo_admin += sueldo
    # acumular sueldo Mecanico
    elif categoria == 2:
        total_sueldo_mecanico += sueldo
    else:
        # acumular sueldo chofer
        total_sueldo_chofer += sueldo
    # La cantidad de Personas entre 20 y 40 anios
    if edad >= 20 and edad <= 40:
        cant_personas_20_40 += 1
    # La cantidad de Personas entre 25 y 30 anios con categoria Administrativo
    if edad >= 25 and edad <= 30 and categoria == 1:
        cant_personas_25_30_admin += 1
    # La cantidad de Mecanicos con sueldo > 500 y menos a 2000 pesos
    if categoria == 2:
        if sueldo > 500 and sueldo < 2000:
            cant_mecanicos_sueldo_500_2000 += 1
    # Cantidad de persona que se llama Pepe
    if nom_apell.upper().find("PEPE") >= 0:
        cant_persona_pepe += 1
    # Cantidad de personas que se llama Jose y es chofer.
    if nom_apell.upper().find("JOSE") >= 0 and categoria == 3:
        cant_persona_jose += 1
    # cantidad de mujeres
    if sexo == 2:
        cant_mujeres += 1
        # Cantidad de mujeres administrativa y se llame maria
        if categoria == 1 and nom_apell.upper().find("MARIA") >= 0:
            cant_persona_maria += 1
    # Cantidad de varones entre 20 y 40 anios de edad,
    elif edad >= 20 and edad <= 40:
        cant_varones_20_40 += 1
    linea = archivo.readline()


archivo.close()

# mostrar resultados
print "Cantidad de personas: ", cant_personas
print "Total de sueldo a pagar: ", total_sueldo
print "Promedio de sueldo a pagar: ", total_sueldo / cant_personas
print "Sueldo a pagar Administrativo: ", total_sueldo_admin
print "Sueldo a pagar Mecanico: ", total_sueldo_mecanico
print "Sueldo a pagar Chofer: ", total_sueldo_chofer
print "Cantidad de personas entre 20 y 40 anios: ", cant_personas_20_40
print "Cantidad de personas entre 25 y 30 anios y Administrativo: ", cant_personas_25_30_admin
print "Cantidad de mecanicos con sueldo > 500 y sueldo < 2000: ", cant_mecanicos_sueldo_500_2000
print "Cantidad de personas llamada Pepe: ", cant_persona_pepe
print "Cantidad de personas que se llama Jose y es chofer: ", cant_persona_jose
print "Cantidad de mujeres: ", cant_mujeres
print "Cantidad de mujeres Administrativa y se llama Maria: ", cant_persona_maria
print "Cantidad de varones entre 20 y 40 anios de edad: ", cant_varones_20_40
