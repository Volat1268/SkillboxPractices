employees_count = int(input('Количество сотрудников: '))
staff = []
for i in range(employees_count):
    print('Зарплата', i + 1, 'сотрудника: ', end='')
    salary = int(input())
    staff.append(salary)

count_0 = 0
for i in staff:
    if i == 0:
        count_0 += 1

for i in range(count_0):
    staff.remove(0)

print('/nЗарплаты:', staff)
print('Максимальная зарплата:', max(staff))
print('Минимальная зарплата:', min(staff))




