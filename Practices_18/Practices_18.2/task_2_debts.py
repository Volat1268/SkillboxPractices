name = input('Введите имя: ')
debt = int(input('Введите долг: '))
message = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}'.format(name, debt)
print(message)