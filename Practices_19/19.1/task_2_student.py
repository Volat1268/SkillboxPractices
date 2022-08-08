student_info = input('Введите информацию о студенте через пробел \n'
                     '(фамилию, имя, город, вуз, все его оценки): ')

student_info_lst = student_info.split()
student_info_dict = dict()

student_info_dict['Фамилия'] = student_info_lst[0]
student_info_dict['Имя'] = student_info_lst[1]
student_info_dict['Город'] = student_info_lst[2]
student_info_dict['ВУЗ'] = student_info_lst[3]
student_info_dict['Оценки'] = []
for i_grade in student_info_lst[4:]:
    student_info_dict['Оценки'].append(i_grade)

print('\nРезультат:')
for stud in student_info_dict:
    print('{0}- {1}'.format(stud, student_info_dict[stud]))

