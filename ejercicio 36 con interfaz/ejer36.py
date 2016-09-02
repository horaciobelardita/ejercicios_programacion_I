import Tkinter as tk
import tkFileDialog, tkMessageBox
import ttk
import numpy


def askopenfileseller():
    ''' Abre el dialogo de archivo para el archivo maestro
    de vendedores y almacena el nombre de archivo en el entry'''
    global entry_seller
    # obtener el nombre de archivo
    filename = tkFileDialog.askopenfilename()
    # abrir el Archivo
    if filename:
        # inserto el nombre de archivo en el entry
        entry_seller.set(filename)

def askopenfilenews():
    ''' Abre el dialogo de archivo para el archivo de novedades
     y si selecciona un archivo  almacena  el nombre de archivo
     en el entry'''
    global entry_news
    # obtener el nombre de archivo
    filename = tkFileDialog.askopenfilename()
    # abrir el Archivo
    if filename:
        # inserto el nombre de archivo en el entry
        entry_news.set(filename)



def upload_sellers(filename):
    ''' Retorna un diccionario con todos los vendedores del
    archivo maestro dict[cod_vendedor] = nombre_apellido '''
    sellers = {}
    with open(filename) as f:
        line = f.readline()
        while line != '':
            record = line.split(',')
            # dict[cod_vendedor] = nombre_apellido
            sellers[int(record[0])] = record[1]
            line = f.readline()
    return sellers

def table(root):
    ''' Genera el encabezado tipo tabla para representar
    los resultados'''
    ttk.Label(root, text='Informe Vendedores').grid(row=3, columnspan=3)
    headers = ['COD. VEND', 'NOMBRE APELLIDO', 'SUCURSALES', 'TOTAL']
    for k, header in enumerate(headers):
        l = ttk.Label(root, text=header, borderwidth=5, relief=tk.SUNKEN)
        if header == 'SUCURSAL':
            l.grid(row=4, column=k, columnspan=4)
        elif header == 'TOTAL':
            l.grid(row=4, column=k+4)
        else:
            l.grid(row=4, column=k)


def matrix(filename, sellers):
    '''Creacion de la matriz con filas => nro vendedores + total
    columnas => sucursales + total '''
    rows = len(sellers) + 1
    columns = 6
    matriz = numpy.zeros((rows, columns))
    # procesar el archivo de novedades
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            record = line.split(',')
            # codigo de sucursal
            cod_suc = int(record[0])
            # codigo de vendedor
            cod_v = int(record[1])
            # importe
            imp = float(record[4])
            # cantidad
            cant = int(record[5])
            # acumular los importes en la matriz
            matriz[cod_v-1][cod_suc-1] += imp * cant
            matriz[rows-1][cod_suc-1] += imp * cant
            matriz[cod_v-1][5] += imp * cant
            line = f.readline()
    return matriz


def process_files(f_seller, f_news, master):
    # muestro el encabezado
    table(master)
    # subo los vendedores  del maestro a un diccionario
    sellers = upload_sellers(f_seller)
    matriz = matrix(f_news, sellers)
    length = len(sellers)
    row = 5
    # armado y muestra del grid de resultados
    for cod, name in sellers.items():
        ttk.Label(master, relief=tk.GROOVE, text=str(cod)).grid(column=0, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=name).grid(column=1, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][0])).grid(column=2, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][1])).grid(column=3, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][2])).grid(column=4, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][3])).grid(column=5, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][4])).grid(column=6, row=row)
        ttk.Label(master, relief=tk.GROOVE, text=str(matriz[cod-1][5])).grid(column=7, row=row)
        row += 1
    # total de totales
    total = 0
    for i in range(len(sellers)):
        total += matriz[i][5]
    ttk.Label(master, text='TOTAL').grid(column=1, row=row)
    ttk.Label(master, text=str(matriz[length][0])).grid(column=2, row=row)
    ttk.Label(master, text=str(matriz[length][1])).grid(column=3, row=row)
    ttk.Label(master, text=str(matriz[length][2])).grid(column=4, row=row)
    ttk.Label(master, text=str(matriz[length][3])).grid(column=5, row=row)
    ttk.Label(master, text=str(matriz[length][4])).grid(column=6, row=row)
    ttk.Label(master, text=str(total)).grid(column=7, row=row)

def process():
    global entry_seller, entry_news, root
    if entry_seller.get() != '' and entry_news.get() != '':
        process_files(entry_seller.get(), entry_news.get(), root)
    else:
        tkMessageBox.showerror('Error', 'Debe seleccionar los archivos')


# ventana principal
root = tk.Tk()

# etiqueta, textbox y boton para el archivo maestro de vendedores
label_seller = ttk.Label(root, text='Archivo vendedores')
label_seller.grid(column=0, row=0)
entry_seller = tk.StringVar()
entry_1 = ttk.Entry(root, textvariable=entry_seller, width=50)
entry_1.grid(column=1, row=0)
button_1 = ttk.Button(root, text='Buscar', command=askopenfileseller)
button_1.grid(column=2, row=0)

# etiqueta, textbox y boton para el archivo de novedades
label_news = ttk.Label(root, text='Archivo novedades')
label_news.grid(column=0, row=1)
entry_news = tk.StringVar()
entry_2 = ttk.Entry(root, textvariable=entry_news, width=50)
entry_2.grid(column=1, row=1)
button_2 = ttk.Button(root, text='Buscar', command=askopenfilenews)
button_2.grid(column=2, row=1)

# boton procesar
process_button = ttk.Button(root, text='Procesar', command=process)
process_button.grid(columnspan=3, row=2)


root.mainloop()
