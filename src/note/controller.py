from note.Note_manage import NoteManage
from note.pretty import *

note = NoteManage

def read(*i): read_w(note.read(*i))

def edit(): note.edit(input('Введите имя редактируемой заметки'))
    
def delete(t): read_w(note.delete(' '.join(map(str, t))))

def add(name, body): read_w(note.add(name, body))