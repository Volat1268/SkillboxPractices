text = input('Введите строку с двоеточиями: ')
text_list = list(text)

new_text = ''
count = 0
for i in text_list:
    if i == ':':
        i = ';'
        count += 1
    new_text += i

print('\nИсправленная строка:', new_text)
print('Количество замен:', count)
