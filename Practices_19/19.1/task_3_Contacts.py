print('Текущие контакты на телефоне:\n')
notebook = dict()
while True:
    name = input('Введите имя: ')
    if name == 'Стоп':
        print('Запись контактов прекращена.')
        break
    else:
        while name in notebook:
            print('Ошибка: такое имя уже существует.')
            name = input('Введите имя: ')
        tel = input('Введите номер телефона: ')
        notebook[name] = tel
        print(notebook)
        for contact in notebook:
            print('{0}   {1}'.format(contact, notebook[contact]))
