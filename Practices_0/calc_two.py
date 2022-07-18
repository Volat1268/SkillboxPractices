action = input('Введите операцию: ')
while action != '+' and action != '-' and action != '/' and action != '*':
    print('Ошибка: такой операции не существует. Попробуйте еще раз.')
    action = input('Введите операцию: ')
seqNum = int(input('Сколько операндов? '))
result = int(input('Введите операнд 1: '))
formula = str(result)
for i in range(2, seqNum + 1):
    print('Введите операнд ', i, ':', sep='', end=' ')
    num = int(input())
    if action == '-':
        result -= num
        formula += ' - ' + str(num)
    elif action == '*':
        result *= num
        formula += ' * ' + str(num)
    elif action == '/':
        result /= num
        formula += ' / ' + str(num)
    elif action == '+':
        result += num
        formula += ' + ' + str(num)
print(formula, '=', result)
