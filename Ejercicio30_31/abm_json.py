import sys, json

BANKS_FILE = 'bancos.json'
banks = {}

def new_file(filename):
    f = open(filename, 'wb')
    f.close()


def load_file(filename):
    global banks
    try:
        with open(filename, 'rb') as b:
            banks = json.load(b)
    except IOError:
       new_file(filename)

def save_to_file(filename):
    global banks
    with open(filename, "wb") as b:
        json.dump(banks, b)

def display_menu():
    print """
    MENU
    1. Agregar Banco
    2. Modificar Banco
    3. Eliminar Banco
    4. Salir
    """

def exists(id):
    global banks
    return True if id in banks else False

def add_bank():
    id_bank = raw_input("Codigo del Banco: ")
    if not exists(id_bank):
        description = raw_input("Descripcion: ")
        banks[id_bank] = description
        save_to_file(BANKS_FILE)
    else:
        print "El Banco ya existe!!"


def modify_bank():
    id_bank = raw_input('Codigo del Banco: ')
    if exists(id_bank):
        print banks[id_bank]
        print "Anote el nuevo dato"
        description = raw_input("Descripcion: ")
        banks[id_bank] = description
        save_to_file(BANKS_FILE)
    else:
        print "El Banco no existe!!"

def delete_bank():
    id_bank = raw_input('Codigo del banco: ')
    if exists(id_bank):
        print banks[id_bank]
        confirm = raw_input("Baja (B) Cancelar (C)").upper()
        if confirm == 'B': del banks[id_bank]
        save_to_file(BANKS_FILE)
    else:
        print "El Banco no existe!!"

def quit():
    sys.exit(0)

def main():
    actions = {
                1: add_bank,
                2: modify_bank,
                3: delete_bank,
                4: quit
              }
    while True:
        load_file(BANKS_FILE)
        display_menu()
        print banks
        choise = input("Elija una opcion: ")
        action = actions.get(choise)
        if action:
            action()
        else:
            print "{0} opcion no valida!!".format(choise)

if __name__ == '__main__':
    main()
