path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
end_f = input('Требуемое расширение файла: ')

if path.lower().endswith(end_f.lower()) and path.lower().startswith(disk.lower()):
    print('Путь корректен!')
else:
    print('Проверьте правильность написания пути к файлу.')