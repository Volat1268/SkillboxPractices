notebook = dict()
names_lst = []
tel_lst = []
print('Текущие контакты на телефоне:\n')
while True:
    name = input('Введите имя: ')
    if name == 'Стоп':
        print('Запись контактов прекращается.')
        break
    else:
        while name in names_lst:
            print('Ошибка: такое имя уже существует.')
            name = input('Введите имя: ')
        notebook['Имя'] = names_lst
        names_lst.append(name)
        tel = input('Введите номер телефона: ')
        notebook['Телефон'] = tel_lst
        tel_lst.append(tel)
        print('\nТекущие контакты на телефоне:')
        for i_person in range(len(names_lst)):
            print('{0}   {1}'.format(notebook['Имя'][i_person], notebook['Телефон'][i_person]))
        print()



