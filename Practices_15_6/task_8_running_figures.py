shift = int(input('Сдвиг: '))
original_list = [1, 4, -3, 0, 10]
shifted_list = []

for i in range(len(original_list) - shift, len(original_list)):
    shifted_list.append(original_list[i])
for i in range(len(original_list) - shift):
    shifted_list.append(original_list[i])

print('\nИзначальный список', original_list)
print('Сдвинутый список', shifted_list)
