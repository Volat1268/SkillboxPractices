action = input('Введите операцию: ')
while action != '+' and action != '-' and action != '*' and action != '/':
  print('Ошибка: такой операции не существует. Попробуйте еще раз.')
  action = input('Введите операцию: ')
number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
if action == '+':
    print(number_one, '+', number_two, '=', number_one + number_two)
elif action == '-':
    print(number_one, '-', number_two, '=', number_one - number_two)
elif action == '*':
    print(number_one, '*', number_two, '=', number_one * number_two)
elif action == '/':
    print(number_one, '/', number_two, '=', number_one / number_two)


