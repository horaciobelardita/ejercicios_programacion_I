import Tkinter as tk
import ttk

ARCHIVO_BANCOS = 'BANCOS.txt'

class App(tk.Frame):
    '''Representa el frame principal (container)'''
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        ttk.Label(self, text='BANCOS').grid(columnspan=2, row=0)
        ttk.Label(self, text='COD BANCO').grid(column=0, row=1)
        ttk.Label(self, text='DESCRIPCION').grid(column=1, row=1)
        self.text = tk.Text(self, width=50, height=15)
        self.text.grid(columnspan=2, row=2)
        ttk.Button(self, text='PROCESAR', command=self.show_banks).grid(row=3, columnspan=2)

    def __sort(self, matrix):
        '''Retorna la matriz ordenada por descripcion en orden alfabetico'''
        rows = len(matrix)
        columns = len(matrix[0])
        i = 0
        while i < rows:
            j = i
            while j < rows:
                if matrix[i][1] > matrix[j][1]:
                    aux = matrix[i][1]
                    aux_1 = matrix[i][0]
                    matrix[i][1] = matrix[j][1]
                    matrix[i][0] = matrix[j][0]
                    matrix[j][1] = aux
                    matrix[j][0] = aux_1
                j += 1
            i += 1
        return matrix


    def show_banks(self):
        # elimino el contenido del Text
        self.text.delete(0.0, tk.END)
        # subo a la matriz los bancos
        banks = self.__upload_banks()
        # ordenamiento de la matriz por descripcion
        self.__sort(banks)
        # recorrido de la matriz y muestro en el Text
        for row in banks:
            record = "\t{0}\t\t\t{1}\n".format(row[0], row[1])
            self.text.insert(tk.END, record)

    def __create_matrix(self, rows, columns):
        '''Retorna un matriz de rows x columns de 2 dimensiones'''
        m = []
        for i in range(rows):
            m.append([0] * columns)
        return m

    def __upload_banks(self):
        '''Retorna los bancos en una matriz leidos desde el
        archivo maestro de bancos'''
        with open(ARCHIVO_BANCOS, 'r') as f:
            # lectura de la cantidad de registros de BANCOS
            # creacion de la matriz
            lines = f.readlines()
            rows = len(lines)
            matriz = self.__create_matrix(rows, 2)
            f.seek(0, 0)
            line = f.readline()
            cr = 0
            # procesamiento del archivo de BANCOS
            # y carga en la matriz
            while line != '':
                record = line.split(',')
                matriz[cr][0] = record[0]
                matriz[cr][1] = record[1]
                cr += 1
                line = f.readline()
        return matriz


if __name__ == '__main__':
    root = tk.Tk()
    root.title('BANCOS')
    app = App(root)
    root.mainloop()
