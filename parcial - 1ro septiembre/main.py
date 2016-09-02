ARCHIVO_VENDEDOR = 'VENDEDORES.txt'
ARCHIVO_ARTICULO = 'ARTICULOS.txt'
ARCHIVO_NOVEDAD = 'NOVEDADES.txt'


def upload_file(filename):
    '''
    Dado un nombre de archivo en formato txt, lo recorre y lo almacena
    en un dictionario
    :param filename: str() => 'example.txt'
    :return: dict(id => description)
    '''
    dictionary = {}
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            record = line.split(',')
            dictionary[int(record[0])] = record[1].strip()
            line = f.readline()
    return dictionary

def create_matriz(rows, columns):
    '''
    Retorna una matriz de 2 dimensiones de filas x columnas dadas como parametro
    :param rows: int()
    :param columns: int()
    :return: list[][]
    '''
    matriz = []
    for i in range(rows):
        matriz.append([0] * columns)
    return matriz


def generate_positions(collection):
    '''
    Dado un dictionario genera otro diccionario con clave article_id y valor
    posicion en la matriz
    :param collection: dict()
    :return: dict(int(article_id) => int(pos))
    '''
    dictionary = {}
    pos = 0
    for item in collection.items():
        dictionary[item[0]] = pos
        pos += 1
    return dictionary

def process(code, articles, year_input):
    '''
    Procesa el archivo de novedades dado un id de vendedor y un anio especifico
    :param code: int()
    :param articles: dict()
    :param year_input: int()
    :return: list[][]
    '''
    position_list = generate_positions(articles)
    # una fila y una columna mas para los totales
    rows = len(position_list) + 1
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
                matriz[position_list.get(article_id)][month - 1] += amount
                matriz[rows - 1][month - 1] += amount
                matriz[position_list.get(article_id)][12] += amount
            line = f.readline()
    return matriz

def calculate_total(matriz):
    '''
    Recorre la ultima columna de la matriz seria los totales de los meses
    y retorna el total acumulado
    :param matriz: list[][]
    :return: float()
    '''
    rows = len(matriz) - 1
    total = 0
    for i in range(rows):
        total += float(matriz[i][12])
    return total


def show_header():
    '''
    Imprime en pantalla el encabezado de la tabla para mostrar resultados
    :return: void
    '''
    e =  "COD ARTICULO\t\tDESCRIPCION\t\t1\t2\t3\t4\t5\t6\t7\t8\t\9\t10\t11\t12\tTOTAL"
    print e


def show_results(articulos, matriz):
    '''
    Recorre la matriz de totales y muestra en pantalla los resultados
    :param articulos: dict(article_id => description)
    :param matriz: list[][]
    :return: void()
    '''
    show_header()
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

def search_best_article(matriz):
    '''
    Retorna el articulo de mayor venta en la matriz
    :param matriz: list[][]
    :return: tuple(article_id, month)
    '''
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
    '''
    Busca el peor mes de venta del articulo pasado como parametro en matriz
    :param article_id: int()
    :param matriz: list[][]
    :return: int(month)
    '''
    row = article_id - 1
    menor = matriz[row][0]
    mes = 1
    for column in range(1, 12):
        if matriz[row][column] < menor:
            menor = matriz[row][column]
            mes = column + 1
    return mes


def month_to_str(x):
    '''
    Dado un valor numerico de 1 a 12 retorna su correspondiente mes
    en caso contrario retorna un string vacio
    :param x: int(4)
    :return: str() => "Abril"
    '''
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
        show_results(articles, totals)
        article = search_best_article(totals)
        print "Mejor Articulo => {} ${}".format(articles[article[0]], article[1])
        month_worst = search_worst_month(article[0], totals)
        print "Peor mes del mejor articulo => {}".format(month_to_str(month_worst))
    else:
        print "Vendedor no existe"
