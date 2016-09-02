from PyQt5.QtWidgets import *
import sys

ARCHIVO_VENDEDOR = 'VENDEDORES.txt'
ARCHIVO_ARTICULO = 'ARTICULOS.txt'
ARCHIVO_NOVEDAD = 'NOVEDADES.txt'


class Controller:

    @staticmethod
    def create_matriz(rows, columns):
        matriz = []
        for i in range(rows):
            matriz.append([0] * columns)
        return matriz

    @staticmethod
    def upload_sellers():
        sellers = {}
        with open(ARCHIVO_VENDEDOR, 'r') as f:
            line = f.readline()
            while line != '':
                record = line.split(',')
                sellers[int(record[0])] = record[1].strip()
                line = f.readline()
        return sellers

    @staticmethod
    def upload_articles():
        articles = {}
        with open(ARCHIVO_ARTICULO, 'r') as f:
            line = f.readline()
            while line != '':
                record = line.split(',')
                articles[int(record[0])] = record[1]
                line = f.readline()
        return articles

    @staticmethod
    def month_to_str(x):
        meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }
        return meses[x] if x >= 1 and x <= 12 else ""
    @staticmethod
    def calculate_total(matriz):
        rows = len(matriz) - 1
        total = 0
        for i in range(rows):
            total += matriz[i][12]
        return total

    @staticmethod
    def search_best_article(matriz):
        rows = len(matriz) - 1
        mayor = 0
        article = 0, ""
        for i in range(rows):
            for j in range(12):
                if matriz[i][j] > mayor:
                    mayor = matriz[i][j]
                    article = i + 1, mayor
        return article

    @staticmethod
    def search_worst_month(article_id, matriz):
        row = article_id - 1
        menor = matriz[row][0]
        mes = 1
        for column in range(1, 12):
            if matriz[row][column] < menor:
                menor = matriz[row][column]
                mes = column + 1
        return mes

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.sellers = Controller.upload_sellers()
        self.articles = Controller.upload_articles()
        self.setup_ui()


    def setup_ui(self):
        vbox = QVBoxLayout(self)
        grid = QGridLayout()
        grid.addWidget(QLabel("COD VENDEDOR"), 0, 0)
        self.code_input = QLineEdit()
        grid.addWidget(self.code_input, 0, 1)
        self.search_name_button = QPushButton("Buscar", self)
        grid.addWidget(self.search_name_button, 0, 2)
        self.search_name_button.clicked.connect(self.search_by_name)
        grid.addWidget(QLabel("NOMBRE Y APELLIDO"), 1, 0)
        self.name_label = QLabel("")
        grid.addWidget(QLabel("NOMBRE Y APELLIDO"), 1, 0)
        grid.addWidget(self.name_label, 1, 1)
        grid.addWidget(QLabel("Anio"), 2, 0)
        self.year_input = QLineEdit()
        grid.addWidget(self.year_input, 2, 1)
        self.process_button = QPushButton("Procesar", self)
        self.process_button.setEnabled(False)
        self.process_button.clicked.connect(self.upload_matriz)
        grid.addWidget(self.process_button, 2, 2)
        vbox.addLayout(grid)
        vbox1 = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.prepare_table()
        vbox1.addWidget(self.table_widget)
        self.best_month = QLabel("")
        self.worst_month = QLabel("")
        vbox1.addWidget(self.best_month)
        vbox1.addWidget(self.worst_month)
        vbox.addLayout(vbox1)



    def search_by_name(self):
        # validacion que no este en blanco el codigo de empleado
        try:
            self.code = int(self.code_input.text())
        except ValueError:
            QMessageBox.critical(self, "Error", 'Debe ingresar un codigo numerico!!')
            self.code_input.setFocus()
            return
        seller = self.sellers.get(self.code)
        if seller:
            self.name_label.setText(seller)
            self.process_button.setEnabled(True)
        else:
            self.name_label.setText("No existe el vendedor")
        self.table_widget.setRowCount(0)

    def prepare_table(self):
        self.table_widget.setColumnCount(15)
        headers = ['COD ARTICULO', 'DESCRIPCION',
        "Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre", "Octubre","Noviembre","Diciembre", 'TOTALES']
        self.table_widget.setHorizontalHeaderLabels(headers)

    def upload_matriz(self):
        try:
            year_input = int(self.year_input.text())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Debe ingresar un anio en formato numerico')
            self.year_input.setFocus()
            return
        if year_input:
            rows = len(self.articles) + 1
            columns = 12 + 1
            self.matriz = Controller.create_matriz(rows, columns)
            with open(ARCHIVO_NOVEDAD, 'r') as f:
                line = f.readline()
                while line != '':
                    record = line.split(',')
                    seller_id = int(record[0])
                    article_id = int(record[1])
                    year = int(record[5])
                    month = int(record[4])
                    qtd = int(record[6])
                    price = float(record[7].strip())
                    if seller_id == self.code and year_input == year:
                        amount = price * qtd
                        self.matriz[article_id - 1][month - 1] += amount
                        self.matriz[rows - 1][month - 1] += amount
                        self.matriz[article_id - 1][12] += amount
                    line = f.readline()
            # calcular el total de totales
            self.matriz[rows-1][12] = Controller.calculate_total(self.matriz)
            self.fill_table()
            article = Controller.search_best_article(self.matriz)
            self.best_month.setText("Mejor Articulo => {} ${}".format(self.articles[article[0]], article[1]))
            month = Controller.search_worst_month(article[0], self.matriz)
            self.worst_month.setText("Peor mes del mejor articulo => {}".format(Controller.month_to_str(month)))
        else:
            QMessageBox.critical(self, 'Error', 'Debe ingresar un anio')
            self.year_input.setFocus()

    def fill_table(self):
        rows = len(self.matriz) - 1
        columns = len(self.matriz[0])
        r = 0
        key_articles = self.articles.keys()
        for i in range(rows):
            self.table_widget.insertRow(r)
            self.table_widget.setItem(r, 0, QTableWidgetItem(str(key_articles[i])))
            self.table_widget.setItem(r, 1, QTableWidgetItem(self.articles[key_articles[i]]))
            for j in range(columns):
                self.table_widget.setItem(r, j+2, QTableWidgetItem(str(self.matriz[i][j])))
            r += 1
        self.table_widget.insertRow(r)
        self.table_widget.setItem(r, 1, QTableWidgetItem(str("TOTALES")))
        for i in range(columns):
            self.table_widget.setItem(r, i + 2, QTableWidgetItem(str(self.matriz[rows][i])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



