zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(zoo.index('lion') + 1, 'bear')
zoo.remove('elephant')
place_lion = zoo.index('lion') + 1
place_monkey = zoo.index('monkey') + 1
print()
print('Зоопарк', zoo)
print('Лев сидит в клетке', place_lion)
print('Обезьяна сидит в клетке', place_monkey)
