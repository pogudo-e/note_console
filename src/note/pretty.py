from prettytable import PrettyTable

def read_w(liste):
    x = PrettyTable()
    x.field_names = ["ID", "NAME", "BODY", "DATE"]

#TODO Обоаботать вывод при None https://stackoverflow.com/questions/22560768/add-multiple-line-in-python-single-table-cell
    if liste == None: return print(nonefunc(x))
    if len(liste) > 4:
        for li in liste: x.add_row([li[0],li[1],li[2],li[3]])
    else: x.add_row([liste[0][0],liste[0][1],liste[0][2],liste[0][3]])
    x.sortby="DATE"
    x.reversesort=True
    print(x) 

def nonefunc(x):
    return x.get_string(title="No result's")

# def datef(timestring):
#     pt = datetime.strptime(timestring,'%d/%m/%Y-%H:%M,%f')
#     total_seconds = pt.second + pt.minute*60 + pt.hour*3600 + pt.day*86400

# def datesort(ll):
#     for lst in ll:
#         sorted(lst[-1], key=lambda x: datetime.strptime(x, '%d/%m/%Y-%H:%M'))
#     return lst