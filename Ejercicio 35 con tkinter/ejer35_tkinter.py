ARCHIVO_BANCOS = 'BANCOS.txt'
ARCHIVO_CUENTAS = 'CUENTAS.txt'
ARCHIVO_NOVEDAD = 'NOVEDADES.txt'

def upload_banks():
    '''Recorre el archivo maestro de BANCOS
    y lo almacena en una lista de diccionario'''
    banks = []
    with open(ARCHIVO_BANCOS, 'r') as f:
        for line in f:
            record = line.split(',')
            bank = {}
            bank['bank_id'] = int(record[0])
            bank['description'] = record[1].rstrip()
            banks.append(bank)
    return banks

def upload_accounts():
    '''Recorre el archivo maestro de cuentas y lo almacena
    en una lista de diccionarios'''
    accounts = []
    with open(ARCHIVO_CUENTAS, 'r') as f:
        for line in f:
            record = line.split(',')
            account = {}
            account['bank_id'] = int(record[0])
            account['account_id'] = int(record[1])
            account['description'] = record[2].rstrip()
            accounts.append(account)
    return accounts

def there_bank(id, banks):
    '''Retorna la posicion  si existe el codigo de banco en la lista de bancos
    -1 en caso contrario'''
    for pos, bank in enumerate(banks):
        if bank['bank_id'] == id:
            return pos
    return -1

def number_of_accounts(id, accounts):
    '''Retorna el numero de cuentas asociadas a un codigo de banco [id]'''
    count = 0
    for account in accounts:
        if account['bank_id'] == id:
            count += 1
    return count

def create_matriz(rows, columns):
    '''Retorna una matriz de n => rows x m => columns'''
    matriz = []
    for i in range(rows):
        matriz.append([0] * columns)
    return matriz

def search_account(id, accounts):
    '''Retorna la posicion  si existe el codigo de cuenta en la lista de cuentas
    -1 en caso contrario'''
    for pos, account in enumerate(accounts):
        if account['account_id'] == id:
            return pos
    return -1

def process(id, accounts):
    rows = number_of_accounts(id, accounts)
    # matriz para almacenar filas (nro cuentas) + total y  los 12 meses + total
    matriz = create_matriz(rows + 1, 12 + 1)
    with open(ARCHIVO_NOVEDAD, 'r') as f:
        for line in f:
            record = line.split(',')
            # si el codigo banco es igual al ingresado
            if int(record[0]) == id:
                cod = int(record[1]) - 1
                month = int(record[3]) - 1
                imp = float(record[5])
                matriz[cod][month] += imp
                matriz[cod][12] += imp
                matriz[rows][month] += imp
    return matriz

banks = upload_banks()
accounts = upload_accounts()

# pido el codigo de banco
code = int(raw_input('Codigo de banco: '))
# si existe el codigo de banco muestro el informe sino
# muestro un error
pos = there_bank(code, banks)
if pos >= 0:
    print banks[pos]['description']
    totals = process(code, accounts)
    print totals
else:
    print 'Codigo de banco no existe!!!'
