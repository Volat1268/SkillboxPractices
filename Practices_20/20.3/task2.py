import random
import string

lst_1 = [random.choice(string.ascii_lowercase) for i in range(10)]
lst_2 = [random.choice(string.ascii_lowercase) for j in range(10)]
# print(f'Первый лист: {lst_1}')
# print(f'Второй лист: {lst_2}')
dct_1 = dict(enumerate(lst_1))
# dct_1 = {i: v for (i, v) in enumerate(lst_1)}
dct_2 = {i: v for (i, v) in enumerate(lst_2)}
print(f'Первый словарь: {dct_1}')
print(f'Второй словарь: {dct_2}')

# dct_2 = {i: v for (i, v) in enumerate(lst_2)}