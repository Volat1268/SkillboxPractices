# my_list = [1, 2, 3]
# print(*my_list)

# ml = (1, 2, 3)
# print('One: {}, two: {}, three: {}'.format(*ml))

# my_dict = dict(name='Aleks', lang='Python')
# print('Name: {name}, Lang: {lang}'.format(**my_dict))


# lang_authors = [{'name': 'Aleks', 'lang': 'Python'}, {'name': 'Tom', 'lang': 'C'}]
# for i in lang_authors:
#     print('Name - {name}, Lang - {lang}'.format(**i))


def pers_lang_info(name, lang, *versions):
    print(f'Name: {name}, Lang: {lang}, versions:', *versions)

pers_lang_info('Aleks', 'Python', 1.2, 2.2, '3a')