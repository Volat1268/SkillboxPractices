txt = input('Введите строку: ')
lower = [i for i in range(len(txt)) if txt[i].islower()]
upper = [i for i in range(len(txt)) if txt[i].isupper()]

if len(lower) > len(upper):
    print(txt.lower())
else:
    print(txt.upper())
