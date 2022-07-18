text = input('Введите строку: ')
smbl_nmb = int(input('Номер символа: '))

text_list = list(text)
your_smbl = text_list[smbl_nmb - 1]
count_smbl = 0
for i in text_list:
    if i == your_smbl:
        count_smbl += 1

print('\nСимвол слева:', text_list[smbl_nmb - 2])
print('Символ справа:', text_list[smbl_nmb])

if count_smbl == 1:
    print('Таких же символов нет')
elif count_smbl == 2:
    print('Есть ровно один такой же символ')
elif count_smbl == 3:
    print('Есть два таких же символа')
elif count_smbl > 3:
    print('Есть еще', count_smbl - 1, 'таких же символов')
