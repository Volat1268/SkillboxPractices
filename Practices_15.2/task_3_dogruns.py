dogs_count = int(input('Количество собак, участвующих в бегах: '))
dogs_points = []
for dog in range(dogs_count):
    print('Введите количество очков для', dog + 1, 'собаки: ', end='')
    points = int(input())
    dogs_points.append(points)
print('Очки собак:', dogs_points)

maks = minim = dogs_points[0]

for i in dogs_points:
    if i < minim:
        minim = i
    if i > maks:
        maks = i
print('maks:', maks, 'min', minim)
print(dogs_points.index(maks))
print(dogs_points.index(minim))

