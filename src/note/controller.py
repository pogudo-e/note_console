from note.Note_manage import NoteManage
from note.pretty import *

note = NoteManage



def read(*i):
    read_list = note.read(*i)
    read_w(read_list)

def edit():
    note.edit()

def delete(t):
    note.delete(t)

def add(name, body):
    read_w(note.add(name, body))