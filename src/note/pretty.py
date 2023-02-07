from prettytable import PrettyTable

def read_w(liste):
    x = PrettyTable(field_names=["ID", "NAME", "BODY", "DATE"])

#TODO Обоаботать вывод при None https://stackoverflow.com/questions/22560768/add-multiple-line-in-python-single-table-cell
    if liste == None: return print(nonefunc(x))
    if len(liste) > 1:
        for li in liste: x.add_row([li[0],li[1],li[2],li[3]])
    else: 
        x.add_row([liste[0][0],liste[0][1],liste[0][2],liste[0][3]])
    x.sortby="DATE"
    x.reversesort=True
    print(x) 

def nonefunc(x): return x.get_string(title="No result's")
