class Customer:

    def __init__(self, id, full_name="", initial_pos=0, end_pos=0):
        self.id = id
        self.full_name = full_name
        self.initial_pos = initial_pos
        self.end_pos = end_pos

    def __str__(self):
        return "{0:4.4},{1:30.30},{2:1.1},{3:1.1}\n".format(str(self.id), self.full_name, str(self.initial_pos), str(self.end_pos))

class Bill:

    def __init__(self, customer_id, date, bill_id, amount, next_record=0, previous_record=0):
        self.customer_id = customer_id
        self.date = date
        self.bill_id = bill_id
        self.amount = amount

class Customers:

    def __init__(self, filename):
        self.filename = filename
        self.load()


    def upload_in_memory(self):
        self.data = []
        with open(self.filename) as f:
            for line in f.readlines():
                record = line.split(',')
                customer = Customer(int(record[0].strip()),
                                    record[1].strip(),
                                    int(record[2].strip()),
                                    int(record[3].strip()))
                self.data.append(customer)

    def load(self):
        try:
            self.file = open(self.filename)
            self.upload_in_memory()
        except IOError:
            self.file = open(self.filename, 'w')
            self.data = []

    def exists(self, id):
        for customer in self.data:
            if customer.id == id:
                return True
        return False

    def save_data(self, customer):
        f = open(self.filename, 'a')
        f.write(str(customer))
        f.close()

    def add(self, id):
        if not self.exists(id):
            customer = Customer(id)
            customer.full_name = raw_input("Name: ")
            self.save_data(customer)
            print "Save successfully"
            Menu.pause()
        else:
            print "Customer already exists!!"
            Menu.pause()



class Menu:


    @staticmethod
    def pause():
        raw_input("Press ENTER to continue")

    @staticmethod
    def validate_range(prompt, low, high):
        while True:
            try:
                opc = int(raw_input(prompt))
                if opc >= low and opc <= high:
                    return opc
            except ValueError:
                print "Please enter only numbers"

    @staticmethod
    def menu():
        prompt = "1) Add Customer\n2)Add bill for customer\n3)Exit\nChoose: "
        while True:
            opc = Menu.validate_range(prompt, 1, 3)
            customers = Customers('customers.txt')
            if opc == 1:
                id = int(raw_input("Customer ID: "))
                customers.add(id)
            elif opc == 2:
                pass
            else:
                return

Menu.menu()
