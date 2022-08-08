pattern = input('Введите шаблон поздравления, в шаблоне можно '
                'использовать конструкцию {name} и {age}: '
                'С днём рождения, {name}! С {age}-летием тебя!: ')
names_lst = input('Список людей через запятую: ').split(', ')
ages_lst = input('Возраст людей через пробел: ').split()
print(ages_lst)
for i in range(len(ages_lst)):
    print('\n', pattern.format(name=names_lst[i], age=ages_lst[i]))

people_lst = [
    ' '.join([names_lst[i], ages_lst[i]]) for i in range(len(names_lst))
]
print('\nИменинники:', ', '.join(people_lst))

