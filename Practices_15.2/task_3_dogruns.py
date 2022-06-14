dogs_count = int(input('Количество собак, участвующих в бегах: '))
print()
dogs_points = []
for dog in range(dogs_count):
    print('Введите количество очков для', dog + 1, 'собаки: ', end='')
    points = int(input())
    dogs_points.append(points)
print('\nТабло с баллами у собак:', dogs_points)

maks = dogs_points[0]
minim = dogs_points[0]
i_count = 0
i_count_minim = 0
i_count_maks = 0
for i in dogs_points:
    if i < minim:
        minim = i
        i_count_minim = i_count
    if i > maks:
        maks = i
        i_count_maks = i_count
    i_count += 1

dogs_points[i_count_minim], dogs_points[i_count_maks] = dogs_points[i_count_maks], dogs_points[i_count_minim]
new_list = []
i_count = 0
for i in dogs_points:
    new_list.append(i)
print('Исправленное табло с баллами у собак: ', new_list)

