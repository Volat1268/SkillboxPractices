txt = input('Введите строку: ')
# print('Ответ:', end=' ')
# for i, v in enumerate(txt):
#     if v == '~':
#        print(i, end=' ')

def indexes_of_symbol(txt, sym):
    return ' '.join(str(i) for i, v in enumerate(txt) if v == sym)

print('Ответ:', indexes_of_symbol(txt, '~'))