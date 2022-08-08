num = int(input('Введите число: '))

square_num_dict = dict()

for i_num in range(1, num + 1):
    square_num_dict[i_num] = i_num ** 2

print('Результат: {}'.format(square_num_dict))