incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}

all_income = 0
for v_item in incomes.values():
    all_income += v_item
print('Общий доход за год составил {} рублей'.format(all_income))
print('Самый маленький доход у {title}. Он составляет {summ} руб.'
      .format(title=min(incomes, key=incomes.get), summ=incomes[min(incomes, key=incomes.get)]))
incomes.pop(min(incomes, key=incomes.get))
print('Итоговый словарь:', incomes)



