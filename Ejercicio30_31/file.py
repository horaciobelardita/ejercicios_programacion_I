import sys, os

BANKS_FILE = 'maebancos.txt'
ACCOUNTS_FILE = 'maecuentas.txt'
TRANSACTION_FILE = 'movimientos.txt'

banks = {}
accounts = {}
transactions = {}

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

def options():
    receipts = ['Cheque', 'Boleta de Deposito', 'Nota de Debito', 'Nota de Credito']
    options = ''
    for k, receipt in enumerate(receipts):
        options += "{0}) {1}\n".format(k+1, receipt)
    options += "Elija una opcion: "
    while True:
        try:
            opt = int(raw_input(options))
            if 1 <= opt <= 4:
                return receipts[opt - 1]
            else:
                continue
        except ValueError:
            print "Presta atencion, opcion no valida!!!"

def get_id():
    count = 1
    if os.path.isfile(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, 'r') as fr:
            for line in fr:
                count += 1
        return count
    return count

def transaction_to_s(transaction_id, account_id, date,
                    receipt_number, receipt_type, detail, due_date, amount):
    return "{0},{1},{2},{3},{4},{5},{6},{7}\n".format(transaction_id,
                                            account_id,
                                            date,
                                            receipt_number,
                                            receipt_type,
                                            detail,
                                            due_date,
                                            amount)

def save_transactions():
    with open(TRANSACTION_FILE, 'a') as fw:
        for key, value in transactions.items():
            record = transaction_to_s(key,
                                     value['account_id'],
                                     value['date'],
                                     value['receipt_number'],
                                     value['receipt_type'],
                                     value['detail'],
                                     value['due_date'],
                                     value['amount'])
            fw.write(record)

def add_transaction(account_id):
    account = search(account_id, accounts)
    if account:
        print "Descripcion de cuenta: {0}".format(account['description'])
        bank_id = account['bank_id']
        bank = search(bank_id, banks)
        print "Codigo Banco: {0}".format(bank_id)
        print "Descripcion Banco: {0}".format(bank)
        date = raw_input("Fecha: ")
        receipt_number = int(raw_input("Numero de comprobante: "))
        receipt_type = options()
        detail = raw_input('Detalle: ')
        due_date = raw_input("Fecha de vencimiento: ")
        amount = float(raw_input("Importe: "))
        transaction_id = get_id()
        transactions[transaction_id] = {'account_id': account_id,
                                        'date' : date,
                                        'receipt_number' : receipt_number,
                                        'receipt_type' : receipt_type,
                                        'detail' : detail,
                                        'due_date' : due_date,
                                        'amount' : amount}
        save_transactions()




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
        elif opc == 3:
            account_id = raw_input("Codigo de cuenta: ")
            add_transaction(account_id)
        elif opc == 5:
            sys.exit()
menu()
