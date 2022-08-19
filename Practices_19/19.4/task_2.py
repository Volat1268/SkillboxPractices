import random
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums_1 = set(nums_1)
nums_2 = set(nums_2)
print('nums_1:', nums_1)
print('nums_2', nums_2)

nums_1_min = min(nums_1)
print('Минимальный элемент 1-го множества: {}'.format(nums_1_min))
nums_1.discard(nums_1_min)
print('nums_1 без минимального элемента 1-го множества: {}'.format(nums_1))
nums_2_min = min(nums_2)
print('Минимальный элемент 2-го множества: {}'.format(nums_2_min))
nums_2.discard(nums_2_min)
print('nums_2 без минимального элемента 2-го множества: {}'.format(nums_2))

rand_for_nums_1 = random.randint(100, 200)
print('Случайное число для 1-го множества:: {}'.format(rand_for_nums_1))
rand_for_nums_2 = random.randint(100, 200)
print('Случайное число для 1-го множества: {}'.format(rand_for_nums_2))

nums_1.add(rand_for_nums_1)
nums_2.add(rand_for_nums_2)

nums_union = nums_1 | nums_2
print('все элементы множеств (объединение): {}'.format(nums_union))

nums_inters = nums_1.intersection(nums_2)
print('только общие элементы (пересечение): {}'.format(nums_inters))

nums_only_2 = nums_2 - nums_1
print('элементы, входящие в nums_2, но не входящие в nums_1: {}'.format(nums_only_2))




