list_container_weights = []
containers_count = int(input('Количество контейнеров: '))
for i in range(containers_count):
    print('Введите вес контейнера:', end=' ')
    weight = int(input())
    while weight > 200:
        print('Вес контейнера не должен превышать 200 кг.')
        print('Введите правильный вес контейнера:', end=' ')
        weight = int(input())
    list_container_weights.append(weight)

new_container_weight = int(input('Введите вес нового контейнера: '))
while new_container_weight > 200:
    print('Вес контейнера не должен превышать 200 кг.')
    new_container_weight = int(input('Введите правильный вес нового контейнера: '))

count = 1
for i in list_container_weights:
    if i >= new_container_weight:
        count += 1
    else:
        break

print('Номер, который получит новый контейнер:', count)
