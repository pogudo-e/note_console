import csv
from note.user import User
from datetime import datetime as dt

u = User()

def file_name():
    '''DATABASE . TXT'''
    return 'notes.csv'

#TODO так как при любой работе с заметками необходимо чтение из файла, возможно сразу сохранять и переменную или класс
# На вход получает файл и возвращает двумерный массив
def arrays(file):
    '''Full array objects: [[1,2,3][1,2,3][1,2,3]]'''
    file1 = open(file)
    file1.close
    res = []
    for line in file1:
        arr = line.split(',')
        res.append(arr)
    return res

# Находит максимальный id из имеющихся и возвращает id+1
def find_id():
    '''Folling the maximum identificator max < id '''
    count = 0
    arr = arrays(file_name())
    for i in range(0, len(arr)):
        try: 
            if int(arr[i][0]) > count: count = int(arr[i][0]) 
        except:
            continue    
    return str(count+1)

def to_file():
    with open(file_name(), 'a', newline='') as f:
        writer = csv.writer(f, delimiter=",", dialect='excel')
        writer.writerow([u.id, u.name, u.body, u.time])

def set_time(): return dt.now().strftime('%d/%m/%Y-%H:%M')



