import random
my_tuple_one = tuple([random.randint(0, 5) for n in range(10)])
my_tuple_two = tuple([random.randint(-5, 0) for n in range(10)])
my_tuple_three = my_tuple_one + my_tuple_two
print(f'Первый кортеж {my_tuple_one}')
print(f'Первый кортеж {my_tuple_two}')
print(f'Третий кортеж {my_tuple_three}')
print('Количество 0 в третьем кортеже:', my_tuple_three.count(0))

