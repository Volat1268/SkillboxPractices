available_films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов',
                   'Мементо', 'Отступники', 'Деревня']

new_favorite_films = []
new_films_count = int(input('Сколько фильмов хотите добавить? '))
for i in range(new_films_count):
    print('Введите название фильма:', end=' ')
    new_film = input()
    new_favorite_films.append(new_film)
print(new_favorite_films)


favorite_films = []
errors = []
for i in new_favorite_films:
    for j in available_films:
        if i == j:
            favorite_films.append(i)
        else:
            continue

for i in new_favorite_films:
    a = False
    for j in available_films:
        if i == j:
            a = True
            break
        else:
            continue
    if a == False:
        errors.append(i)
    else:
        continue

print('favorite_films:', favorite_films)
print('errors', errors)
