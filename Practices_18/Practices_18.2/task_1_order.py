name = input('Имя: ')
ord_nmb = int(input('Номер заказа: '))
# message = 'Здравствуйте, {name}! Ваш номер заказа: {ord_nmb}. Приятного дня!'.format(
#     name=name,
#     ord_nmb=ord_nmb
# )
# message = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(name, ord_nmb)
message = f'Здравствуйте, {name}! Ваш номер заказа: {ord_nmb}. Приятного дня!'

print(message)
