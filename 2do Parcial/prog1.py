import os

archivo = open("emple.txt", "a")
while True:
    # ingreso de datos    
    edad = int(raw_input("Ingrese la edad: "))
    if edad == 0:
        break
    nom_ape = raw_input("Ingrese Nombre y apellido: ")
    sueldo_basico = float(raw_input("Ingrese sueldo basico: "))
    while True:
        sexo = int(raw_input("Ingrese sexo (1-Varon , 2-Mujer): "))
        if sexo == 1 or sexo == 2:
            break
    while True:
        categoria = int(raw_input("Ingrese Categoria (1- Administrativo , 2-Mecanico, 3-Chofer): "))
        if categoria == 1 or categoria == 2 or categoria == 3:
            break
    # creacion del registro y posterior escritura
    registro = "{0},{1},{2},{3},{4}\n".format(edad, nom_ape, sueldo_basico, sexo, categoria)
    archivo.write(registro)
    # limpiar la pantalla
    os.system('cls' if os.name=='nt' else 'clear')

archivo.close()
