sym = {'.', ',', ';', ':', '!', '?'}
text = input('Введите строку: ')
count = 0
for s in text:
    if s in sym:
        count += 1
print('Количество знаков пунктуации: {}'.format(count))
