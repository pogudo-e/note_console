from src.note.secondary_func import *


def add(name, body):
    u.us(find_id(), name, ' '.join(body), set_time())
    to_file()

def delete(name):
    lines = list()

    with open(file_name(), 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == name:
                    lines.remove(row)
    with open(file_name(), 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

def edit():
    search_name = input('Введите имя редактируемой заметки')
    lines = arrays(file_name())
    with open(file_name(), 'w') as f2:
        for line in lines:
            try:
                if line[1] == search_name:
                    print('Вот что я нашел: ', line[1], ' and text: ', line[2])
                    new_body = input('Меняем на: ')
                    line[2], line[-1]= new_body, set_time()
                    f2.write(','.join(line))
                else:
                    f2.write(','.join(line))
            except:
                continue
        f2.write('\n')


def read(*i):
    result = None
    if not i:
        with open(file_name(), 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                print(' '.join(row))
    else:
        with open(file_name(), 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                for field in row:
                    if field == i[0]:
                        result = ' '.join(row)
        if not result:
            print('Ничего не найдено')
        else: print(result)