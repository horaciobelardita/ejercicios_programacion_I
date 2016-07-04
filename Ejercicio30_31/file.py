import sys

class Banks:

    def __init__(self, filename):
        self.filename = filename
        self.banks = {}
        self.load()

    def upload_in_memory(self, f):
        for line in f.readlines():
            record = line.split(',')
            id = record[0].strip()
            description = record[1].strip()
            self.banks[id] = description

    def load(self):
        try:
            f = open(self.filename, 'r')
            self.upload_in_memory(f)
        except IOError:
            return

    def search(self, id):
        if id in self.banks:
            return self.banks[id]
        return None

    def show(self, id):
        bank = self.search(id)
        if bank:
            print "ID: {0} Descripcion: {1}".format(id, bank)
            pause()
        else:
            print "El Banco no existe!!"
            pause()

    def to_s(self, id, description):
        return "{0:4.4},{1:30.30}\n".format(id, description)

    def save(self):
        f = open('maebancos.txt', 'w')
        for key, value in self.banks.items():
            record = self.to_s(key, value)
            f.write(record)
        f.close()

    def add(self, id):
        bank = self.search(id)
        if not bank:
            description = raw_input("Descripcion: ")
            self.banks[id] = description
            self.save()
            print "{0} dado de alta con exito!!!".format(description)
            pause()
        else:
            print "El Banco ya ha sido dado de alta!!"
            pause()

    def delete(self, id):
        bank = self.search(id)
        if bank:
            print "Codigo de banco: {0}\nDescripcion: {1}".format(id, bank)
            opc = raw_input("Baja (B) Cancelar (C)").upper()
            if opc == 'B':
                del self.banks[id]
                self.save()
                print "{0} dado de baja con exito!!".format(bank)
                pause()
        else:
            print "El banco no existe!!"
            pause()

    def update(self, id):
        bank = self.search(id)
        if bank:
            print "Codigo de banco: {0}\nDescripcion: {1}".format(id, bank)
            print "Anote el nuevo dato"
            description = raw_input("Descripcion: ")
            self.banks[id] = description
            self.save()
            print "{0} modificado con exito!!!".format(bank)
            pause()
        else:
            print "El banco no existe!!"
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
        banks = Banks('maebancos.txt')
        if opc == 1:
            banks.add(input_code())
        elif opc == 2:
            banks.delete(input_code())
        elif opc == 3:
            banks.update(input_code())
        elif opc == 4:
            id = input_code()
            banks.show(id)
        elif opc == 5:
            menu()

def menu():
    while True:
        clear_screen()
        prompt = "1)ABM Banco\n2)Alta de Cuenta\n3)Carga libro banco\n"
        prompt += "4) Informe Libro Banco\n5)Salir\nElija una opcion: "
        opc = int(raw_input(prompt))
        if opc == 1:
            sub_menu()
        elif opc == 2:
            pass
        elif opc == 5:
            sys.exit()
menu()
