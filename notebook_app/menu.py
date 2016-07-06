import sys
from notebook import Note, NoteBook

class Menu:
    '''Muesta un menu y responde a la opcion cuando se ejecuta'''
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
                "1" : self.show_notes,
                "2" : self.search_notes,
                "3" : self.add_note,
                "4" : self.modify_note,
                "5" : self.quit
                }
    def display_menu(self):
        print """
        NoteBook menu

        1. Mostrar todas las notas
        2. Buscar nota
        3. Agregar nota
        4. Modificar Nota
        5. Salir
        """
    def run(self):
        '''Muestra el menu y responde a una eleccion'''
        while True:
            self.display_menu()
            choice = input("Ingrese una opcion: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print "{0} no es una opcion valida".format(choice)
