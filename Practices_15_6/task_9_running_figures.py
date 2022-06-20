shift = int(input('Сдвиг: '))
first_list = [1, 4, -3, 0, 10]
changed_list = []

for i in range(len(first_list) - shift, len(first_list)):
    changed_list.append(first_list[i])
for i in range(len(first_list) - shift):
    changed_list.append(first_list[i])

print('\nИзначальный список', first_list)
print('Сдвинутый список', changed_list)