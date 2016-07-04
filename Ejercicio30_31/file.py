import sys

BANKS_FILE = 'maebancos.txt'
ACCOUNTS_FILE = 'maecuentas.txt'

banks = {}
accounts = {}


def upload_banks():
    try:
        f = open(BANKS_FILE, 'r')
        for line in f.readlines():
            record = line.split(',')
            id = record[0].strip()
            description = record[1].strip()
            banks[id] = description
        f.close()
    except IOError:
        return banks

def search(id, collection):
    if id in collection:
        return collection[id]
    return None

def show(id):
    bank = search(id, banks)
    if bank:
        print "ID: {0} Descripcion: {1}".format(id, bank)
        pause()
    else:
        print "El Banco no existe!!"
        pause()

def bank_to_s(id, description):
    return "{0},{1}\n".format(id, description)

def save_banks():
    f = open(BANKS_FILE, 'w')
    for key, value in banks.items():
        record = bank_to_s(key, value)
        f.write(record)
    f.close()

def add_bank(id):
    bank = search(id, banks)
    if not bank:
        description = raw_input("Descripcion: ")
        banks[id] = description
        save_banks()
        print "{0} dado de alta con exito!!!".format(description)
        pause()
    else:
        print "El Banco ya ha sido dado de alta!!"
        pause()

def delete(id):
    bank = search(id, banks)
    if bank:
        print "Codigo de banco: {0}\nDescripcion: {1}".format(id, bank)
        opc = raw_input("Baja (B) Cancelar (C)").upper()
        if opc == 'B':
            del banks[id]
            save_banks()
            print "{0} dado de baja con exito!!".format(bank)
            pause()
    else:
        print "El banco no existe!!"
        pause()

def update(id):
    bank = search(id, banks)
    if bank:
        print "Codigo de banco: {0}\nDescripcion: {1}".format(id, bank)
        print "Anote el nuevo dato"
        description = raw_input("Descripcion: ")
        banks[id] = description
        save_banks()
        print "{0} modificado con exito!!!".format(bank)
        pause()
    else:
        print "El banco no existe!!"
        pause()

def upload_accounts():
    try:
        f = open(ACCOUNTS_FILE, 'r')
        for line in f.readlines():
            record = line.split(',')
            # id de cuenta
            id = record[0].strip()
            # id de banco
            bank = record[1].strip()
            # Descripcion de cuenta
            description = record[2].strip()
            accounts[id] = {'bank_id': bank, 'description': description}
        f.close()
    except IOError:
        return accounts

def account_to_s(account_id, bank_id, description):
    return "{0},{1},{2}\n".format(account_id, bank_id, description)

def save_account():
    fw = open(ACCOUNTS_FILE, 'w')
    for key, value in accounts.items():
        record = account_to_s(key, value['bank_id'], value['description'])
        fw.write(record)
    fw.close()


def add_account(bank_id):
    bank = search(bank_id, banks)
    if bank:
        print bank
        account_id = raw_input('Codigo de cuenta: ')
        if not search(account_id, accounts):
            description = raw_input("Descripcion de la cuenta: ")
            accounts[account_id] = {'bank_id' : bank_id, 'description': description}
            save_account()
            print "Cuenta dada de alta con exito!!"
            pause()
        else:
            print "La cuenta ya existe!!"
            pause()
    else:
        print "El Banco no existe!!"
        pause()



def pause():
    raw_input("Oprima una tecla para continuar")


def input_code():
    while True:
        try:
            bank_code = raw_input("Codigo Banco: ")
            return bank_code
        except ValueError:
            print "Presta atencion, solo digitos!!"

def clear_screen():
    import os
    os.system('cls') if os.name == 'nt' else os.system('clear')

def sub_menu():
    while True:
        clear_screen()
        prompt = "1)Alta de Banco\n2)Baja de Banco\n3)Modificacion de Banco\n"
        prompt += "4)Ver Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            add_bank(input_code())
        elif opc == 2:
            delete(input_code())
        elif opc == 3:
            update(input_code())
        elif opc == 4:
            id = input_code()
            show(id)
        elif opc == 5:
            menu()

def menu():
    while True:
        clear_screen()
        upload_banks()
        upload_accounts()
        prompt = "1)ABM Banco\n2)Alta de Cuenta\n3)Carga libro banco\n"
        prompt += "4) Informe Libro Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            sub_menu()
        elif opc == 2:
            bank_id = raw_input("Codigo de banco: ")
            add_account(bank_id)
        elif opc == 5:
            sys.exit()
menu()
