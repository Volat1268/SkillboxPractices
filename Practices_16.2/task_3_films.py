def is_film_in_list(new_film, films):
    for i in films:
        if i == new_film:
            return True
    return False




films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_films = []

while True:
    print('Ваш текущий топ фильмов', my_films)
    print('Введите название фильма:', end=' ')
    new_film = input()
    print('Команды: 1 - добавить, 2 - вставить, 3 - удалить')
    command = int(input('Введите команду:'))
    while command != 1 and command != 2 and command != 3:
        print('Введена несуществующая команда')
        print('Команды: 1 - добавить, 2 - вставить, 3 - удалить')
        command = int(input('Введите команду:'))
    if command == 1:
        if is_film_in_list(new_film, films):
            print('Такой фильм уже есть в списке')
        else:
            my_films.append(new_film)
    if command == 3:
        if is_film_in_list(new_film, films):
            my_films.remove(new_film)
        else:
            print('Такого фильма нет в списке')
    if command == 2:
        if is_film_in_list(new_film, films):
            print('Такой фильм уже есть в списке')
        else:
            place = int(input('Каким по счету поставить фильм: 1, 2, 3 и т.д.: '))
            my_films.insert(place - 1, new_film)
    print(my_films)

