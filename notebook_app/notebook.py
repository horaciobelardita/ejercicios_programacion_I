import datetime

# almacena el siguiente id disponible para las nuevas nota
last_id = 0

class Note:
    '''Representa una nota en el cuaderno'''
    def __init__(self, memo, tags=''):
        '''Inicializa una nota con contenido y un tag opcional.
        Automaticamente establece la fecha de creacion y un id unico'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determina si la nota coincide con el texto filter.
        Retorna true si coincide o falso de lo contrario.
        La busqueda es case sensitive y coincide con el texto
        y los tags'''
        return filter in self.memo or filter in self.tags

class NoteBook:
    '''Representa una coleccion de notas que pueden ser marcadas,
    modificadas y ser buscadas'''

    def __init__(self):
        '''Inicializa un cuaderno con una lista vacia'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Crea una nueva nota y la agrega a la lista.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Localiza la nota dado su id'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Busca la nota dado su id y cambia su texto por el
        valor dado'''
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Busca la nota dado su id y cambia su tag
        por el valor dado'''
        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''Busca todas las notas y las retorna que coincidan con el
        string filter'''
        return [note for note in self.notes if note.match(filter)]
