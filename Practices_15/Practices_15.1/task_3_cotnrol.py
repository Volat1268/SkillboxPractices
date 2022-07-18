staff = []
quontity_empl = int(input('Введите количество сотрудников: '))
absence = True

for _ in range(quontity_empl):
    id = int(input('ID сотрудника: '))
    staff.append(id)

f_id = int(input('Какой ID ищем? '))
for i in staff:
    if f_id == i:
        absence = False

if absence:
    print('Сотрудник не работает!')
else:
    print('Сотрудник на месте.')
