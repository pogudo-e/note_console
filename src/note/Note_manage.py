from note.secondary_func import *

class NoteManage:
    def add(name, body):
        u.us(find_id(), name, ' '.join(body), set_time())
        to_file()
#TODO убрать такой кривой ретюрн
        return [[u.id, u.name, u.body, u.time]]

#TODO чтение из файла изменить на фу
    def delete(name):
        lines = list()
        sear = None
        r = None
        with open(file_name(), 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                print(row)
                lines.append(row)
                for field in row:
                    if field == name:
                        r = row
                        lines.remove(row)
                        sear = field
            if sear == None: return None
        with open(file_name(), 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        if sear != None: return[r]

#TODO - убрать принты, возможно вынести инпуты
    def edit(search_name):
        lines = arrays(file_name())
        with open(file_name(), 'w') as f2:
            for line in lines:
                try:
                    if line[1] == search_name:
                        print('Вот что я нашел: ', line[1], ' and text: ', line[2])
                        new_body = input('Меняем на: ')
                        line[2], line[-1]= new_body, set_time()
                        f2.write(','.join(line))
                        continue
                    else:
                        f2.write(','.join(line))
                except:
                    continue
            f2.write('\n')
        return


    def read(*i):
        result = []
        body = arrays(file_name())
        if not i:
            for row in body:
                result.append(row)
        else:
            for row in body:
                for field in row:
                    if field == i[0]:
                        result.append(row)
            if not result:
                return None
        return result