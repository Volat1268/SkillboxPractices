peap = {'Aleks': 123, 'Karl': 345, 'Mike': 567}
spec = dict(lector='Petrov', driver='Ivanov', artist='Sidorov')
res = dict([('aaa', [1, 2, 3]), ('bbb', [4, 5, 6]), ['ccc', [7, 8, 9]]])
smesh = dict({'BMW': 2222, 'Audi': 3333}, Renault=4444, Lada=6666)

stud = ['Artur', 'Andrey', 'Anton']
ages = [44, 55, 66]
ag_st = dict(zip(stud, ages))
# print(ag_st)

peap.update({'Nik': 789})
spec.update(doctor='Tarasov')
res.update([('ddd', [0, 0, 0]), ('eee', [10, 11, 21])])

# print(peap)
# print(spec)
# print(res)

# product = {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100, 'pillow': 10, 'shelf': 70, 'sofa': 400}
# new_pro = {product: value for product, value in product.items() if value < 100}
# print(new_pro)

works_of_art = {'The_Starry_Night': {'author': 'Van Gogh', 'year': 1889, 'style': 'post-impressionist'},
                'The_Birth_of_Venus': {'author': 'Sandro Botticelli', 'year': 1480, 'style': 'renaissance'},
                'Guernica': {'author': 'Pablo Picasso', 'year': 1937, 'style': 'cubist'},
                'American_Gothic': {'author': 'Grant Wood', 'year': 1930, 'style': 'regionalism'},
                'The_Kiss': {'author': 'Gustav Klimt', 'year': 1908, 'style': 'art nouveau'}}
# print(works_of_art['The_Kiss']['year'])

person = {}
s = 'IVANOV IVAN Samara SGU 5 4 5 5 3 5'
s_l = s.split()
# print(s_l)
person['name'] = s_l[0]
person['prename'] = s_l[1]
person['city'] = s_l[2]
person['univ'] = s_l[3]
person['marks'] = [int(mark) for mark in s_l[4:]]

for book in works_of_art:
    print(book, ':')
    for info, data in works_of_art[book].items():
        print(info, '-', data)

# print(person)
# for name, data in person.items():
#     print(name, data)
