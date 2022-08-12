small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

# while True:
#     item = input('Введите название товара: ')
#     if item == 'стоп':
#         print('Поиск товара остановлен. До встречи!')
#         break
#     else:
#         print('Количество товара "{0}" на складе: {1}'.format(item, big_storage.get(item, 'Товар отсутствует')))

item = input('Введите название товара: ')
while item != 'стоп':
    print('Количество товара "{0}" на складе: {1}'.format(item, big_storage.get(item, 'Товар отсутствует')))
    item = input('Введите название товара: ')
print('Поиск товара остановлен. До встречи!')