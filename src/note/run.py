from src.note.note_manage import *
import argparse



def run():

    parser = argparse.ArgumentParser(
        prog='Notes for console',
        description='''Консольное приложение заметки, с сохранением, чтением,
                    добавлением, редактированием и удалением заметок. Заметка
                    содержит идентификатор, заголовок, тело заметки и дату/время создания
                    или последнего изменения заметки''',
        epilog='(c) Разработал Pogudo Evgeny',
        add_help=True
    )

    parser.add_argument('-a', '--add', nargs='+', help='Введите имя заметки и текст через пробел')
    parser.add_argument('-d', '--delete', nargs=1, help='Функция для удаления, принимает один параметр - имя записи')
    parser.add_argument('-e', '--edit', nargs='*', help='Не принимает аргументов.')
    parser.add_argument('-r', '--read', nargs='*', help='Выводит список всех записей')

    args, unknown = parser.parse_known_args()
    while(args.add != None or args.delete != None or args.edit != None or args.read != None):
        if (args.add):
            if len(args.add) >= 2:
                add(args.add[0], args.add[1:])
            else: print("Неверное колличество аргументов")
            args.add = None
        elif(args.delete):
            delete(args.delete)
        elif(args.edit != None):
            edit()
        elif(args.read != None):
            if args.read:
                read(args.read[0])
            else: read()
            args.read = None
        if unknown:
            print ("Ошибка. Я таких команд не знаю :( '{}'".format (unknown) )