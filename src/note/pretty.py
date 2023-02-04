from prettytable import PrettyTable

def read_w(liste):
    x = PrettyTable()
    x.field_names = ["ID", "NAME", "BODY", "DATE"]
#TODO Обоаботать вывод при None
    if liste == None: return print('Pusto')
    if len(liste) > 4:
        for li in liste: x.add_row([li[0],li[1],li[2],li[3]])
    else: x.add_row([liste[0][1],liste[0][1],liste[0][2],liste[0][3]])
    print(x) 
