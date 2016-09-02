ARCHIVO_VENDEDOR = 'VENDEDORES.txt'
ARCHIVO_ARTICULO = 'ARTICULOS.txt'
ARCHIVO_NOVEDAD = 'NOVEDADES.txt'


def upload_file(filename):
    dictionary = {}
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            record = line.split(',')
            dictionary[int(record[0])] = record[1].strip()
            line = f.readline()
    return dictionary

def create_matriz(rows, columns):
    matriz = []
    for i in range(rows):
        matriz.append([0] * columns)
    return matriz



def process(code, articles, year_input):
    # una fila y una columna mas para los totales
    rows = len(articles) + 1
    columns = 12 + 1
    matriz = create_matriz(rows, columns)
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
            if code == seller_id and year_input == year:
                amount = price * qtd
                matriz[article_id - 1][month - 1] += amount
                matriz[rows - 1][month - 1] += amount
                matriz[article_id - 1][12] += amount
            line = f.readline()
    return matriz

def calculate_total(matriz):
    rows = len(matriz) - 1
    total = 0
    for i in range(rows):
        t = matriz[i][12]
        total += t
    return total


def show_results(articulos, matriz):
    rows = len(matriz) - 1
    columns = len(matriz[0])
    k_articulos = articulos.keys()
    for i in range(rows):
        msg = "{}\t\t\t\t{}\t\t\t\t".format(k_articulos[i], articulos[k_articulos[i]])
        for j in range(columns):
            msg += str(matriz[i][j]) + "\t"
        msg += '\n'
        print msg
    msg = "TOTAL GENERAL\t\t\t\t\t\t"
    for i in range(columns):
        msg += str(matriz[rows][i]) + "\t"
    print msg

def show_header():
    e =  "COD ARTICULO\t\tDESCRIPCION\t\t1\t2\t3\t4\t5\t6\t7\t8\t\9\t10\t11\t12\tTOTAL"
    print e

def search_best_article(matriz):
    rows = len(matriz) - 1
    mayor = 0
    article = 0, ""
    for i in range(rows):
        for j in range(12):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
                article = i+1, mayor
    return article

def search_worst_month(article_id, matriz):
    row = article_id - 1
    menor = matriz[row][0]
    mes = 1
    for column in range(1, 12):
        if matriz[row][column] < menor:
            menor = matriz[row][column]
            mes = column + 1
    return mes


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


if __name__ == '__main__':
    cod_vendedor = int(raw_input("Codigo de vendedor: "))
    sellers = upload_file(ARCHIVO_VENDEDOR)
    if cod_vendedor in sellers:
        print sellers[cod_vendedor]
        year = int(raw_input("Anio: "))
        articles = upload_file(ARCHIVO_ARTICULO)
        totals = process(cod_vendedor, articles, year)
        totals[len(totals) - 1][12] = calculate_total(totals)
        show_header()
        show_results(articles, totals)
        article = search_best_article(totals)
        print "Mejor Articulo => {} ${}".format(articles[article[0]], article[1])
        month_worst = search_worst_month(article[0], totals)
        print "Peor mes del mejor articulo => {}".format(month_to_str(month_worst))
    else:
        print "Vendedor no existe"
